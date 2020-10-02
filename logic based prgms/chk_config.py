from configparser import ConfigParser
config = ConfigParser()
config.read('chk.ini')

c = config.get('Preferences','min_small_l')

conv = int(c)

if conv == 1:
    print('p')