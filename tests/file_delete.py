# -*- coding: utf-8 -*-
import sys
import os
import datetime

def main(argv):

    basedir = '/home/pi/workspace/fisheye/data/temp/'
    #
    for dirpath, dirnames, filenames in os.walk(basedir):
        for file in filenames:
            curpath = os.path.join(dirpath, file)
            file_modified = datetime.datetime.fromtimestamp(os.path.getmtime(curpath))
            if datetime.datetime.now() - file_modified > datetime.timedelta(hours=24):
                print(curpath)
                os.remove(curpath)
    #
    for dirpath, dirnames, filenames in os.walk(basedir + 'concat'):
        for file in filenames:
            curpath = os.path.join(dirpath, file)
            file_modified = datetime.datetime.fromtimestamp(os.path.getmtime(curpath))
            if datetime.datetime.now() - file_modified > datetime.timedelta(hours=24):
                print(curpath)
                os.remove(curpath)

if __name__ == "__main__":
    main(sys.argv)
