from xml.dom import minidom

class LionDBAudioMixIn():
    def accept_all_temp_audio(self, langid):
        """copy the audio uris from the tempaudio table to the permanent table for the given language.
        note that the file copying must be done by hand."""
        request = """SELECT xmlid FROM tempaudio WHERE langid="%s" """ % langid
        self.execute_query(request)
        for row in self.cursor.fetchall():
            self.accept_temp_audio(langid, row[0])
    
    def clear_all_temp_audio(self, langid):
        """clear all rows in the tempaudio table for the given language"""
        request = """DELETE FROM tempaudio WHERE langid="%s" """ % langid
        self.execute_query(request)
    
    def accept_temp_audio(self, langid, xmlid):
        """copy a single audio uri from the tempaudio table to the permanent language table
        note that the file copying must be done by hand."""
        request = """SELECT audiouri FROM tempaudio WHERE xmlid="%s" and langid="%s" """ \
            % (xmlid, langid)
        self.execute_query(request)
        if self.cursor.rowcount == 0:
            self.warn("No audio found.")
            return
        
        audio_dir_prefix = self.config["main"]["audio_dir_prefix"]
        if not audio_dir_prefix.endswith("/"): audio_dir_prefix += "/"
        audiofile = audio_dir_prefix + os.path.basename(self.cursor.fetchone()[0])
        self.trace_msg("Saving audio to language table as %s" % audiofile)    
        request = """UPDATE %s SET audiouri="%s" WHERE xmlid="%s" """ \
            % (self.make_table_name(langid), audiofile, xmlid)
        self.execute_query(request)
        self.clear_temp_audio(langid, xmlid)
    
    def clear_temp_audio(self, langid, xmlid):
        """clear a single row from the tempaudio table for the given language"""
        request = """DELETE FROM tempaudio WHERE xmlid="%s" and langid="%s" """ \
            % (xmlid, langid)
        self.execute_query(request)
    
    def import_audio_prompts(self, langid, ncx, audio_is_temporary=False):
        """Fill up the database with prompts file names. We use the NCX file
        from the Obi export and match the navPoint text label with textstrings
        in the DB."""
        self.trace_msg("Getting audio prompts from NCX")
        try:
            dom = minidom.parse(ncx)
        except Exception, e:
            self.die("""Couldn't open "%s" (%s)""" % (ncx, e))
        self.execute_query("SELECT xmlid, textstring FROM " +
                self.make_table_name(langid))
        db_items = self.cursor.fetchall()
        xml_labels = dom.getElementsByTagNameNS(
            "http://www.daisy.org/z3986/2005/ncx/", "navLabel")
        self.trace_msg("Got %d labels for %d strings" %
            (xml_labels.__len__(), db_items.__len__()))
        
        for xml_label, db_item in zip(xml_labels, db_items):
            db_xmlid = db_item[0]
            db_text = db_item[1]
            xml_text = xml_label.getElementsByTagNameNS(
                "http://www.daisy.org/z3986/2005/ncx/", "text")[0].firstChild.data
            xml_audio_src = xml_label.getElementsByTagNameNS(
                "http://www.daisy.org/z3986/2005/ncx/", "audio")[0].getAttribute("src")
            if xml_text == db_text and xml_audio_src != "":
                # if we're writing permanent audio uris to the language table
                if audio_is_temporary == False:
                    self.execute_query("""UPDATE %s SET audiouri="%s" WHERE xmlid="%s" """ %
                        (self.make_table_name(langid), xml_audio_src, db_xmlid))
                
                # or we're writing to the temp audio table
                else:
                    a, b = self.get_tempaudio_paths(langid)
                    self.write_tempaudio(db_xmlid, langid, b + xml_audio_src)
            else:
                self.warn("""No match between db string="%s" and ncx label="%s"?! (id = %s)""" %
                        (db_text, xml_text, db_xmlid))


    def write_tempaudio(self, xmlid, langid, file):
        # update the tempaudio table
        # does this have an entry already?
        request = """SELECT id FROM tempaudio WHERE xmlid="%s" and langid="%s" """ % \
            (xmlid, langid)
        self.execute_query(request)
        # if so, just update it
        if self.cursor.rowcount > 0:
            request = """UPDATE tempaudio SET audiouri="%(audiouri)s" WHERE 
                xmlid="%(xmlid)s" AND langid="%(langid)s" """  % \
                {"audiouri": file, "xmlid": xmlid, "langid": langid}
        # otherwise create a new entry
        else:
            request = """INSERT INTO tempaudio (audiouri, xmlid, langid) VALUES
                ("%(audiouri)s", "%(xmlid)s", "%(langid)s" ) """ % \
                {"audiouri": file, "xmlid": xmlid, "langid": langid}
        self.execute_query(request)

    def get_tempaudio_paths(self, langid):
        temp_audio_dir = self.config["main"]["temp_audio_dir"]
        temp_audio_uri = self.config["main"]["temp_audio_uri"]
        
        # calculate the filesystem path to the temporary file storage
        if not temp_audio_dir.endswith("/"): temp_audio_dir += "/"
        save_to_dir =  temp_audio_dir + langid + "/"

        # this is the URI used to read the temporary file back from the web server
        # we'll link to the temp file until it gets integrated into the permanent fileset (done manually for now)
        if not temp_audio_uri.endswith("/"): temp_audio_uri += "/"
        www_dir = temp_audio_uri + langid + "/"
        return save_to_dir, www_dir