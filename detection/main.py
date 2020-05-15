# -*- coding: utf-8 -*-
import sys
import re
import subprocess
import numpy as np
import cv2
import os.path
import datetime
import schedule
import time
import csv
import pandas as pd
import undistort
import anomly_detect

def readCameCSV(camera_para_file):
    print("****",camera_para_file,"から、カメラパラメータを読み込み")
    cama_df=pd.read_csv(camera_para_file, sep=',')
    return cama_df


def save_frame_camera(image, camera_no, dir_path, ext='jpg'):
    print("****写真記録を残す")
    """
    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, str(camera_no))
    cv2.imwrite('{}_{}.{}'.format(base_path, datetime.datetime.now().strftime('%Y%m%d%H%M'), ext), image)
    """
    pass

def writeToFile(result,rak_no,server_no):
    records_path = "../data/records"
    print("****",records_path,"のファイルに結果を書き込む")
    pass

def sendMail():
    print("****メールで通知")
    pass

def resultProcess(result,rak_no,server_no):
    print("結果を処理する")
    result_flag=True
    writeToFile(result, rak_no, server_no)
    sendMail()
    """
    if True:
        print("正常、ファイルに書き込む")
        writeToFile(result,rak_no,server_no)
    else:
        print("異常あり、アラート出す。")
        sendMail()
    
    """



if __name__ == "__main__":
    camera_para_path= "../data/camera_para/"
    dir_path = "../data/temp/"

    camera_para_file=os.path.join(camera_para_path, "camera_loc.csv")

    cama_df=readCameCSV(camera_para_file)
    #print(cama_df)
    for index, row in cama_df.iterrows():
        print("bus番号",row["bus_no"],"カメラ番号:",row["camera_no"],"ラック番号:",row["rak_no"],"サーバ番号:",row["server_no"])
        undistort_image =undistort.createUndistortImage(row)

        # いろいろな検知方法を試す
        result,image = anomly_detect.find_rect_of_target_color(undistort_image)


        #写真保存
        save_frame_camera(image, row["camera_no"], dir_path, ext='jpg')

        # 検知結果を処理する
        resultProcess(result, row["rak_no"], row["server_no"])


    #for i in range(3):
        #time.sleep(1)
        #print(i)


