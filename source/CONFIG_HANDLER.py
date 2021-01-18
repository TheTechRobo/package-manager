import configparser
def write(base_path, section, item, text):
    config = configparser.ConfigParser()
    config.read('%s/config.ini' % base_path)
    config[section][item] = text
    return
def read(base_path, section, item):
    config = configparser.ConfigParser()
    config.read('%s/config.ini' % base_path)
    return config[section][item]

