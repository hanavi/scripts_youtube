#!/usr/bin/env python3

import os
import sys
import time
import subprocess
import gnupg
import shutil

myfpr = "12E7C7C78A4D42132F9641233A3800D7B0682446"
myfpr = "FEC14CAE719278D4B4CFA49D07436D570209D4AE"

dl_dir = "/home/james/Downloads/youtube/dl/"
xfer_dir = "/home/james/Dropbox/xfer/pole_linux"

def check_file(fname):

    sig_file = "{}.asc".format(fname)
    if os.path.isfile(sig_file):
        fd = open(sig_file,"rb")
        gpg = gnupg.GPG(gnupghome="/home/james/.gnupg")
        ver = gpg.verify_file(fd,fname)
        print(ver.fingerprint)
        print(myfpr)

        if ver:
            if ver.fingerprint == myfpr:
                return True

    print("here")

    return False

def get_vname_from_file(fname):
    data = open(fname).readlines()

    file_list = []
    for line in data:
        file_list.append(line.strip())
    return file_list

def download_videos(flist):
    for fname in flist:
        print("Downloading File: {}".format(fname))
        subprocess.call(["/home/james/Dropbox/xfer/youtube/bin/yt.sh",fname])

def mv_file(fname,dl_fname):

    sig_fname = "{}.asc".format(fname)
    new_sig_fname = "{}.asc".format(dl_fname)
    shutil.move(fname,dl_fname)
    shutil.move(sig_fname,new_sig_fname)

if __name__ == '__main__':

    fname = sys.argv[1]

    if check_file(fname):
        dl_fname = "{}{}".format(dl_dir,fname)
        mv_file(fname,dl_fname)
        flist = get_vname_from_file(dl_fname)
        download_videos(flist)





