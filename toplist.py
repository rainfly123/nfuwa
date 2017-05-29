#!/usr/bin/env python
"""API for Query one's friend list"""
import urllib2
import json
import redi

URL="https://api.66boss.com/ucenter/userinfo/friendlist?user_id="
def GetUserInfo(userid):
    response = urllib2.urlopen(URL + userid)
    jsonres = response.read()
    response.close()
    return json.loads(jsonres)

def GetToplist(userid):
    result = list()
    for user in GetUserInfo(userid):
        key = str(user['user_id']) + "_pack"
        how = redi.r.scard(key)
        if how == 0:
            continue
        temp = dict()
        temp['user'] = user['user_id']
        temp['snap'] = user['avatar']
        temp['nick'] = user['user_name']
        temp['number'] = how
        result.append(temp)
    result.sort(key=lambda x:x['number'],reverse=True)
    return result

if __name__ == "__main__":
    print GetToplist("100000000")
    
