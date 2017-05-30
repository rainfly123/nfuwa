#!/usr/bin/env python
#-*- coding: utf-8 -*- 
import geopy.distance

#latitude,longtitude
def getdistance(a, b):
    return geopy.distance.vincenty(a, b).m
