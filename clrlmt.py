#!/usr/bin/env python
# -*- coding:utf-8 -*-
import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=1, password="aaa11bbb22")
for x in xrange(10000):
    key = str(x) + "_lmt"
    r.delete(key)
