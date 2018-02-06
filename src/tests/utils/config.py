import ConfigParser, os

def get_property(section,property):
    dir = os.path.dirname(os.path.abspath(__file__))
    file = 'test.properties'
    configPath = dir + '/' + file
    config = ConfigParser.RawConfigParser()
    config.read(configPath)
    return config.get(section,property)

