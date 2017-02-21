#!/usr/bin/python
import os
import socket

hosts = ['8.8.8.8', '8.8.4.4', '208.67.222.222', '208.67.220.220']

print('\n' + 'Unknown destination addresses seen and need to be resolved!')
for name in hosts:
	print('original IP -> ' +  name)


print('\n' + 'Resolve the IP to a  name:')
for name in hosts:
    try:
        aa = socket.gethostbyaddr(name)
        print('-> ' + aa[0])
    except:
        print ('-> ' + name + '  has no host record')
        continue

print('\n' + 'Is the IP actually active?:')


for name in hosts:
    response = os.system("ping -c 1 -w 2 " + name + " > /dev/null 2>&1")
    if response == 0:
        print('-> ' + name + ' is up!')
    else:
        print('-> ' + name + ' is down!')
