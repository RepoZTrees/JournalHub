import shutil
import os
import os.path
from . import parser
import argparse
import logging
import glob
import socketserver
import http.server

def get_logger(verbose=False):
    l = logging.getLogger('journalhub')
    sh = logging.StreamHandler() 
    l.addHandler(sh)
    fmt = logging.Formatter('%(asctime)s | %(filename)s:%(lineno)d | %(message)s')
    sh.setFormatter(fmt)
    if verbose:
        sh.setLevel(logging.DEBUG)
    else:
        sh.setLevel(logging.INFO)
    l.setLevel(logging.DEBUG)
    return l

def arg_parse():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('function',help='$ journal init  -->  Initialzes blog templates. $ journal generate  -->  Generates html files', choices = ["init","generate","serve"])
    arg_parser.add_argument('-v','--verbose', help = "Show verbose debugging output")
    arg_parser.add_argument('-s','--single',
                            default = False,
                            action = 'store_true',
                            help = 'Posts generated in single page. %(default)s by default')
    args = arg_parser.parse_args()
    return args.function,args.single

def create_fresh_blog(at):
    """
    Creates a fresh blog setup at location `at`
    """
    # Move stuff from main here so that it's testable

def main():

    command,option = arg_parse()
    l = get_logger()
    # if '-v' in command:
    #     l = get_logger(True)
    # else:
    #     l = get_logger(False)

    this_dir, _ = os.path.split(__file__)
    # create_fresh_blog(os.getcwd())
    
    # opj = os.path.join

    # from_ = opj(this_dir, 'assets')
    # to = os.getcwd()

    source_path = os.path.join(this_dir,'assets','config.ini')
    destination_path = os.path.join(os.getcwd(),'config.ini')
    
    source_path1 = os.path.join(this_dir,'assets','templates')
    destination_path1 = os.path.join(os.getcwd(),'templates')

    source_path2 = os.path.join(this_dir,'assets','blog_posts')
    destination_path2 = os.path.join(os.getcwd(),'blog_posts')
    
    if command == 'init':
        # for src, dest in [('config.ini', 'config.ini'),
        #                   ('templates', 'templates')]:
        #     shutil.copyfile(src, dest)

        shutil.copyfile(source_path, destination_path)
        shutil.copytree(source_path1, destination_path1)
        shutil.copytree(source_path2, destination_path2)
        l.info("Initializes the blog")
    elif command == 'generate':
        path = os.getcwd()

        if "post_html" not in os.listdir(path):
            post_html_path= os.path.join(path,"post_html")
            os.mkdir(post_html_path)
        else:
            filelist = glob.glob(path+"/post_html/*.html")
            for f in filelist:
                os.remove(f)
                
        parser.md_to_html(path,option)
        l.info("Generated html files")

    elif command == 'serve':
        
        PORT = 8000
   
        web_dir = os.path.join(os.getcwd(), 'post_html')
        os.chdir(web_dir)

        Handler = http.server.SimpleHTTPRequestHandler
        httpd = socketserver.TCPServer(("", PORT), Handler)
        print("serving at port", PORT,"http://0.0.0.0:8000/")
        httpd.serve_forever()

