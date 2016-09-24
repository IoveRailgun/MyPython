#coding:utf-8
#autor:evan

import requests
import re
import sys
import json
import urllib2
import urllib


#get key
def getKeys(url):
    s = requests.Session()
    r = s.post(url)
    token = re.search(r'(?<=type="hidden" value=").+(?=" />)', r.text)
    keys=token.group()
    #print r.cookies
    return keys, r.cookies.values()[0]

#sendVote use requests
def sendVote(posturl,keys,getcookie,choice):
    s = requests.Session()
    #s.cookies.clear()
    #setcookies='__RequestVerificationToken='+getcookie+';_ga=GA1.2.1961587745.1472313057; _gat=1; Choice'+str(choice)+'=%2C98487%2C'
    setcookies='__RequestVerificationToken='+getcookie+'; Choice17224=%2C'+str(choice)+'%2C'
    #formdata='&__RequestVerificationToken='+keys+'&Choice='+str(choice)+'&X-Requested-With=XMLHttpRequest'
    #print posturl
    #print keys
    #print getcookie
    #print choice
    #print setcookies
    paras={'Choice':choice,          
            '__RequestVerificationToken':keys,
            'X-Requested-With':'XMLHttpRequest'}
    headers = {
          'Host': 'www.toutoupiao.com',
          'Connection': 'keep-alive',
          'Accept': '*/*',
          'Origin': 'http://www.toutoupiao.com',
          'X-Requested-With': 'XMLHttpRequest',
          'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
          'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'Referer': 'http://www.toutoupiao.com/Vote/17224?from=singlemessage&isappinstalled=0',
          'Accept-Encoding': 'gzip, deflate',
          'Accept-Language': 'zh-CN,zh;q=0.8',
          'Cookie':setcookies
    }
    r = s.post(posturl,data=paras,headers=headers)
    if r.status_code==200:
        return "sendVote ok"
    else:
        return "sendVote error"
    
  

#another method use urllib2
def sendVote2(posturl,keys,getcookie,choice):
    postDict = {
            '__RequestVerificationToken':keys,
            'Choice':choice,
            'X-Requested-With':"XMLHttpRequest"  
            }
    setcookies='__RequestVerificationToken='+getcookie+'; Choice17224=%2C'+str(choice)+'%2C'
    header = {
          'Host': 'www.toutoupiao.com',
          'Connection': 'keep-alive',
          'Accept': '*/*',
          'Origin': 'http://www.toutoupiao.com',
          'X-Requested-With': 'XMLHttpRequest',
          'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
          'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'Referer': 'http://www.toutoupiao.com/Vote/17224?from=singlemessage&isappinstalled=0',
          'Accept-Encoding': 'gzip, deflate',
          'Accept-Language': 'zh-CN,zh;q=0.8',
          'Cookie':setcookies
    }
    
    req = urllib2.Request(posturl, urllib.urlencode(postDict),headers=header)
    response = urllib2.urlopen(req)
    if response.code==200:
        return "sendVote ok"
    else:
        return "sendVote error"

if __name__=="__main__":
     #url="http://www.toutoupiao.com/Vote/17224?from=timeline&isappinstalled=0"
     url="http://www.toutoupiao.com/Vote/17224"
     posturl="http://www.toutoupiao.com/Ajax/SendVote/17224?PageSize=50&PageIndex=1"
     keys,getcookie=getKeys(url)
     #print getcookie
     #投一票
     #print sendVote(posturl,keys,getcookie,98487)
     print sendVote(posturl,keys,getcookie,98487)     
     #投N票     
     #for i  in xrange(0,6):
         #print sendVote(posturl,keys,getcookie,98487)
