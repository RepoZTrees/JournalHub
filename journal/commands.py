from sys import argv
import sys
import shutil
import os
import os.path
import parser

def main():
    this_dir,this_filename = os.path.split(__file__)
    source_path = os.path.join(this_dir,'assets','config.ini')
    destination_path = os.path.join(os.getcwd(),'config.ini')
    
    source_path1 = os.path.join(this_dir,'assets','templates')
    destination_path1 = os.path.join(os.getcwd(),'templates')

    if sys.argv[1] == 'init':
        dest = shutil.copyfile(source_path, destination_path)
        d = shutil.copytree(source_path1, destination_path1)
    elif sys.argv[1] == 'generate':
        path = os.getcwd()
        parser.md_to_html(path)
    else:
        print('wrong command')
