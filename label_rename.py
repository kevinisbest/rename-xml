import os
import linecache
dirpath ="/home/esa/Documents/python_test/"
for fname in os.listdir(dirpath):
    if os.path.splitext(fname)[-1] =='.xml':
        f=open(fname,'r')
        print(fname)
        count = linecache.getline(fname,4)
        print(count[11:19])
        newfname=count[11:19]
        newfpath="%s/%s"%(dirpath,newfname+'.xml')
        oldfpath="%s/%s"%(dirpath,fname)
        os.rename(oldfpath, newfpath)


f.close()


