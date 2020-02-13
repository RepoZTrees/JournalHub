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
    args = arg_parser.parse_args()
    return args.function

def main():
    argument = arg_parse()

    this_dir,this_filename = os.path.split(__file__)
    source_path = os.path.join(this_dir,'assets','config.ini')
    destination_path = os.path.join(os.getcwd(),'config.ini')
    
    source_path1 = os.path.join(this_dir,'assets','templates')
    destination_path1 = os.path.join(os.getcwd(),'templates')

    if argument == 'init':
        dest = shutil.copyfile(source_path, destination_path)
        d = shutil.copytree(source_path1, destination_path1)
        print("Blog templates created")
    elif argument == 'generate':
        path = os.getcwd()
        parser.md_to_html(path)
    
