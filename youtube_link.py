#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re
import pexpect
import os
import subprocess
from time import sleep


def clean_url(url):
    url = url.split("&")[0]
    return url


def get_url_from_clipboard():
    if sys.platform == "darwin":
        p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    else:
        p = subprocess.Popen(['xsel', '-b'], stdout=subprocess.PIPE)
    url = p.communicate()[0].decode().strip()
    if verify_url(url):
        url = clean_url(url)
        return url
    return None


def verify_url(url):
    r = re.compile("https://www.youtube.com/.*")
    if r.match(url):
        print("URL verified")
        return True
    else:
        print("Skipping non-url")
        return False


def send_url(url):
    print("Sending url: {}".format(url))
    p = pexpect.spawn("ssh homelocal")
    print("logging in")
    p.expect(".*james@homeserver:.*")
    print("connected")
    p.sendline("cd /media/disk1/files/youtube/music_test")
    p.expect(".*james@homeserver:.*")
    print("downloading")
    p.sendline("youtube-dl {}".format(url))
    p.expect(".*james@homeserver:.*",timeout=300)
    print("done")


def clear_clipboard():
    if sys.platform == "darwin":
        os.system("echo NONE |pbcopy")
    else:
        os.system("echo NONE |xsel -b")


def main():
    """ Main code block """

    try:
        while True:
            url = get_url_from_clipboard()
            if url is not None:
                send_url(url)
                clear_clipboard()
            sleep(10)
    except KeyboardInterrupt as e:
        print("\nExiting")
        sys.exit()


if __name__ == "__main__":
    main()
