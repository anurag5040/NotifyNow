import os

HOME_DIR = os.path.abspath(os.pardir)

Oldpath = HOME_DIR+"\\comp\\Old.txt"
Newpath = HOME_DIR+"\\comp\\New.txt"

if os.path.exists(Oldpath) and os.path.exists(Newpath) :
    print("Success!!!!!")

    OldFileObj = open(Oldpath,mode='r')
    NewFileObj = open(Newpath,mode='r')

    OldList = OldFileObj.read().split('\n')
    NewList = NewFileObj.read().split('\n')

    OldList.sort()
    NewList.sort()

    if OldList == NewList :
        print("Same!!!!!")

    else :
        print("Not Same!!!!!")