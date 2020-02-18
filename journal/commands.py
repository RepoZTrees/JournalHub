from sys import argv
import sys
import shutil
import os
import os.path
from . import parser
import argparse


def arg_parse():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('function',help='$ journal init  -->  Initialzes blog templates. $ journal generate  -->  Generates html files', choices = ["init","generate"])
    arg_parser.add_argument('-s','--single',
                            default = False,
                            action = 'store_true',
                            help = 'Posts generated in single page. %(default)s by default')
    args = arg_parser.parse_args()
    return args.function,args.single

def main():
    command,option = arg_parse()

    this_dir,this_filename = os.path.split(__file__)
    source_path = os.path.join(this_dir,'assets','config.ini')
    destination_path = os.path.join(os.getcwd(),'config.ini')
    
    source_path1 = os.path.join(this_dir,'assets','templates')
    destination_path1 = os.path.join(os.getcwd(),'templates')
    
    if command == 'init':
        dest = shutil.copyfile(source_path, destination_path)
        d = shutil.copytree(source_path1, destination_path1)
    elif command == 'generate':
        path = os.getcwd()
        parser.md_to_html(path,option)
    
