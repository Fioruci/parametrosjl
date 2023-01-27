# v1.0.23.1h
import yaml, os, configparser, time
from yaml.loader import SafeLoader

def setupKey(empresa):
    startz2 = "C:\\" + empresa

    for dirpath, dirnames, filenames in os.walk(startz2):
        for dirname in dirnames:
            if dirname == "Acesso":
                config = configparser.ConfigParser()
                config.read('C:\\' + empresa + '\\Acesso\\parametro.ini')
                keyy = config['ACESSOSISTEMA']['KEY']
                # print(keyy)

                dict_key = {'KEY': keyy}

                
    with open('build\\assets\\key.yaml', 'w') as key:
        yaml.dump(dict_key, key)
        
    with open('build\\assets\\key.yaml', 'r') as key:
        data2 = yaml.load(key, Loader=SafeLoader)
        return data2['KEY']