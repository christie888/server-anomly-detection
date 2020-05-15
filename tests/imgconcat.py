# -*- coding: utf-8 -*-
import sys
import cv2
import os
import datetime
from operator import itemgetter
import schedule
import time

# 引数（第１引数、第２引数）の接頭辞に合致する画像ファイル名同士を左右に結合します
def main(argv):

    argc = len(argv)
    if(argc != 4):
        print ("Usage: python3 imgconcat.py 1 2 RACK1")
        quit()

    left_camno = argv[1]
    right_camno = argv[2]
    prefix = argv[3]

    # current time(毎正時の処理：crontab)
    current_time = datetime.datetime.now().strftime("%Y%m%d%H%M")

    basedir = '/home/pi/workspace/fisheye/data/temp/'
    left_filename = basedir + left_camno + '_' + current_time + '.jpg'
    right_filename = basedir + right_camno + '_' + current_time + '.jpg'

    # image concatinate
    im1 = cv2.imread(left_filename)
    im2 = cv2.imread(right_filename)
    im_h = cv2.hconcat([im1, im2])

    # output directory
    base_path = '/home/pi/workspace/fisheye/data/temp/concat/'
    os.makedirs(base_path, exist_ok=True)
    basename = current_time + '_' + prefix
    cv2.imwrite('{}{}.{}'.format(base_path, basename, 'jpg'), im_h)

    # finally

if __name__ == "__main__":
    main(sys.argv)
