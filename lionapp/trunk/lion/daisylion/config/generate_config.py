# run this to generate the 3 configuration file options for the lion
from optparse import OptionParser
import time

COMMENT = """# daisylion configuration file
# generated by generate_config.py with the option %s
# %s
"""

STATIC_MAIN_SECTION = """
[main]
masterlang=eng-US
trace=false
show_audio_upload=false
dbname=lionutf8
webport=8080
audio_dir_prefix=./audio/
target_app=amis
"""

DYNAMIC_MAIN_SECTION = {
"local": """# site and db are local
dbhost=localhost
webhost=localhost
temp_audio_dir=/tmp/daisylionaudio
temp_audio_uri=file:///tmp/daisylionaudio
""",

"web": """# site and db are on gandi (92.243.13.151)
dbhost=92.243.13.151
webhost=92.243.13.151
temp_audio_dir=/srv/d_daisylion/www/www.example.net/htdocs/daisylionaudio
temp_audio_uri=http://92.243.13.151/daisylionaudio
""",

"combo":"""# site is local and db is on gandi (92.243.13.151).  requires that your IP is authorized on the remote mysql server.
dbhost=92.243.13.151
webhost=localhost
temp_audio_dir=/tmp/daisylionaudio
temp_audio_uri=file:///tmp/daisylionaudio
"""   
}

STATIC_MODULE_SECTION="""
# each module has its own section
[amis]
lioniomodule=lionio_amis
lionioclass=AmisLionIO

"""

def assemble_file(option):
    return (COMMENT % (option, time.asctime())) + STATIC_MAIN_SECTION + DYNAMIC_MAIN_SECTION[option] + STATIC_MODULE_SECTION

def main():
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option("-t", "--type", dest="output_type",
                    help="Configuration to generate [local | web | combo]")
    (options, args) = parser.parse_args()
    
    # default to combo
    if options.output_type == None:
        options.output_type = "combo"

    config = assemble_file(options.output_type)
    print config

if __name__ == "__main__": main()
