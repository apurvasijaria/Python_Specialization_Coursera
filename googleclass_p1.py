import sys
import os

def Lit(dir):
    filenames=os.listdir(dir)
    for filename in filenames:
        path=os.path.join(dir,filename)
        print path
        print os.path.abspath(path)