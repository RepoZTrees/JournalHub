from configparser import ConfigParser

parser = ConfigParser()
parser.read('config_details.ini')
print(parser.sections())

print(parser.get("Landing Page", "title"))
print(parser.get("Landing Page", "description"))
print(parser.get("Landing Page", "subtitle"))
    

