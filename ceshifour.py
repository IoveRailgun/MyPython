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

def createPhone():
  prelist=["130","131","132","133","134","135","136","137","138","139","147","150","151","152","153","155","156","157","158","159","186","187","188"]
  return random.choice(prelist)+"".join(random.choice("0123456789") for i in range(8))



def group(strl,n):
    ls = re.findall(r'\"(.*?)\"',strl)
    return ls[n]

def sendOne(posturl,name,tel,school,cre,invite,s):
    "注册"
    paras={'username':name,
           'phoneNumber':tel,
           'school':school,
           'identityNum':cre,
           'inviteNum':invite
           }
    headers = {
               'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
               }
    r = s.post(posturl,data=paras,headers=headers)
    return r.content

def sendTwo(s,text,name,tel):
    "回答问题"
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
    chooses4 = [group(choose[4], 0),group(choose[4], 1),group(choose[4], 2),group(choose[4], 3)]
    paras={
            'useranswer[]':answerOne,
             'questions[0][_id]':id[0],
             'questions[0][key]':key[0],
             'questions[0][title]':title[0],
             'questions[0][answerOne]':answerOne[0],
             'questions[0][answerUrl]':answerUrl[0],
             'questions[0][__v]':0,
             'questions[0][choose][]':chooses0,
             'questions[0][questionType]':'单选题',
             'questions[1][_id]':id[1],
             'questions[1][key]':key[1],
             'questions[1][title]':title[1],
             'questions[1][answerOne]':answerOne[1],
             'questions[1][answerUrl]':answerUrl[1],
             'questions[1][__v]':0,
             'questions[1][choose][]':chooses1,
             'questions[1][questionType]':'单选题',
             'questions[2][_id]':id[2],
             'questions[2][key]':key[2],
             'questions[2][title]':title[2],
             'questions[2][answerOne]':answerOne[2],
             'questions[2][answerUrl]':answerUrl[2],
             'questions[2][__v]':0,
             'questions[2][choose][]':chooses2,
             'questions[2][questionType]':'单选题',
             'questions[3][_id]':id[3],
             'questions[3][key]':key[3],
             'questions[3][title]':title[3],
             'questions[3][answerOne]':answerOne[3],
             'questions[3][answerUrl]':answerUrl[3],
             'questions[3][__v]':0,
             'questions[3][choose][]':chooses3,
             'questions[3][questionType]':'单选题',
             'questions[4][_id]':id[4],
             'questions[4][key]':key[4],
             'questions[4][title]':title[4],
             'questions[4][answerOne]':answerOne[4],
             'questions[4][answerUrl]':answerUrl[4],
             'questions[4][__v]':0,
             'questions[4][choose][]':chooses4,
             'questions[4][questionType]':'单选题',
             'finalClick':True
    }
    headers={
              'Host': 'kaixue.wanfangdata.com.cn',
              'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
              'Content-Length': '6606',
              'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
              'X-Requested-With':'XMLHttpRequest'
              }
    url = 'http://kaixue.wanfangdata.com.cn/record'
    r = s.post(url, data=paras,headers=headers)
    print r
    
    dat={
         'username':name,
         'phoneNumber':tel
         }
    headers = {
               'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
               }
     
    r = s.post('http://kaixue.wanfangdata.com.cn/login',data=dat,headers=headers)
    if(r.status_code==200):
        return r.content
    else:
        print "eroror"
      
    
    
    
if __name__=="__main__":
    posturlt = 'http://kaixue.wanfangdata.com.cn/register'
    n = input('Please enter the lottery number:')
    sexku =['赵','钱','孙','李','周','吴', '郑', '王','冯','陈 ','楮','卫 ','蒋','沈','韩','杨','朱','秦','尤','许 ','何 ','吕 ','施 ','张 ','孔','曹 ','严','华 ','金','魏 ','陶','姜','戚 ','谢 ','邹','喻','柏 ','水 ','窦','章 ','云 ','苏','潘','葛','奚 ','范','彭 ','郎 ','鲁 ','韦','昌 ','马','苗','凤 ','花','方','俞 ','任 ','袁','柳 ','酆 ','鲍','史','唐','费 ','廉','岑','薛','雷','贺 ','倪 ','汤 ','祝','左','涂','谷','祁','时','舒','耿','牟','卜','路','詹','关','苗','凌','费','纪','靳','盛','童','景','蒲','单','包','司','柏','宁','柯','阮','桂','闵','欧','阳','解','强','柴','华','车','冉','边','全','褚','廉','简','娄','盖','符','奚','木','穆','党','燕','郎','邸','冀','谈','屠','连','郜','都','巩','稽','井','练','仲','乐','虞','卞','封','竺','冼','原','官','衣','楚','佟','栗','匡','宗']
    mingku = ['雅静','倩雪','飞','浩','豪','梦琪','忆柳','之桃','慕青','问兰','尔岚','元香','初夏','沛菡','傲珊','曼文','乐菱','痴珊','恨玉','惜文','香寒','新柔','语蓉','海安','夜蓉','涵柏','水桃','醉蓝','语琴','从彤','傲晴','语兰','又菱','碧彤','元霜','怜梦','紫寒','妙彤','曼易','南莲','紫翠','雨寒','易烟','白 ','宾鸿 ','宾实','彬彬 ','彬炳','彬郁 ','斌斌','蔚 ','海 ','波','波鸿','波峻','波涛','博瀚','超 ','博达 ','博厚 ','博简 ','博明 ','容 ','博赡','博涉 ','博实 ','博涛 ','博文 ','博学 ','博雅 ','博延 ','博艺','易','博裕','辰逸','尉','卫','伟','博','程','程飞','涛','赛赛','岩心','亚心','安','健康','东东','勋','然','毅','杰','浩','坤','熙','川','轩','博','渊','涵','嘉','文','耀','辉','恺','恒','温']
    un = ['清华大学 ','北京大学 ','浙江大学','海交通大学','南京大学 ','复旦大学','华中科技大学 ','武汉大学 ','吉林大学 ','西安交通大学 ','中国科学技术大学','中山大学 ','四川大学 ','哈尔滨工业大学 ','山东大学 ','天津大学 ','南开大学 ','中南大学 ','北京师范大学 ','中国人民大学 ','厦门大学 ','北京航空航天大学 ','东南大学 ','同济大学','大连理工大学 ','西北工业大学 ','华南理工大学 ','重庆大学 ','中国农业大学 ','华东师范大学 ','兰州大学 ','东北大学','北京理工大学 ','湖南大学 ','苏州大学 ','郑州大学 ','中国石油大学 ','华东理工大学','南京航空航天大学 ','武汉理工大学 ','中国矿业大学 ','南京农业大学 ','北京科技大学 ','暨南大学 ','西安电子科技大学 ','西北大学 ','电子科技大学 ','南京理工大学 ','西北农林科技大学 ','上海大学 ','西南大学 ','南京师范大学 ','西南交通大学 ','东北师范大学 ','华中师范大学 ','华中农业大学 ','扬州大学 ','中国海洋大学 ','华南师范大学 ','湖南师范大学','北京化工大学 ','河南城建学院','安阳工学院']

    for i in xrange(0 , n*3):
        try:
            s = requests.session()
            name = random.choice(sexku)+random.choice(mingku) #随机姓名
            tel = createPhone()  #随机手机号
            school = random.choice(un) #随机学校
            cre = random.randint(100000,999999) #随机学号
            print name
            print tel
            print school
            print cre
            invite = 'Sy9N7n7T'  #邀请码
            text = sendOne(posturlt,name,tel,school,cre,invite,s) #注册账号，返回注册后界面
            print sendTwo(s,text,name,tel) #答题
        except Exception,ex:
            continue


    
    
    
    
    
    
    
    