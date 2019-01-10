#!/bin/bash

DLDIR="/home/james/Dropbox/xfer/pole_linux"
YT="/usr/local/bin/youtube-dl -f mp4"

cd ${DLDIR}
${YT} $1

