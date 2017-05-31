#!/usr/bin/env python
#-*- coding: utf-8 -*- 
import redis  
from tornado import gen
import tornado
import json
import time
import random
import getdis

STORE_PATH="/www/html/fuwa/"
pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=1, password="aaa11bbb22")  
r = redis.Redis(connection_pool=pool)  

HOWFAR = 60 
def QueryFuwaNew(longtitude, latitude, radius, biggest):
    if biggest == "0":
        biggest = 0x1fffffff
    else:
        biggest = int(biggest)

    fuwas = r.georadius("fuwa_c", longtitude, latitude, int(radius), unit="m", withdist=True)
    near = [x for x in fuwas if x[1] <= HOWFAR and int(x[0][7:]) < biggest]
    far = [x for x in fuwas if x[1] > HOWFAR]
    near = sorted(near, key=lambda x: int(x[0][7:]), reverse=True)
    near = near[:100]

    nearfuwas = list()
    for fuwa in near:
        fuwaid, distance = fuwa[0], fuwa[1]
        detail, pos, pic, idd = r.hmget(fuwaid, "detail", "pos", "pic", "id")
        geohash = r.geopos("fuwa_c", fuwaid)
        geo = "%f-%f"%(geohash[0][0], geohash[0][1])

        name, avatar, gender, signature, location, video, owner = r.hmget(fuwaid, "name", "avatar", "gender", "signature", "location", "video", "owner")

        result  = {"gid":fuwaid, "distance":distance, "pos":pos, "id":idd, "geo":geo, "pic":pic, "detail":detail,\
                  "name":name, "avatar":avatar, "gender":gender, "signature":signature, "location":location,\
                  "video":video, "hider": owner}
        nearfuwas.append(result)

    farfuwas = list()
    for fuwa in far:
        if len(farfuwas) >= 300:
            break
        fuwaid, distance = fuwa[0], fuwa[1]
        detail, pos, pic, idd = r.hmget(fuwaid, "detail", "pos", "pic", "id")
        geohash = r.geopos("fuwa_c", fuwaid)
        geo = "%f-%f"%(geohash[0][0], geohash[0][1])

        name, avatar, gender, signature, location, video, owner = r.hmget(fuwaid, "name", "avatar", "gender", "signature", "location", "video", "owner")

        result  = {"distance":distance, "pos":pos, "geo":geo, "pic":pic, "detail":detail,\
                  "name":name, "avatar":avatar, "gender":gender, "signature":signature, "location":location,\
                  "video":video, "hider": owner, "number":1}
        total = len(farfuwas)
        for x in xrange(total):
            if farfuwas[x]['geo'] == geo:
                farfuwas[x]['number'] += 1
        if x == (total - 1):
            farfuwas.append(result)
        farfuwas.append(result)

    return {"far":farfuwas, "near":nearfuwas}

def QueryStrFuwaNew(longtitude, latitude, radius, biggest):
    if biggest == "0":
        biggest = 0x1fffffff
    else:
        biggest = int(biggest)

    fuwas = r.georadius("fuwa_i", longtitude, latitude, int(radius), unit="m", withdist=True)
    near = [x for x in fuwas if x[1] <= HOWFAR and int(x[0][7:]) < biggest]
    far = [x for x in fuwas if x[1] > HOWFAR]
    near = sorted(near, key=lambda x: int(x[0][7:]), reverse=True)
    near = near[:100]

    nearfuwas = list()
    for fuwa in near:
        fuwaid, distance = fuwa[0], fuwa[1]
        detail, pos, pic, idd = r.hmget(fuwaid, "detail", "pos", "pic", "id")
        geohash = r.geopos("fuwa_i", fuwaid)
        geo = "%f-%f"%(geohash[0][0], geohash[0][1])

        name, avatar, gender, signature, location, video, owner = r.hmget(fuwaid, "name", "avatar", "gender", "signature", "location", "video", "owner")

        result  = {"gid":fuwaid, "distance":distance, "pos":pos, "id":idd, "geo":geo, "pic":pic, "detail":detail,\
                  "name":name, "avatar":avatar, "gender":gender, "signature":signature, "location":location,\
                  "video":video, "hider": owner}
        nearfuwas.append(result)

    farfuwas = list()
    for fuwa in far:
        if len(farfuwas) >= 300:
            break
        fuwaid, distance = fuwa[0], fuwa[1]
        detail, pos, pic, idd = r.hmget(fuwaid, "detail", "pos", "pic", "id")
        geohash = r.geopos("fuwa_i", fuwaid)
        geo = "%f-%f"%(geohash[0][0], geohash[0][1])

        name, avatar, gender, signature, location, video, owner = r.hmget(fuwaid, "name", "avatar", "gender", "signature", "location", "video", "owner")

        result  = {"distance":distance, "pos":pos, "geo":geo, "pic":pic, "detail":detail,\
                  "name":name, "avatar":avatar, "gender":gender, "signature":signature, "location":location,\
                  "video":video, "hider": owner, "number":1}
        total = len(farfuwas)
        for x in xrange(total):
            if farfuwas[x]['geo'] == geo:
                farfuwas[x]['number'] += 1
        if x == (total - 1):
            farfuwas.append(result)
        farfuwas.append(result)

    return {"far":farfuwas, "near":nearfuwas}

def QueryFuwav3(longtitude, latitude, radius, biggest):
    if biggest == "0":
        biggest = 0x1fffffff
    else:
        biggest = int(biggest)

    fuwas = r.georadius("fuwa_c", longtitude, latitude, int(radius), unit="m", withdist=True)
    near = [x for x in fuwas if x[1] <= HOWFAR and int(x[0][7:]) < biggest]
    far = [x for x in fuwas if x[1] > HOWFAR]
    near = sorted(near, key=lambda x: int(x[0][7:]), reverse=True)
    near = near[:100]

    nearfuwas = list()
    for fuwa in near:
        fuwaid, distance = fuwa[0], fuwa[1]
        detail, pos, pic, idd = r.hmget(fuwaid, "detail", "pos", "pic", "id")
        geohash = r.geopos("fuwa_c", fuwaid)
        geo = "%f-%f"%(geohash[0][0], geohash[0][1])

        name, avatar, gender, signature, location, video, owner = r.hmget(fuwaid, "name", "avatar", "gender", "signature", "location", "video", "owner")

        result  = {"gid":fuwaid, "distance":distance, "pos":pos, "id":idd, "geo":geo, "pic":pic, "detail":detail,\
                  "name":name, "avatar":avatar, "gender":gender, "signature":signature, "location":location,\
                  "video":video, "hider": owner}
        nearfuwas.append(result)

    farfuwas = list()
    for fuwa in far:
        if len(farfuwas) >= 300:
            break
        fuwaid, distance = fuwa[0], fuwa[1]
        detail, pos, pic, idd = r.hmget(fuwaid, "detail", "pos", "pic", "id")
        geohash = r.geopos("fuwa_c", fuwaid)
        geo = "%f-%f"%(geohash[0][0], geohash[0][1])

        name, avatar, gender, signature, location, video, owner = r.hmget(fuwaid, "name", "avatar", "gender", "signature", "location", "video", "owner")

        result  = {"distance":distance, "pos":pos, "geo":geo, "pic":pic, "detail":detail,\
                  "name":name, "avatar":avatar, "gender":gender, "signature":signature, "location":location,\
                  "video":video, "hider": owner, "number":1}
        total = len(farfuwas)
        for x in xrange(total):
            if farfuwas[x]['geo'] == geo:
                farfuwas[x]['number'] += 1
        if x == (total - 1):
            farfuwas.append(result)
        farfuwas.append(result)

    return {"far":farfuwas, "near":nearfuwas}

BASE = "https://api.66boss.com/ucenter/userinfo/info?user_id="
def HideFuwaNew(longtitude, latitude, pos, pic, owner, detail, video, number, purpose,\
               videogeo, filemd5):

    results = r.smembers(owner + "_apply")
    shufflefuwas = list(results)
    random.shuffle(shufflefuwas)

    nows = str(int(time.time()))
    if purpose == "1":
        for which in xrange(len(results)):
            fuwagid  = shufflefuwas[which]
            if fuwagid.find('i') > 0:
                continue
            r.geoadd("fuwa_c", longtitude, latitude, fuwagid)
            r.geoadd(videogeo, longtitude, latitude, filemd5)
            name, avatar, gender = r.hmget(fuwagid, "name", "avatar", "gender")
            vdic = {"name":name, "avatar":avatar, "gender":gender, "userid":owner, "video":video}
            r.hmset(filemd5, vdic) 
            dic = {"pos": pos, "pic": pic, "detail": detail, "video": video, "htime": nows}
            r.hmset(fuwagid, dic) 
            r.srem(owner + "_apply", fuwagid)
            number -= 1
            if number == 0 :
                break
    else:
        for which in xrange(len(results)):
            fuwagid  = shufflefuwas[which]
            if fuwagid.find('c') > 0:
                continue
            r.geoadd("fuwa_i", longtitude, latitude, fuwagid)
            r.geoadd(videogeo, longtitude, latitude, filemd5)
            name, avatar, gender = r.hmget(fuwagid, "name", "avatar", "gender")
            vdic = {"name":name, "avatar":avatar, "gender":gender, "userid":owner, "video":video}
            r.hmset(filemd5, vdic) 
            dic = {"pos": pos, "pic": pic, "detail": detail, "video": video, "htime": nows}
            r.hmset(fuwagid, dic) 
            r.srem(owner + "_apply", fuwagid)
            number -= 1
            if number == 0 :
                break

def CaptureFuwa(pic, user, gid):
    import os
    import imgcmp

    filename = os.path.basename(pic)
    fullpath = os.path.join(STORE_PATH, filename)
    clue = r.hget(gid, "pic") 
    filenamec = os.path.basename(clue)
    fullpathc = os.path.join(STORE_PATH, filenamec)
    ok = imgcmp.ImgCmp(fullpathc, fullpath)
    if ok < 45:
        return False

    pipe = r.pipeline()
    pipe.hset(gid, "owner", user)
    pipe.sadd(user + "_pack", gid)
    if gid.find('c') > 0:
        pipe.zrem("fuwa_c", gid)
    else:
        pipe.zrem("fuwa_i", gid)
    pipe.execute()
    return True

def Capturev2Fuwa(user, gid):

    pipe = r.pipeline()
    pipe.hset(gid, "owner", user)
    pipe.sadd(user + "_pack", gid)
    if gid.find('c') > 0:
        pipe.zrem("fuwa_c", gid)
    else:
        pipe.zrem("fuwa_i", gid)
    pipe.execute()
    return True

def QueryMy(user):
    outs = list()
    
    results = r.smembers(user + "_pack")
    for gid in results:
        out = dict()
        creator, name, pos, awarded, idd = r.hmget(gid, "creator", "name", "pos", "awarded", "id")
        out['creatorid'] = creator 
        out['creator'] = name 
        out['pos'] = pos
        out["gid"] = gid
        out["id"] = idd
        if awarded is '0':
            out['awarded'] = False
        else:
            out['awarded'] = True
        outs.append(out)
    return outs

def QueryMyApply(user):
    outs = list()

    results = r.smembers(user + "_apply")
    for gid in results:
        creator, idd = r.hmget(gid, "name", "id")
        out = {'creator':creator, "gid":gid, "id":idd}
        outs.append(out)
    return outs

def QueryMyfortop(user):
    outs = dict()
    fuwas = list()
    results = r.smembers(user + "_pack")
    for gid in results:
        idd = r.hget(gid, "id")
        if outs.has_key(idd):
            outs[idd] += 1
        else:
            outs[idd] = 1

    for key in sorted(outs.keys(), key=lambda x:int(x)):
        fuwa = dict()
        fuwa['id'] = key
        fuwa['number'] = outs[key]
        fuwas.append(fuwa)

    return fuwas

def QueryDetail(gid):
    outs = dict()

    creator, pos, awarded = r.hmget(gid, "name", "pos", "awarded")

    outs['creator'] = creator
    outs['pos'] = pos
    if awarded is '0':
        outs['awarded'] = False
    else:
        outs['awarded'] = True
    
    return outs

def Donate(touser, gid, fromuser):
    if len(touser) != 9:
        return 1
    outs = dict()
    i=r.srem(fromuser + "_pack", gid)
    if i == 0:
        return 1
    r.sadd(touser + "_pack", gid)
    r.hset(gid, "owner", touser)
    return 0

MES1 = u"你不是福娃的生成者"
MES2 = u"此福娃已兑奖"
MES0 = u"成功"

def Award(user, gid):
    creator, awarded = r.hmget(gid, "creator", "awarded")
    if creator != user:
        return 1, MES1

    if awarded is '1':
        return 2, MES2

    r.hset(gid, "awarded", "1")
    return 0, MES0

def Huodong(gid):
    detail = r.hget(gid, "detail")
    if detail != None:
        pass
    else:
        detail = ""
    return detail

aclass =[{"name":"美食", "enum":"1"}, {"name":"女装", "enum":"2"}, {"name":"男装", "enum":"3"},\
        {"name":"鞋帽", "enum":"4"}, {"name":"玩乐", "enum":"5"}]

def Class():
    return aclass

def Hit(filemd5, classid):
    r.zincrby("video_" + classid, filemd5, amount=1)
    return True

def QueryVideo(classid, longtitude, latitude):
    location = (latitude, longtitude)
    filemd5s = r.zrevrange("video_" + classid, 0, 9)
    positions = r.geopos("video_g_" + classid, *filemd5s)
    distances = list()
    for pos in postions:
        dis = getdis.getdistance(location, (pos[1], pos[0]))
        distances.append(dis)
    results = list()
    which = 0
    for filemd5 in filemd5s:
        temp = dict()
        name, gender, avatar, userid, video, width, height = \
        r.hmget(filemd5, "name", "gender", "avatar", "userid", "video", "width", "height")
        temp['name'] = name
        temp['gender'] = gender
        temp['avatar'] = avatar
        temp['userid'] = userid
        temp['video'] = video
        temp['width'] = width
        temp['height'] = height
        temp['distance'] = distances[which]
        temp['filemd5'] = filemd5
        results.append(temp)
        which += 1 

    videos = r.georadius("video_g_"+classid, longtitude, latitude, 50000, unit="m", withdist=True, sort="ASC")
    for video in videos:
        filemd5, far = video[0], video[1]
        temp = dict()
        name, gender, avatar, userid, video, width, height = \
        r.hmget(filemd5, "name", "gender", "avatar", "userid", "video", "width", "height")
        temp['name'] = name
        temp['gender'] = gender
        temp['avatar'] = avatar
        temp['userid'] = userid
        temp['video'] = video
        temp['width'] = width
        temp['height'] = height
        temp['distance'] = far
        temp['filemd5'] = filemd5
        results.append(temp)

    return results

def QueryStrVideo(longtitude, latitude):
    location = (latitude, longtitude)
    filemd5s = r.zrevrange("video_i", 0, 9)
    positions = r.geopos("video_g_i", *filemd5s)
    distances = list()
    for pos in postions:
        dis = getdis.getdistance(location, (pos[1], pos[0]))
        distances.append(dis)
    results = list()
    which = 0
    for filemd5 in filemd5s:
        temp = dict()
        name, gender, avatar, userid, video, width, height = \
        r.hmget(filemd5, "name", "gender", "avatar", "userid", "video", "width", "height")
        temp['name'] = name
        temp['gender'] = gender
        temp['avatar'] = avatar
        temp['userid'] = userid
        temp['video'] = video
        temp['width'] = width
        temp['height'] = height
        temp['distance'] = distances[which]
        temp['filemd5'] = filemd5
        results.append(temp)
        which += 1 

    videos = r.georadius("video_g_i", longtitude, latitude, 50000, unit="m", withdist=True, sort="ASC")
    for video in videos:
        filemd5, far = video[0], video[1]
        temp = dict()
        name, gender, avatar, userid, video, width, height = \
        r.hmget(filemd5, "name", "gender", "avatar", "userid", "video", "width", "height")
        temp['name'] = name
        temp['gender'] = gender
        temp['avatar'] = avatar
        temp['userid'] = userid
        temp['video'] = video
        temp['width'] = width
        temp['height'] = height
        temp['distance'] = far
        temp['filemd5'] = filemd5
        results.append(temp)

    return results


#print QueryMyApply("100000076")
#print QueryMy("100000320")
#print CaptureFuwa("http://afa/daf/pic.jpg", "john", "fuwa_1")
#print QueryStrFuwaNew(113.3, 23.09 , 9000, "0")
