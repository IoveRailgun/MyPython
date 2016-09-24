#coding:utf-8
#autor:h

import requests
import traceback
import re
import urllib2
import urllib
import os
import random
from random import choice

n = input('note is:')

for i in xrange(0,n):   
    print str(i)+' draw'
    url = 'http://kaixue.wanfangdata.com.cn/login'
    data={
          'username':'季小意',
          'phoneNumber':'13283052512'
          }
    headers = {
               'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
               }
    s = requests.session()
    r = s.post(url,data=data,headers=headers)
    r = s.get('http://kaixue.wanfangdata.com.cn/lotteryprize?inviteNum=Sy9N7n7T',headers=headers)
    r = s.get('http://kaixue.wanfangdata.com.cn/api/prize',headers=headers)
    t = eval(r.text)
    print t
    if((t['success']==1)and(t['degree']==5)):
        print 'Did not draw in the prize'
    else:
        print 'It might have been a prize. Let\'s go and see!'
        break
    
