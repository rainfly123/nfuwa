#!/usr/bin/env python
#-*- coding: utf-8 -*- 

import MySQLdb
import time
import string
from DBUtils.PooledDB import PooledDB
import dbconfig
import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)  
r = redis.Redis(connection_pool=pool)  

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

    selling = []
    sql = "select orderid, fuwagid, owner, time from sell where state = 1"
    cur.execute(sql)
    res = cur.fetchall()
    now = datetime.datetime.now()
    outdated = [(chan[0], chan[1], chan[2]) for chan in res if (now - chan[3]).total_seconds() >= 86400] 
    for chan in outdated:

        orderid = chan[0]
        gid = chan[1]
        owner = chan[2]

        sql = "delete from sell where orderid = %s"%orderid
        cur.execute(sql)
        con.commit()
        r.sadd(owner + "_pack", gid)

    cur.close()
    con.close()

if __name__ ==  '__main__':
    import cjson
    import datetime
    print  Query()
