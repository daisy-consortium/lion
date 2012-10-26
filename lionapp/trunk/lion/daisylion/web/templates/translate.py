#!/usr/bin/env python




##################################################
## DEPENDENCIES
import sys
import os
import os.path
try:
    import builtins as builtin
except ImportError:
    import __builtin__ as builtin
from os.path import getmtime, exists
import time
import types
from Cheetah.Version import MinCompatibleVersion as RequiredCheetahVersion
from Cheetah.Version import MinCompatibleVersionTuple as RequiredCheetahVersionTuple
from Cheetah.Template import Template
from Cheetah.DummyTransaction import *
from Cheetah.NameMapper import NotFound, valueForName, valueFromSearchList, valueFromFrameOrSearchList
from Cheetah.CacheRegion import CacheRegion
import Cheetah.Filters as Filters
import Cheetah.ErrorCatchers as ErrorCatchers
from xhtml import xhtml

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '2.4.4'
__CHEETAH_versionTuple__ = (2, 4, 4, 'development', 0)
__CHEETAH_genTime__ = 1348528239.683658
__CHEETAH_genTimestamp__ = 'Mon Sep 24 16:10:39 2012'
__CHEETAH_src__ = 'translate.tmpl'
__CHEETAH_srcLastModified__ = 'Thu Dec  8 06:01:44 2011'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class translate(xhtml):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(translate, self).__init__(*args, **KWs)
        if not self._CHEETAH__instanceInitialized:
            cheetahKWArgs = {}
            allowedKWs = 'searchList namespaces filter filtersLib errorCatcher'.split()
            for k,v in KWs.items():
                if k in allowedKWs: cheetahKWArgs[k] = v
            self._initCheetahInstance(**cheetahKWArgs)
        

    def title(self, **KWS):



        ## CHEETAH: generated from #def title at line 17, col 1.
        trans = KWS.get("trans")
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        _v = VFFSL(SL,"appname",True) # u'$appname' on line 18, col 1
        if _v is not None: write(_filter(_v, rawExpr=u'$appname')) # from line 18, col 1.
        write(u''' translation for ''')
        _v = VFFSL(SL,"language",True) # u'$language' on line 18, col 26
        if _v is not None: write(_filter(_v, rawExpr=u'$language')) # from line 18, col 26.
        write(u'''
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def page(self, **KWS):



        ## CHEETAH: generated from #def page at line 20, col 1.
        trans = KWS.get("trans")
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        _v = VFFSL(SL,"section",True) # u'$section' on line 21, col 1
        if _v is not None: write(_filter(_v, rawExpr=u'$section')) # from line 21, col 1.
        write(u''' section
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def usepages(self, **KWS):



        ## CHEETAH: generated from #def usepages at line 23, col 1.
        trans = KWS.get("trans")
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write(u'''False
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def body(self, **KWS):



        ## CHEETAH: generated from #def body at line 26, col 1.
        trans = KWS.get("trans")
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write(u'''
''')
        #  calculate the drop down list default value
        all_selected = ""
        newtodo_selected = ""
        new_selected = ""
        todo_selected = ""
        allok_selected = ""
        if VFFSL(SL,"last_view",True) == "todo": # generated from line 34, col 1
            todo_selected = "SELECTED"
        elif VFFSL(SL,"last_view",True) == "newtodo": # generated from line 36, col 1
            newtodo_selected = "SELECTED"
        elif VFFSL(SL,"last_view",True) == "new": # generated from line 38, col 1
            new_selected = "SELECTED"
        elif VFFSL(SL,"last_view",True) == "allok": # generated from line 40, col 1
            allok_selected = "SELECTED"
        else: # generated from line 42, col 1
            all_selected = "SELECTED"
        write(u'''
<h1>''')
        _v = VFFSL(SL,"title",True) # u'$title' on line 46, col 5
        if _v is not None: write(_filter(_v, rawExpr=u'$title')) # from line 46, col 5.
        write(u'''</h1>
<h2>''')
        _v = VFFSL(SL,"page",True) # u'$page' on line 47, col 5
        if _v is not None: write(_filter(_v, rawExpr=u'$page')) # from line 47, col 5.
        write(u'''</h2>
<div id="navigation">
\t<a href="../TranslateStrings?view=all">Translate strings</a> | 
''')
        if VFFSL(SL,"translate_accelerators",True) == True: # generated from line 50, col 2
            write(u'''\t<a href="../ChooseAccelerators?view=all">Assign keyboard shortcuts</a> | 
''')
        if VFFSL(SL,"translate_mnemonics",True) == True: # generated from line 53, col 2
            write(u'''\t<a href="../ChooseMnemonics?view=all">Choose mnemonics</a> | 
''')
        write(u'''\t<a href="../MainMenu">Back to tasks menu</a>
\t
</div>

<div class="description">
\t<p>''')
        _v = VFFSL(SL,"about",True) # u'$about' on line 61, col 5
        if _v is not None: write(_filter(_v, rawExpr=u'$about')) # from line 61, col 5.
        write(u'''</p>
\t<p>Showing ''')
        _v = VFFSL(SL,"view_description",True) # u'$view_description' on line 62, col 13
        if _v is not None: write(_filter(_v, rawExpr=u'$view_description')) # from line 62, col 13.
        write(u''' (''')
        _v = VFFSL(SL,"count",True) # u'$count' on line 62, col 32
        if _v is not None: write(_filter(_v, rawExpr=u'$count')) # from line 62, col 32.
        write(u''' items).  
''')
        if VFFSL(SL,"usepages",True) == True: # generated from line 63, col 2
            p = VFFSL(SL,"pagenum",True) + 1
            write(u'''\t\tPage ''')
            _v = VFFSL(SL,"p",True) # u'$p' on line 65, col 8
            if _v is not None: write(_filter(_v, rawExpr=u'$p')) # from line 65, col 8.
            write(u''' of ''')
            _v = VFFSL(SL,"total_num_pages",True) # u'$total_num_pages' on line 65, col 14
            if _v is not None: write(_filter(_v, rawExpr=u'$total_num_pages')) # from line 65, col 14.
            write(u'''
''')
        write(u'''\t</p>
</div>
<div>
\t<form action="change_view" method="POST">
\t    <select name="viewfilter">
\t        <option ''')
        _v = VFFSL(SL,"all_selected",True) # u'$all_selected' on line 72, col 18
        if _v is not None: write(_filter(_v, rawExpr=u'$all_selected')) # from line 72, col 18.
        write(u''' value="all">all items</option>
\t        <option ''')
        _v = VFFSL(SL,"newtodo_selected",True) # u'$newtodo_selected' on line 73, col 18
        if _v is not None: write(_filter(_v, rawExpr=u'$newtodo_selected')) # from line 73, col 18.
        write(u''' value="newtodo">all items marked new or to-do</option>
\t        <option ''')
        _v = VFFSL(SL,"new_selected",True) # u'$new_selected' on line 74, col 18
        if _v is not None: write(_filter(_v, rawExpr=u'$new_selected')) # from line 74, col 18.
        write(u''' value="new">all new items</option>
\t        <option ''')
        _v = VFFSL(SL,"todo_selected",True) # u'$todo_selected' on line 75, col 18
        if _v is not None: write(_filter(_v, rawExpr=u'$todo_selected')) # from line 75, col 18.
        write(u''' value="todo">all to-do items</option>
\t\t\t<option ''')
        _v = VFFSL(SL,"allok_selected",True) # u'$allok_selected' on line 76, col 12
        if _v is not None: write(_filter(_v, rawExpr=u'$allok_selected')) # from line 76, col 12.
        write(u''' value="allok">all done items</option>
\t    </select>
\t    <input type="submit" value="Change view" />
\t</form>
</div>
<br/>

''')
        #  "warnings" variable contains preformatted HTML
        if VFFSL(SL,"warnings",True) != None and VFFSL(SL,"warnings",True) != "": # generated from line 84, col 1
            write(u'''\t''')
            _v = VFFSL(SL,"warnings",True) # u'$warnings' on line 85, col 2
            if _v is not None: write(_filter(_v, rawExpr=u'$warnings')) # from line 85, col 2.
            write(u'''
''')
        #  the big table
        write(u'''<div>''')
        _v = VFFSL(SL,"form",True) # u'$form' on line 88, col 6
        if _v is not None: write(_filter(_v, rawExpr=u'$form')) # from line 88, col 6.
        write(u'''</div>

''')
        #  the page numbers at the bottom
        write(u'''
''')
        if VFFSL(SL,"usepages",True) == True and VFFSL(SL,"total_num_pages",True) > 1: # generated from line 92, col 1
            write(u'''<div class="page_nav">
''')
            if VFFSL(SL,"pagenum",True) != 0: # generated from line 94, col 2
                write(u'''\t\t<span><a href="previous_page">&lt;&lt;</a></span>
''')
            for i in range(0, VFFSL(SL,"total_num_pages",True)): # generated from line 97, col 2
                display_pagenum = VFFSL(SL,"i",True) + 1
                if VFFSL(SL,"pagenum",True) != VFFSL(SL,"i",True): # generated from line 99, col 3
                    write(u'''\t\t\t<span><a href="change_page?pagenum=''')
                    _v = VFFSL(SL,"i",True) # u'$i' on line 100, col 39
                    if _v is not None: write(_filter(_v, rawExpr=u'$i')) # from line 100, col 39.
                    write(u'''">''')
                    _v = VFFSL(SL,"display_pagenum",True) # u'$display_pagenum' on line 100, col 43
                    if _v is not None: write(_filter(_v, rawExpr=u'$display_pagenum')) # from line 100, col 43.
                    write(u'''</a></span>
''')
                else: # generated from line 101, col 3
                    write(u'''\t\t\t<span>''')
                    _v = VFFSL(SL,"display_pagenum",True) # u'$display_pagenum' on line 102, col 10
                    if _v is not None: write(_filter(_v, rawExpr=u'$display_pagenum')) # from line 102, col 10.
                    write(u'''</span>
''')
            if VFFSL(SL,"pagenum",True) != VFFSL(SL,"total_num_pages",True) - 1: # generated from line 105, col 2
                write(u'''\t\t<span><a href="next_page">&gt;&gt;</a></span>
''')
            write(u'''</div>
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def writeBody(self, **KWS):



        ## CHEETAH: main method generated for this template
        trans = KWS.get("trans")
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        # 
        # Template variables:
        # 
        # 	actions = navigation links
        # 	about = about this page
        # 	view_description = about this page view
        # 	count = number of items being displayed
        # 	form = table rows, each containing a translation form
        # 	usepages = if True, this represents a page
        # 	total_num_pages = the total number of pages
        # 	pagenum = the current page number
        # 	all_warnings = html-formatted list of warnings about the page
        write(u'''
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        
    ##################################################
    ## CHEETAH GENERATED ATTRIBUTES


    _CHEETAH__instanceInitialized = False

    _CHEETAH_version = __CHEETAH_version__

    _CHEETAH_versionTuple = __CHEETAH_versionTuple__

    _CHEETAH_genTime = __CHEETAH_genTime__

    _CHEETAH_genTimestamp = __CHEETAH_genTimestamp__

    _CHEETAH_src = __CHEETAH_src__

    _CHEETAH_srcLastModified = __CHEETAH_srcLastModified__

    _mainCheetahMethod_for_translate= 'writeBody'

## END CLASS DEFINITION

if not hasattr(translate, '_initCheetahAttributes'):
    templateAPIClass = getattr(translate, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(translate)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=translate()).run()

