import commonmark
import glob
import json

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
