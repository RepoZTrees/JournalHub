import commonmark
import glob
import json
import os
import jinja2
import os.path

l = getLogger('journalhub')

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
    md_files = glob.glob(path+"/blog_posts/*.md")
    articles = {}
    for i in md_files:
        with open(i,'r') as f:
            l.debug("Generating ....")
            data = f.read()
        file_name = os.path.basename(i)
        file_name = file_name.split('.')[0]
        info,md_content = split_md(data)  
        python_object = convert_md_to_python(info)
        line1,line2,line3 = parse_info(python_object)
        html_content = convert_content_to_html(md_content)
        article_data = {'title': line1,
             'author': line2,
             'date': line3,
            'content':html_content}
        articles[file_name] = article_data
    return articles

def create_post(dict,path,option):
    if "post_html" not in os.listdir(path):
        post_html_path= os.path.join(path,"post_html")
        os.mkdir(post_html_path)
    templateLoader = jinja2.FileSystemLoader(searchpath="./templates/")
    templateEnv = jinja2.Environment(loader=templateLoader)
    post_template = templateEnv.get_template("post_template.html")
    if option:
        post_details = []
        dir_name = os.path.basename(path)
        for key,value in dict.items():
            post_details.append(value)
        data = {
            'head' : "JournalHub",
            'post_details' : post_details
            }
        str = post_template.render(post=data)
        post_path = os.path.join(path,"post_html",dir_name)
        post_path += ".html"
        f= open(post_path,"w")
        f.write(str)
    else:
        for key,value in dict.items():
            data= {
                'head' : "JournalHub",
                'post_details' : [value]
                }
            str = post_template.render(post=data)
            post_path = os.path.join(path,"post_html",key)
            post_path += ".html"
            f = open(post_path,"w")
            f.write(str)

def create_index(dict,path,option):
    templateLoader = jinja2.FileSystemLoader(searchpath="./templates/")
    templateEnv = jinja2.Environment(loader=templateLoader)
    index_template = templateEnv.get_template("index_template.html")
    blog_names = []
    for i in dict:
        dir_name = os.path.basename(path)
        break
    for key,values in dict.items():
        blog_names.append(key)
    if option:
        data = {
            'head' : "JournalHub",
            'blog_names' : [dir_name]
            }
    else:
        data = {
            'head' : "JournalHub",
            'blog_names': blog_names
        }
    str = index_template.render(post=data)
    index_path = os.path.join(path,"index.html")
    f = open(index_path,"w")
    f.write(str)
    
def md_to_html(path,option):
    dict = get_parsed_md(path)
    create_index(dict,path,option)
    create_post(dict,path,option)
