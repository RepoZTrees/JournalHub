import commonmark
import glob
import json
import os
import jinja2
import os.path
from . import config
import datetime

#l = getLogger('journalhub')

def split_md(data):
    "It seperates header and the content of an article"
    md_data = data.split('---')
    return md_data[0],md_data[1]

def convert_md_to_python(info):
    "Converts markdown data to Python object"
    parser = commonmark.Parser()
    parse_data = parser.parse(info)
    json_format = commonmark.dumpJSON(parse_data)
    py_object = json.loads(json_format)
    return py_object 
   
def parse_info(d):
    "Extracts title, author, and date"
    split_title = d[0]['children'][1]['literal'].split(':')
    split_author = d[0]['children'][3]['literal'].split(':')
    split_date = d[0]['children'][5]['literal'].split(':')
    title = split_title[1].strip()
    author = split_author[1].strip()
    date = split_date[1].strip()
    return title,author,date

def convert_content_to_html(md_content):
    "It renders content of the article and converts into html format"
    renderer = commonmark.HtmlRenderer()
    parser = commonmark.Parser()
    syntax_tree = parser.parse(md_content)
    html = renderer.render(syntax_tree)
    return html

def get_parsed_md(path):
    md_path = os.path.join(path,"blog_posts","*.md")
    md_files = glob.glob(md_path)
    articles = []
    for i in md_files:
        with open(i,'r') as f:
            #l.debug("Generating ....")
            data = f.read()
        file_name = os.path.basename(i)
        file_name = file_name.split('.')[0]
        info,md_content = split_md(data)  
        python_object = convert_md_to_python(info)
        line1,line2,line3 = parse_info(python_object)
        date_str = line3
        date = datetime.datetime.strptime(date_str, '%d-%m-%Y').date()
        html_content = convert_content_to_html(md_content)
        article_data = {
            'file_name': file_name,
            'title': line1,
             'author': line2,
             'date': date,
            'content':html_content}
        articles.append(article_data)
    return articles

def create_index(parsed_data,config_data,path,option):
    search_path = os.path.join(path,"templates")
    templateLoader = jinja2.FileSystemLoader(searchpath=search_path)
    templateEnv = jinja2.Environment(loader=templateLoader)
    
    index_template = templateEnv.get_template("index_template.html")

    str_index = index_template.render(post=parsed_data,config_data=config_data,option=option)

    return str_index
    
    

def create_post(parsed_data,config_data,path):
    search_path = os.path.join(path,"templates")
    templateLoader = jinja2.FileSystemLoader(searchpath=search_path)
    templateEnv = jinja2.Environment(loader=templateLoader)
    
    post_template = templateEnv.get_template("post_template.html")
    
    for i in parsed_data:
        str_post = post_template.render(post=i,config_data=config_data)
        post_path = os.path.join(path,"post_html",i['file_name'])
        post_path += ".html"
        f= open(post_path,"w")
        f.write(str_post)
        
    
def md_to_html(path,option):
    parsed_data = get_parsed_md(path)
    config_data = config.get_config_data(os.path.join(path,"config.ini"))
    
    if option:
        str_index = create_index(parsed_data,config_data,path,option)
        index_path = os.path.join(path,"post_html","single_index.html")
        f = open(index_path,"w")
        f.write(str_index)
    else:
        str_index = create_index(parsed_data,config_data,path,option)
        index_path = os.path.join(path,"post_html","index.html")
        f = open(index_path,"w")
        f.write(str_index)
        create_post(parsed_data,config_data,path)
        
