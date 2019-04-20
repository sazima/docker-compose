#!/usr/bin/python
# import shadowsocks

import os
import json
import time
import threading
import traceback


def remove_file(*files):
    time.sleep(5)
    for file in files:
        os.remove(file)


def run():
    with open('./config.json', 'r') as rf:
        client_datas = json.load(rf)
    command = ''  # run sslocal
    file_names = []  # temp json_file
    for index, client_data in enumerate(client_datas):
        file_name = '/tmp/config{}.json'.format(index)
        with open(file_name, 'w') as wf:
            json.dump(client_data, wf)
        command += "sslocal -c {} restart & ".format(file_name)
        file_names.append(file_name)
    remove = threading.Thread(target=remove_file, args=file_names)
    remove.start()
    os.popen(command.strip('&'))
    return command.strip('&')


if __name__ == '__main__':
    while True:
        command = run()
        time.sleep(3600 * 24)  # restart one day

