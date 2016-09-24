#coding:utf-8
#autor:h

import requests
import re
import sys
import json
import urllib2
import urllib
import os
import random
import time
import socket
socket.setdefaulttimeout(180)

def group(strl,n):
    ls = re.findall(r'\"(.*?)\"',strl)
    return ls[n]


def getCookie(posturl):
    s = requests.session()
    r = s.post(posturl)
    #print r.cookies.values()
    #print r.cookies.keys()
    gettime=str(int(time.time()))#COOKIE取得时间
    #return  r.cookies.keys()[0]+"="+r.cookies.values()[0]+"; Hm_lvt_aca6e7e9684cf1e0028155b8175a4f2d="+gettime
    #return  r.cookies.keys()[0]+"="+r.cookies.values()[0]
    return r.cookies.values()[0]

def sendOne(posturl,name,tel,school,cre,invite,getcookie):
    "注册"
    #getcookie=getcookie+"; Hm_lpvt_aca6e7e9684cf1e0028155b8175a4f2d="+str(int(time.time()))
    print getcookie
    s = requests.session()
    paras={'username':name,
           'phoneNumber':tel,
           'school':school,
           'identityNum':cre,
           'inviteNum':invite
           }
    print paras
    headers = {
               'Host': 'kaixue.wanfangdata.com.cn',
               'Connection': 'keep-alive',
               'Content-Length': '147',
               'Cache-Control': 'max-age=0',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Origin': 'http://kaixue.wanfangdata.com.cn',
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
               'Content-Type': 'application/x-www-form-urlencoded',
               'Referer': 'http://kaixue.wanfangdata.com.cn/login',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.8',
               'Cookie': getcookie
               }
    r = s.post(posturl, data=paras, headers=headers)
     
    #print  r1.cookies.keys()
    if(r.status_code==200):
        return r.content



def sendTwo(getcookie,text,gettime):
    "回答问题"
    myquestions=[]
    s = requests.session()
    setcookie=getcookie+"; Hm_lvt_aca6e7e9684cf1e0028155b8175a4f2d="+gettime+"; Hm_lpvt_aca6e7e9684cf1e0028155b8175a4f2d="+str(int(time.time()))
    #setcookie="keystone.sid="+getcookie+"; Hm_lpvt_aca6e7e9684cf1e0028155b8175a4f2d=1474116825"
    #setcookie='''keystone.sid=s%3AHMHLSPMKYUPWEA-R2o6lsEn-BCXuALnk.wRDqpfx%2FUhkfF5e8Hh8gYRGOwPLkhFSavklG%2F1FsXC8; Hm_lvt_aca6e7e9684cf1e0028155b8175a4f2d=1474116806; Hm_lpvt_aca6e7e9684cf1e0028155b8175a4f2d=1474118343'''
    print setcookie
   
    texto = re.search(r'(?<=window.questions = \[\{).+?(?=}];)', text)
    textt = texto.group()
    id = re.findall(r'\"_id\":\"(.*?)\"', textt)
    key = re.findall(r'\"key\":\"(.*?)\"', textt)
    title = re.findall(r'\"title\":\"(.*?)\"', textt)
    answerOne = re.findall(r'\"answerOne\":\"(.*?)\"', textt)
    answerUrl = re.findall(r'\"answerUrl\":\"(.*?)\"', textt)
    choose = re.findall(r'\"choose\":\[(.*?)\]', textt)
    chooses0 = [group(choose[0], 0),group(choose[0], 1),group(choose[0], 2),group(choose[0], 3)]
    chooses1 = [group(choose[1], 0),group(choose[1], 1),group(choose[1], 2),group(choose[1], 3)]
    chooses2 = [group(choose[2], 0),group(choose[2], 1),group(choose[2], 2),group(choose[2], 3)]
    chooses3 = [group(choose[3], 0),group(choose[3], 1),group(choose[3], 2),group(choose[3], 3)]
    #chooses4 = [group(choose[4], 0),group(choose[4], 1),group(choose[4], 2),group(choose[4], 3)]
   
        
    questions={}    
   
    for i in range(0,4):      
        questions["_id"]=id[i]
        questions["key"]=key[i]
        questions["title"]=title[i]
        questions["answerMore"]=[]
        questions["answerOne"]=answerOne[i]
        questions["answerUrl"]=answerUrl[i]
        questions["__v"]="0"
        questions["questionType"]="单选题"

        
        questions["choose"]=[group(choose[i], 0),group(choose[i], 1),group(choose[i], 2),group(choose[i], 3)]
        #print questions["title"]
        myquestions.append(dict(questions))
    #print myquestions
    #return
   
        

    
    #print chooses0[2]
    paras={
        'useranswer':answerOne,
        'questions':myquestions,
        'finalClick':True
    }
    headers={
            'Accept':'*/*',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'Cache-Control':'no-cache',
            #'Content-Length':9999,
            'Connection':'keep-alive',
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie':setcookie+'''; WFKS.Auth=%7b%22Context%22%3a%7b%22AccountIds%22%3a%5b%5d%2c%22Data%22%3a%5b%5d%2c%22SessionId%22%3a%2286d0f7d7-c1ed-482d-b5fe-d424eafd8c31%22%2c%22Sign%22%3a%22hi+authserv%22%7d%2c%22LastUpdate%22%3a%222016-09-17T15%3a23%3a58Z%22%2c%22TicketSign%22%3a%22C9KnEtDY1aeTPLisVrpivg%3d%3d%22%7d''',
            'Host':'kaixue.wanfangdata.com.cn',
            'Pragma':'no-cache',
            'Origin':'http://kaixue.wanfangdata.com.cn',
            'Referer':'http://kaixue.wanfangdata.com.cn/answer',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest'
             }
    url = 'http://kaixue.wanfangdata.com.cn/record'
    #url2 = 'http://kaixue.wanfangdata.com.cn/judge?inviteNum=B1MwN0q2'

    postbody = json.dumps(paras)
    print  postbody
    r = s.post(url, data=postbody, headers=headers,timeout=220) #post第一道题
    print"s"*20
    #rint r.cookies.values()
    #r2 = s.post(url2, data=postbody, headers=headers2) #post第一道题

    #print r.content
  
    if(r.status_code==200):
        print r.content
    else:
        print r.status_code
    s = requests.session()
  
   

    
if __name__=="__main__":
    posturl ="http://wanfangdata.com.cn/"
    posturlt = 'http://kaixue.wanfangdata.com.cn/register'
    
    name = ''.join(map(lambda xx:(hex(ord(xx))[2:]),os.urandom(5))) #随机姓名
    tel = random.randint(10000000000,99999999999)  #随机手机号
    school = ''.join(map(lambda xx:(hex(ord(xx))[2:]),os.urandom(6))) #随机学校
    cre = random.randint(100000,999999) #随机学号
    invite = "HkrjNME3"  #邀请码等于空
    
    #cookieo = 'WFKS.Auth='+getCookie(posturl)+'; keystone.sid='+getCookie(posturlt)
    cookieoo = getCookie(posturlt)  #获得cookieoo
    gettime=str(int(time.time()))
    #setcookie = 'keystone.sid='+cookieoo
    #print setcookie
    text = sendOne(posturlt,name,tel,school,cre,invite,cookieoo) #注册账号，返回注册后界面
    #print text
    sendTwo(cookieoo,text,gettime) #答题

    
    
    
    
    
    
    
