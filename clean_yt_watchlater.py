#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import pyautogui
import sys
from time import sleep

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("working")


def remove_item():

    pyautogui.moveTo(1200, 229)
    pyautogui.click()
    sleep(.5)
    pyautogui.moveTo(1117, 326, .5)
    pyautogui.click()

def main():
    """ Main code block """

    # INIT
    pyautogui.moveTo(1200, 229)
    pyautogui.click()

    count = 1
    if len(sys.argv) == 2:
        count = int(sys.argv[1])

    for i in range(count):
        sleep(1)
        remove_item()


if __name__ == "__main__":
    main()

