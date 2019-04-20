#!/usr/bin/python
from gevent import monkey
monkey.patch_all()
import gevent
import json
import sys

from shadowsocks.local import main as local_main


def start_local(config):
    sys.argv = ('sslocal -c {} start'.format(config)).split()
    print(sys.argv)
    sys.exit(local_main())


def run():
    with open('./config.json', 'r') as rf:
        client_datas = json.load(rf)

    for index, client_data in enumerate(client_datas):
        file_name = '/tmp/config{}.json'.format(index)
        print(file_name)
        with open(file_name, 'w') as wf:
            json.dump(client_data, wf)
        yield file_name


if __name__ == '__main__':
    for file_name in run():
        task = gevent.spawn(start_local, file_name)
    task.join()


