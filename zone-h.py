#!/usr/bin/python

import requests
import os
from time import sleep

def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux,windows][os.name == 'nt'])

cls()
banner = '''

  Simple code for Zone-h Mass Poster

  Developer : jok3r
  
  telegram.me/publish
  
  instagram.com/localroot

'''
print(banner)
hacker = raw_input('Enter your Name: ')
text = raw_input('Enter your list: ')
openfile = open(text, 'r').readlines()
sleep(2)
cls()
print(banner)
for list_domain in openfile:
    with requests.Session() as c:
        print '\033[1;31m[!] sending   => ' + list_domain + '\033[1;m'
        #print '\033[1;32m[!] Attacker => ' + hacker + '\033[1;m'+'\n'
        link = 'http://www.zone-h.com/notify/single'
        c.get(link)
        post_data = dict(defacer=hacker, domain1=list_domain, hackmode=18, reason=5)
        c.post(link, data=post_data, headers={"Referer": "http://www.zone-h.com"})
        page = c.get('http://www.zone-h.com/notify/single')
print 'Done ~ Good Luck'
sleep(2)
