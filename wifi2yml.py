#!/bin/python3
import os
import yaml


class Pswd:
    def dump():
        ptys = os.path.dirname(__file__)
        yml = f'{ptys}/wilog.yaml'
        wfprof = set(sorted(os.popen('nmcli -s -t connection show | grep wireless | grep -o -P "^.+?(?=:)"').read().split("\n")[:-1]))
        if len(wfprof) > 0:
            wfdata = {l: p for l, p in zip(list(os.popen(f'nmcli -s  -t -g "802-11-wireless.ssid"  connection show "{i}" | cut -d"\n" -f1').read().replace('\n', '') for i in wfprof if os.popen(f'nmcli -s  -t -g "802-11-wireless-security.key-mgmt"  connection show "{i}" | cut -d"\n" -f1').read().replace('\n', '') == "wpa-psk"), list(os.popen(f'nmcli -s  -t -g "802-11-wireless-security.psk"  connection show "{i}" | cut -d"\n" -f1').read().replace('\n', '') for i in wfprof if os.popen(f'nmcli -s  -t -g "802-11-wireless-security.key-mgmt"  connection show "{i}" | cut -d"\n" -f1').read().replace('\n', '') == "wpa-psk"))}
            if os.path.exists(yml) == False:
                open(yml, 'a').close()
            # up/down load to yaml file
            f = open(yml, 'r+', encoding='utf-8')
            jik = yaml.load(f, yaml.FullLoader)
            if jik != None:
                deb = jik
                deb.update(wfdata)
                f.seek(0)
                yaml.dump(deb, f)
                f.close()
            elif jik == None:
                yaml.dump(wfdata, f)
                f.close()
        elif len(wfprof) == 0:
            print('NoSavedWirelessNetworks \nSorry no saved networks.\nThis script do stoped.')
            exit(0)


if __name__ == '__main__':
    Pswd.dump()  # run
