# !/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
import re
import subprocess
import numpy as np
import cv2
import datetime
import tkinter
#import matplotlib
#import matplotlib.pyplot as plt
from tkinter import messagebox

def createUndistortImage(camra_para):
    # argument check
    print("画像を撮影、歪み補正する")

    undistort_image =""
    """
    camera_no = camra_para["para_no"]
    devid = camra_para["bus_no"]
    devid = devid.replace('-', ':')
    devid = devid.replace('.', ':')

    # device number derivation
    cmd = "ls -al /dev/v4l/by-path"
    ret = subprocess.check_output(cmd.split()).decode('utf-8')
    list = ret.splitlines()
    for item in list:
        item = item.replace('-', ':')
        item = item.replace('.', ':')
        m = re.search(devid, item)
        if m:
            rval = item.rsplit(':> ::/::/', 1)[1]
            idx = rval.replace('video', '')
            print(idx)
    video_input = cv2.VideoCapture(int(idx))
    video_input.set(cv2.CAP_PROP_FRAME_WIDTH, 1600) # カメラ画像の横幅を1366に設定
    video_input.set(cv2.CAP_PROP_FRAME_HEIGHT, 1200) # カメラ画像の縦幅を768に設定
    video_input.set(cv2.CAP_PROP_FPS, 10)
    if (video_input.isOpened() == False):
        exit()

    param_path = '/home/pi/workspace/undistort/param/' + camera_no + '/'
    camera_mat, dist_coef = [], []
    camera_mat = np.loadtxt(param_path + 'K.csv', delimiter=',')
    dist_coef = np.loadtxt(param_path + 'd.csv', delimiter=',')
    print("K = \n", camera_mat)
    print("d = ", dist_coef.ravel())

    # 歪み補正画像表示
    dir_path = '/home/pi/workspace/undistort/data/temp/'
    ext = 'jpg'
    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, camera_no)

    ret, frame = video_input.read()
    undistort_image = cv2.undistort(frame, camera_mat, dist_coef)
    cv2.imwrite('{}_{}.{}'.format(base_path, datetime.datetime.now().strftime('%Y%m%d%H%M'), ext), undistort_image)
    video_input.release()
    cv2.destroyAllWindows()
    return 
    """
    return undistort_image