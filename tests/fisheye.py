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

# 引数（第１引数、第２引数）カメラ番号
def main(argv):

    argc = len(argv)
    print(argc)

    if(argc != 3):
        print ("Usage: python3 fisheye.py 1 usb-0:1.2:1.0-video-index0")
        quit()

    camera_no = argv[1]
    devid = argv[2]
    devid = devid.replace('-', ':')
    devid = devid.replace('.', ':')

    cmd = "ls -al /dev/v4l/by-path"
    ret = subprocess.check_output(cmd.split()).decode('utf-8')
    list = ret.splitlines()
    for item in list:
        item = item.replace('-', ':')
        item = item.replace('.', ':')
        m = re.search(devid, item)
        #m = re.search(r"usb-0:1.2:1.0-video-index0", item)
        if m:
            rval = item.rsplit(':> ::/::/', 1)[1]
            idx = rval.replace('video', '')
            print(idx)

    save_frame_camera(camera_no, idx)

def save_frame_camera(camera_no, idx, dir_path='/home/pi/workspace/fisheye/data/temp/', ext='jpg'):

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, camera_no)

    video_input = cv2.VideoCapture(int(idx))
    video_input.set(cv2.CAP_PROP_FRAME_WIDTH, 1600)
    video_input.set(cv2.CAP_PROP_FRAME_HEIGHT, 1200)
    video_input.set(cv2.CAP_PROP_FPS, 10)
    if (video_input.isOpened() == False):
        exit()

    # 画像取得
    ret, frame = video_input.read()
    cv2.imwrite('{}_{}.{}'.format(base_path, datetime.datetime.now().strftime('%Y%m%d%H%M'), ext), frame)
    video_input.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
