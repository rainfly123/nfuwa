#!/bin/sh 
#curl -F "file=@${1}" http://live.66boss.com/upload/writev2
curl -F "file=@${1}" -F "video=@${2}" "http://fuwa2.66boss.com:9090/api/hide?owner=100000076&detail=ddd&fuwagid=fuwa_c_100&pos=dd&geohash=102.23-33.22"

