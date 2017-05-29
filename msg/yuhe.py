#!/usr/bin/env python
#-*- coding: utf-8 -*- 

import MySQLdb
import time
import string
from DBUtils.PooledDB import PooledDB
import dbconfig
from tornado import gen


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

def yuHe():
    con = getConn()
    cur = con.cursor()
    sql = "select owner, amount, orderid  from sell where state = 2"
    cur.execute(sql)
    results = cur.fetchall()
    for result in results:
        userid = result[0]
        amount = result[1]
        orderid = result[2]
        sqlm = "update money set amount = amount + %s where userid='%s'"%(amount, userid)
        print userid, amount, orderid
        print sqlm
        cur.execute(sqlm)
        sqls = "update sell set state = 3 where orderid = %s"%(orderid)
        print sqls
        cur.execute(sqls)
        con.commit()

    cur.close()
    con.close()

yuHe()
