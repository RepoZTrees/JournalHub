import commonmark
import glob
import json
import os
from jinja2 import Environment, PackageLoader
import os.path

env = None

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
    md_files = glob.glob(path+"/*.md")
    articles = {}
    for i in md_files:
        with open(i,'r') as f:
            data = f.read()
        info,md_content = split_md(data)  
        python_object = convert_md_to_python(info)
        line1,line2,line3 = parse_info(python_object)
        html_content = convert_content_to_html(md_content)
        article_data = {'title': line1,
             'author': line2,
             'date': line3,
            'content':html_content}
        articles[i] = article_data
    return articles

def create_post(dict,path):
    if "post_html" not in os.listdir(path):
        post_html_path= os.path.join(path,"post_html")
        os.mkdir(post_html_path)
    post_template = env.get_template('post.html')
    str = post_template.render(post=dict)
    title = dict['title']
    post_path = os.path.join(path,"post_html",title)
    post_path+=".html"
    f = open(post_path,"w")
    f.write(str)
    
def create_index(dict,path):
    index_template = env.get_template('index.html')
    
    blog_names=[]
    for i in dict:
        dir_name = os.path.basename
        break
    for key,values in dict.items():
        blog_names.append(values['title'])
    data = {
        'head' : dir_name,
        'blog_names': blog_names
    }
    str = index_template.render(post=data)
    index_path = os.path.join(path,"index.html")
    f = open(index_path,"w")
    f.write(str)

def generate_html(dict,path):
    create_index(dict,path)
    for key,values in dict.items():
        create_post(values,path)

def md_to_html(path):
    global env
    env = Environment(loader=PackageLoader('parser','/tmp/journal/templates'))
    dict = get_parsed_md(path)
    generate_html(dict,path)
    
if __name__=='__main__':
    main()
    
