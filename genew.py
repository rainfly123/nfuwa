#!/usr/bin/env python
#-*- coding: utf-8 -*- 
import redis  
import random
import urllib2
import json
import mysql
import pickle

BASE = "https://api.66boss.com/ucenter/userinfo/info?user_id="
pool = redis.ConnectionPool(host='127.0.0.1', port=6379, password="aaa11bbb22")  
r = redis.Redis(connection_pool=pool)  

def getName(userid):
    response = urllib2.urlopen(BASE + userid)
    html = response.read()
    if not html:
        return dict()
    data =  json.loads(html)
    response.close()
    dic = {"name": data['user_name'], "avatar": data['avatar'], "gender": data['sex'],\
           "location":data['district_str'], "signature":data['signature']}
    return dic

def gene(userid, info, total, shop):
    gid = r.get("globalid")
    start = int(gid)
    for i in range (total):
        r.incr("globalid")
        fid = str(start + i)
        if shop :
            key ="fuwa_c_%s"%fid
        else:
            key ="fuwa_i_%s"%fid
        temp = dict()
        temp["owner"] = userid
        idd = random.randint(1,65)
        if idd in [6, 16, 26, 36, 46, 56]:
            idd -= 1
        temp["id"] =  idd        
        temp["creator"] = userid
        temp["awarded"] = "0" 
        temp["pos"] = "广州大酒店"
        temp["name"] = info['name']
        temp["avatar"] = info['avatar']
        temp["gender"] = info['gender']
        temp["location"] = info['location']
        temp["signature"] = info['signature']
        i=r.hmset(key, temp)
        r.sadd(userid + "_apply", key)

def Create(userid, total, shop):
    info = getName(userid)
    gene(userid, info, total, shop)

con = mysql.getConn()
cur =  con.cursor()

result = dict()
f2 = file('temp.pkl', 'rb')  
midd = pickle.load(f2)  
f2.close()
sql = "select id, userid, number,shop from application where id > {0} ".format(midd)
cur.execute(sql)
res = cur.fetchall()
cur.close()
con.close()
for idd, userid, number, shop in res:
    print idd, userid, number,shop
    if number > 200:
       number = 200
    if shop == 1:
        Create(userid, number, True)
    else:
        Create(userid, number, False)
    midd = idd
f1 = file('temp.pkl', 'wb')  
pickle.dump(midd, f1, True)  
f1.close()
