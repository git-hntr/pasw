#!/bin/python3
import os
import yaml


class Pswd:
    def load():
        ptys = os.path.dirname(__file__)
        js = f'{ptys}/wilog.json'
        yml = f'{ptys}/wilog.yaml'
        if os.path.exists(js) == False and os.path.exists(yml) == False:
            print('NoFileExist error \nPlease use wifi2json.py or wifi2yml.py script.')
            exit(0)
        if os.path.exists(js) and os.path.exists(yml):
            if os.stat(js).st_size > os.stat(yml).st_size :
                f = open(js, 'r', encoding='utf-8')
            elif os.stat(js).st_size < os.stat(yml).st_size :
                f = open(yml, 'r', encoding='utf-8')
        else:
            if os.path.exists(js):
                f = open(js, 'r', encoding='utf-8')
            if os.path.exists(yml):
                f = open(yml, 'r', encoding='utf-8')
        jik = yaml.load(f, yaml.FullLoader)
        f.close()
        for x, y in jik.items():
            if len(y) >= 8: os.popen(f'nmcli connection add type wifi con-name "{x}" ssid "{x}" wifi-sec.key-mgmt wpa-psk wifi-sec.psk "{y}"')
        print("Succ")


if __name__ == '__main__':
    Pswd.load()
