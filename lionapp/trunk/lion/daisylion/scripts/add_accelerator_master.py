from global_options_parser import *
from daisylion.db.liondb import LionDB

def main():
    usage = """usage: %prog [options] string stringid refid keys
    Edits the master language and updates all other languages.
    
    string: the human-readable name for the accelerator shortcut
    refid: the id of the string label for the command referenced by the accelerator
    keys: the actual keys used to access the accelerator shortcut
    
    e.g. 
    %prog Escape t123 t345 esc
    
    """
    parser = GlobalOptionsParser(usage=usage)
    (options, args) = parser.parse_args()
    parser.check_args(4, args)
    
    session = LionDB(options.config, options.trace, options.app)    
    string, stringid, refid, keys = args
    session.add_accelerator_master(string, stringid, refid, keys)

if __name__=="__main__": main()


