import parser

def test_split_md():

    blog_data = """title : GitHub Project Recommendation Tool
author : Vik
date : 02-07-2020
---

## GitHub API documentation:

My first task was to read the GitHub documentation and understand what is an API and how to it works.

**So what is an API? What is a REST API?**

API stands for Application Programming Interface. An API is a set of routines, protocols, and tools for building software application. Simply put it's a messenger that takes the requests  and tells a system what you want to do and then return the response back to you. In a very layman term messenger is a waiter in a restaurant. He is a critical link between you and chef in the kitchen of the restaurant. Waiters job is to communicate your order to the kitchen and deliver your food back to your table. Just like a restaurant, GitHub has a menu. For e.g. you choose programming language, click on trending projects, etc. In order to get the data you want, you interact with GitHub's website to access GitHub's database to see which user committed repositories recently, and/or which projects are trending etc. But what if you don't want to search all these information manually but write a command and let your software do the search based on variables you enter. In that case your software interacts with *GitHub's API*. API is like that helpful waiter can be asked by your software program to get certain information from GitHub's database over the internet and deliver right back to your software program which then shows it you."""
    
    info,content = parser.split_md(blog_data)
    
    assert info == 'title : GitHub Project Recommendation Tool\nauthor : Vik\ndate : 02-07-2020\n'

    assert content ==  "\n\n## GitHub API documentation:\n\nMy first task was to read the GitHub documentation and understand what is an API and how to it works.\n\n**So what is an API? What is a REST API?**\n\nAPI stands for Application Programming Interface. An API is a set of routines, protocols, and tools for building software application. Simply put it's a messenger that takes the requests  and tells a system what you want to do and then return the response back to you. In a very layman term messenger is a waiter in a restaurant. He is a critical link between you and chef in the kitchen of the restaurant. Waiters job is to communicate your order to the kitchen and deliver your food back to your table. Just like a restaurant, GitHub has a menu. For e.g. you choose programming language, click on trending projects, etc. In order to get the data you want, you interact with GitHub's website to access GitHub's database to see which user committed repositories recently, and/or which projects are trending etc. But what if you don't want to search all these information manually but write a command and let your software do the search based on variables you enter. In that case your software interacts with *GitHub's API*. API is like that helpful waiter can be asked by your software program to get certain information from GitHub's database over the internet and deliver right back to your software program which then shows it you."

#----------

def test_convert_md_to_python():
    actual_value = 'title : GitHub Project Recommendation Tool\nauthor : Vik\ndate : 02-07-2020\n'
    expected_value = [{'children': [{'children': [], 'type': 'paragraph'}, {'literal': 'title : GitHub Project Recommendation Tool', 'type': 'text'}, {'type': 'softbreak'}, {'literal': 'author : Vik', 'type': 'text'}, {'type': 'softbreak'}, {'literal': 'date : 02-07-2020', 'type': 'text'}], 'type': 'document'}, {'children': [], 'type': 'paragraph'}, {'children': [], 'type': 'document'}]

    assert parser.convert_md_to_python(actual_value) == expected_value
    
#--------

def test_parse_info():
    actual_value = [{'children': [{'children': [], 'type': 'paragraph'}, {'literal': 'title : GitHub Project Recommendation Tool', 'type': 'text'}, {'type': 'softbreak'}, {'literal': 'author : Vik', 'type': 'text'}, {'type': 'softbreak'}, {'literal': 'date : 02-07-2020', 'type': 'text'}], 'type': 'document'}, {'children': [], 'type': 'paragraph'}, {'children': [], 'type': 'document'}]

    title,author,date = parser.parse_info(actual_value)
    
    assert title == 'GitHub Project Recommendation Tool'
    assert author == 'Vik'
    assert date == '02-07-2020'

#--------

def test_convert_content_to_html():

    actual_value =  "\n\n## GitHub API documentation:\n\nMy first task was to read the GitHub documentation and understand what is an API and how to it works.\n\n**So what is an API? What is a REST API?**\n"
    expected_value = """<h2>GitHub API documentation:</h2>
<p>My first task was to read the GitHub documentation and understand what is an API and how to it works.</p>
<p><strong>So what is an API? What is a REST API?</strong></p>
"""
    
    assert parser.convert_content_to_html(actual_value) == expected_value

#--------
