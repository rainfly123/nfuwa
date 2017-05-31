#!/bin/sh 
#curl -F "file=@${1}" http://live.66boss.com/upload/writev2
curl -F "file=@${1}" -F "video=@${2}" "http://fuwa.hmg66.com/api/hidev2?owner=100000320&detail=店内活动&pos=沙县小吃&geohash=113.3-23.08&validtime=1&number=5&type=1&class=1"

