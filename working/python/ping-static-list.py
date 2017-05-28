#!/usr/bin/python

import os

hosts = ['192.168.1.1', '8.8.8.8']


for name in hosts:
    response = os.system("ping -c 1 -w 2 " + name + " > /dev/null 2>&1")
    if response == 0:
        print (name + ' is up!')
    else:
        print(name + ' is down!')
