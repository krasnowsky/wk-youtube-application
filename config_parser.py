import configparser

config = configparser.ConfigParser()
config.read('settings.conf')

api_key = config['api']['api_key']
