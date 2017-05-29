#!/bin/sh
pid=/var/run/snap
if [ -f $pid ]
   then
   echo "running"
   exit 0
fi

touch $pid

    files=$(ls *.mp4 -t | head -10)
    for file in $files
        do
        jpg=${file%.*}.jpg
        if [ ! -f $jpg ]
        then
            /usr/local/bin/ffmpeg -loglevel quiet -i $file -vframes 1 -f image2 -y $jpg
            nohup qrsctl put -c wsim fuwa/$file   $file &
        fi
    done
    sleep 1
    files=$(ls *.mov -t | head -10)
    for file in $files
        do
        jpg=${file%.*}.jpg
        if [ ! -f $jpg ]
        then
            /usr/local/bin/ffmpeg -loglevel quiet -i $file -vframes 1 -f image2 -y $jpg
            nohup qrsctl put -c wsim fuwa/$file   $file & 
        fi
    done

rm $pid
