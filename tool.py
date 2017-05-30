#!/usr/bin/env python
# -*- coding:utf-8 -*-
import redis
import sys
from PIL import Image
import os

if len(sys.argv[1]) > 0:
    r = redis.Redis(host='127.0.0.1', port=6379,db=1, password="aaa11bbb22")
    jpg = Image.open(sys.argv[1])
    dic = {"width":jpg.size[0],"height":jpg.size[1]}
    videoid = os.path.splitext(sys.argv[1])[0]
    r.hmset(videoid, dic) 
