from configparser import ConfigParser

def get_config_data(path):
    parser = ConfigParser()
    parser.read(path)
    parser.sections()
    data = {'title':parser.get("Landing Page", "title"),
            'description':parser.get("Landing Page", "description"),
            'order_by_date':parser.get("Landing Page", "order_by_date")}
    return data

