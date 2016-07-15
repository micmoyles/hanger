# -*- coding: utf-8 -*-

DESCRIPTION = """
    Script file amqpcon
    Author: Alexey Kolyanov, 2016
"""

import os
import sys
sys.path.append('/home/mmoyles/stomp.py-4.1.8')
import yaml
import time
import stomp

CUR_DIR = os.path.dirname(os.path.abspath(__file__))


def get_config(cfgpath):
    config = {}
    if not os.path.exists(cfgpath):
        if not os.path.exists(os.path.join(CUR_DIR, cfgpath)):
            raise ValueError("Config file %s is not found!" % cfgpath)
        cfgpath = os.path.join(CUR_DIR, cfgpath)
    with open(cfgpath, 'r') as cfgf:
        config = yaml.load(cfgf.read())
    return config


class MyListener(stomp.ConnectionListener):

    def on_error(self, headers, message):
        print('   !!!!!! Received an error \n%s' % message)

    def on_message(self, headers, message):
        print('   ****** Received a message \n%s'+ datetime.datetime.now()+ ' ' % message)


def main():
    config = get_config('settings.yaml')

    conn = stomp.Connection(host_and_ports=[(config['connection']['host'], config['connection']['port'])],
                            use_ssl=config['connection']['ssl'])
    conn.set_listener('', MyListener())
    conn.start()
    conn_headers = {
        'host': config['connection']['vhost'],
        'client-id': config['connection']['client_id'],
    }
    conn.connect(username=config['connection']['login'],
                 passcode=config['connection']['passcode'],
                 headers=conn_headers,
                 wait=True)

    print("connected")

    conn.subscribe(destination=config['subscription']['topic'],
                   id=config['subscription']['subscriptionid'],
                   ack=config['subscription']['ack'])
    print("subscribed")

    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        pass

    conn.disconnect()

    return 0


if __name__ == "__main__":
    retval = main()
    sys.exit(retval)
