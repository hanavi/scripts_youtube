#!/bin/bash

for fname in /home/james/Dropbox/xfer/youtube/dllist/*.dl
do
  bname=$(basename ${fname})
  echo ${bname}
  cd /home/james/Dropbox/xfer/youtube/dllist/
  ../bin/youtube.py ${bname}
done
