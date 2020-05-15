# -*- coding: utf-8 -*-
import sys
import re
import subprocess
import numpy as np
import cv2
import os
import datetime
import schedule
import time


def main(argv):
    argc = len(argv)
    print(argc)

    if (argc != 3):
        print("Usage: python3 fisheye.py 1 usb-0:1.2:1.0-video-index0")
        quit()


if __name__ == "__main__":
    main(sys.argv)
