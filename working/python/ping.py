#!/usr/bin/python3
__author__ = 'bruce'
import os

with open("hosts.txt") as f:
    a = [a.strip('\n') for a in f.readlines()]
    for hostip in a:
        response = os.system("ping -c 1 -w 2 " + hostip + " > /dev/null 2>&1")
        if response == 0:
            print(hostip, 'is up!')
        else:
            print(hostip, 'is down!')
