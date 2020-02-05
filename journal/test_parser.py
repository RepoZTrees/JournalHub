import parser

def list_md():
    return """
    title:Letter Invaders
    author:Shireen
    date:05/02/2020
    ---
    # Heading
    * a
    * b
    * b.a
    """

def test_md_file_info():
    assert parser.md_file_info(list_md) == {'title':'Letter Invaders','author':'Shireen','date':'05/02/2020'}
