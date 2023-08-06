#!/bin/python3
import os
import json


class Pswd:
    def dump():
        ptys = os.path.dirname(__file__)
        js = f'{ptys}/wilog.json'
        wfprof = set(sorted(os.popen('nmcli -s -t connection show | grep wireless | grep -o -P "^.+?(?=:)"').read().split("\n")[:-1]))
        if len(wfprof) > 0:
            wfdata = {l: p for l, p in zip(list(os.popen(f'nmcli -s  -t -g "802-11-wireless.ssid"  connection show "{i}" | cut -d"\n" -f1').read().replace('\n', '') for i in wfprof if os.popen(f'nmcli -s  -t -g "802-11-wireless-security.key-mgmt"  connection show "{i}" | cut -d"\n" -f1').read().replace('\n', '') == "wpa-psk"), list(os.popen(f'nmcli -s  -t -g "802-11-wireless-security.psk"  connection show "{i}" | cut -d"\n" -f1').read().replace('\n', '') for i in wfprof if os.popen(f'nmcli -s  -t -g "802-11-wireless-security.key-mgmt"  connection show "{i}" | cut -d"\n" -f1').read().replace('\n', '') == "wpa-psk"))}
            if os.path.exists(js) == False:
                open(js, 'a').close()
            # up/down load to json file
            f = open(js, 'r+', encoding='utf-8')
            try:
                jik = json.loads(f.read())
            except json.decoder.JSONDecodeError:
                jik = {}
            if len(jik) > 0:
                deb = jik.copy()
                deb.update(wfdata)
                f.seek(0)
                json.dump(deb, f, indent=4, ensure_ascii=False)
                f.close()
            elif len(jik) == 0:
                json.dump(wfdata, f, indent=4, ensure_ascii=False)
                f.close()
        elif len(wfprof) == 0:
            print('NoSavedWirelessNetworks \nSorry no saved networks.\nThis script do stoped.')
            exit(0)


if __name__ == '__main__':
    Pswd.dump()  # run
