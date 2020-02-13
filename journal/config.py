from configparser import ConfigParser

parser = ConfigParser()
parser.read('assets/config.ini')


print(parser.sections())
print(parser.get("Landing Page", "title"))
print(parser.get("Landing Page", "description"))

    

