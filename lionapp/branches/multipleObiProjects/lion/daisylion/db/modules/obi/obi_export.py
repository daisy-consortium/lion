from xml.dom import minidom
import obi_import
import re

def export_resx(session, langid, dir):
    """Export strings for the language given by langid to a directory, using
    the original files as templates. Save to the same directory, keeping the
    same file names with only the two-letter language code as a suffix (e.g.,
    Dialogs/About.resx becomes Dialogs/About.gi.resx)"""
    dir = re.sub("/$", "", dir)
    session.trace_msg("export_resx %s %s %s" % (session, langid, dir))
    session.execute_query(
        """SELECT langid_short FROM languages WHERE langid="%s" """ \
        % langid)
    langid_short, = session.cursor.fetchone()
    session.trace_msg("langid_short = %s" % langid_short)
    all_strings = fetch_strings(langid, session)
    apply_mnemonics(all_strings, session)
    strings = all_strings["STRING"]
    for file in strings.keys():
        path_orig = dir + "/" + file + ".resx"
        path = dir + "/" + file + "." + langid_short + ".resx"
        session.trace_msg("* %s" % path)
        try:
            doc = minidom.parse(path_orig)
            # index data element by name for easy reference
            datas = dict(map(lambda d: (d.attributes["name"].nodeValue, d),
                doc.getElementsByTagName("data")))
            for name, textstr in strings[file].iteritems():
                session.trace_msg("  + %s=%s" % (name, textstr))
                if datas.has_key(name):
                    data = datas[name]
                    text = doc.createTextNode(textstr)
                    value = data.getElementsByTagName("value")[0]
                    if value.hasChildNodes():
                        value.normalize()
                        value.replaceChild(text, value.firstChild)
                else:
                    session.warn("No data element named %s in %s" %
                        (name, path_orig))
            f = open(path, "w")
            session.trace_msg("Writing %s" % f)
            f.write(doc.toxml())
            f.close()
        except Exception, e:
            session.die("Couldn't export %s (%s)" % (path, e), 1)


def apply_mnemonics(strings, session):
    """Apply mnemonics to strings by reintroducing the & special form."""
    for file in strings["MNEMONIC"].keys():
        for name, mnemonic in strings["MNEMONIC"][file].iteritems():
            if strings["STRING"].has_key(file) and \
                strings["STRING"][file].has_key(name):
                s = strings["STRING"][file][name]
                ss = re.sub("(%s)" % mnemonic, "&\\1", s, 1)
                if s == ss:
                    strings["STRING"][file][name] = "%s (&%s)" % (s, mnemonic)
                else:
                    strings["STRING"][file][name] = ss
            else:
                session.warn("No match in strings for mnemonic %s:%s" \
                    (file, name))

def fetch_strings(langid, session):
    """Fetch all strings from the DB and organize them by role, file, and
    name. Return the dictionary of these strings."""
    strings = {}
    session.execute_query("SELECT xmlid, textstring, role FROM %s" % session.make_table_name(langid))
    for row in session.cursor.fetchall():
        xmlid, textstring, role = row
        m = re.match("([^:]+):([^:]+)", xmlid)
        if m:
            files, name = m.groups()
            for file in files.rsplit(";"):
                if not strings.has_key(role): strings[role] = {}
                if not strings[role].has_key(file): strings[role][file] = {}
                strings[role][file][name] = textstring
    return strings
