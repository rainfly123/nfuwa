#!/usr/bin/env python
#-*- coding: utf-8 -*- 

import MySQLdb
import time
import string
from DBUtils.PooledDB import PooledDB
import dbconfig


ERROR = {0:"OK", 1:"Parameter Error", 2:"Database Error", 3:u"您已赞", 4:u"你无权开通直播"}
Default_Snapshot = "http://7xvsyw.com2.z0.glb.qiniucdn.com/n.jpg"

class DbManager():
    def __init__(self):
        kwargs = {}
        kwargs['host'] =  dbconfig.DBConfig.getConfig('database', 'dbhost')
        kwargs['port'] =  int(dbconfig.DBConfig.getConfig('database', 'dbport'))
        kwargs['user'] =  dbconfig.DBConfig.getConfig('database', 'dbuser')
        kwargs['passwd'] =  dbconfig.DBConfig.getConfig('database', 'dbpassword')
        kwargs['db'] =  dbconfig.DBConfig.getConfig('database', 'dbname')
        kwargs['charset'] =  dbconfig.DBConfig.getConfig('database', 'dbcharset')
        self._pool = PooledDB(MySQLdb, mincached=1, maxcached=15, maxshared=10, maxusage=10000, **kwargs)

    def getConn(self):
        return self._pool.connection()

_dbManager = DbManager()

def getConn():
    return _dbManager.getConn()

def Query():
    con = getConn()
    cur =  con.cursor()
    result = list()
    results = dict()

    selling = []
    sql = "select orderid, fuwaid, fuwagid, amount, owner from sell where state = 1"
    cur.execute(sql)
    res = cur.fetchall()

    for channel in res:
        temp = dict()
        temp['orderid'] = channel[0]
        temp['fuwaid'] = channel[1]
        temp['fuwagid'] = channel[2]
        temp['amount'] = channel[3]
        temp['owner'] = channel[4]
        result.append(temp)

    cur.close()
    con.close()
    results['code'] =  0
    results['message'] =  ERROR[0]
    results['data'] =  result
    return results

def Delete(orderid):
    con = getConn()
    cur =  con.cursor()

    result = dict()

    sql = "delete from sell where orderid = '{0}' ".format(orderid)
    cur.execute(sql)
    con.commit()

    cur.close()
    con.close()
    result['code'] =  0
    result['message'] =  ERROR[0]
    return result

def Done(orderid, buyer):
    con = getConn()
    cur =  con.cursor()

    result = dict()

    sql = "update sell set state = 2 where orderid = '{0}' ".format(orderid)
    cur.execute(sql)
    con.commit()
    sql = "update sell set buyer ='{0}' where orderid = '{1}' ".format(buyer, orderid)
    cur.execute(sql)
    con.commit()

    cur.close()
    con.close()
    result['code'] =  0
    result['message'] =  ERROR[0]
    result['data'] =  ""
    return result


def Create(fuwaid, fuwagid, amount, owner):
    con = getConn()
    cur =  con.cursor()
    result = dict()

    sql = "insert into sell (fuwaid,fuwagid,amount,owner,state)\
          values ('{0}', '{1}', '{2}', '{3}', 1)".format(fuwaid, fuwagid, amount, owner)

    cur.execute(sql)
    con.commit()
    cur.close()
    con.close()

    result['code'] =  0
    result['message'] =  ERROR[0]
    return result

if __name__ ==  '__main__':
    import cjson
    #a = u"王"
    #b =u"女"
    #ApplyLive("1234", a.encode('utf-8'), b.encode('utf-8'), "133333333333", "afadf.jpg")
    #print  Query()
    #print  Delete(1)
    print Create(66, "fuwa_33", 100.10, "xiechc")
    print  Query()
    print  Done(10, "john")
