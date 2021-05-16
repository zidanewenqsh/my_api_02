#!/D/MySoft/Python/Python38/python

#/D/Soft/Python/Python38/python

import sys
import os
import torch
import argparse
from tool.utils import makedir
from base.baseai3 import BaseNet
class ED:
    def __init__(self, srclist, dstdir='./', endlist=None, excudelist=None):
        parser = argparse.ArgumentParser(description="base class for network training")
        # parser.add_argument("-s", "--src", type=str, default=None, help="src path")
        # parser.add_argument("-t", "--dst", type=str, default=None, help="dst path")
        # parser.add_argument("-i", "--index", type=int, default=1, help="path index")
        parser.add_argument("-e", "--encode", type=int, default=0, help="path index")
        parser.add_argument("-d", "--decode", type=int, default=0, help="path index")
        self.args = parser.parse_args()
        self.datadict = {}
        self.dstdir = os.path.abspath(dstdir).replace("\\", '/')
        self.srclist = srclist

        self.dictpath = r"C:\Users\wen\Desktop\a\a.tor".replace("\\",'/')
        # if os.path.exists(self.dictpath):
        #     self.datadict = torch.load(self.dictpath)

        self.isencode = self.args.encode
        self.isdecode = self.args.decode
        # if os.path.isdir(self.srcpath):

        # if not os.path.exists(self.dstpath) or not os.path.isdir(self.dstpath):
        #     print("dstpath error")
        #     exit(-1)
        # print(os.path.abspath(self.srcpath))
        # print(os.path.abspath(self.dstpath))
        # self.index = self.args.index
        self.excludelist = [] if (None==excudelist) else excudelist
        self.endlist = [] if (None==endlist) else endlist

    def encodefile(self, filepath, index=1, save=True):
        pathlist = filepath.split('/')
        newpath = '/'.join(pathlist[index:])
        # print("newpath", newpath)
        with open(filepath, 'rb') as f:
            torchdata = f.readlines()
            self.datadict[newpath]=torchdata
        if save:
            torch.save(self.datadict, self.dictpath)

    # def sameendocedecode(self):

    def decode(self):
        datadict = torch.load(self.dictpath)
        for newpath, filedata in datadict.items():
            savepath = os.path.join(self.dstdir, newpath).replace("\\", "/")
            # if os.path.exists(savepath):
            #     savepath_mtime = os.stat(savepath).st_mtime
            #     filepath_mtime = os.stat(filepath).st_mtime
            #     print('s',savepath, savepath_mtime)
            #     print('f',filepath, filepath_mtime)
            #     if savepath_mtime <= filepath_mtime:
            #         continue
            filedir = os.path.dirname(savepath)
            # print("filedir", filedir)
            makedir(filedir)
            print("savepath",savepath)

            with open(savepath, 'wb') as f:
                f.writelines(filedata)

    def encodedir(self):
        index = len(self.srcpath.split('/'))-1
        if not os.path.isdir(self.srcpath):
            print("srcpath should be dir")
            exit(-1)
        print("encode start")
        print("srcpath", self.srcpath)

        for roots, dirs, files in os.walk(self.srcpath):
            for file in files:
                end = file.split('.')[-1]
                if end in self.excludelist:
                    continue
                if end in self.endlist or len(self.endlist)==0:
                    filepath = os.path.join(roots, file).replace("\\",'/')
                    print("filepath", filepath)
                    self.encodefile(filepath, index)

    def forward(self):
        print(f"Usage: python {sys.path[0]} -s <src> -t <dst> -i <index> -e 1 / -d 1>")
        if self.isencode:
            for srcpath_ in self.srclist:
                self.srcpath = os.path.abspath(srcpath_).replace("\\", '/')
                srcdir = os.path.dirname(self.srcpath).replace("\\", '/')
                srcname = os.path.basename(self.srcpath)

                dstname = srcname if (self.dstdir != srcdir) else f"{srcname}.bak"
                # print("dstname:",dstname)
                dstpath = os.path.join(self.dstdir, dstname)
                if not os.path.isdir(self.dstdir):
                    print(self.dstdir)
                    print("dstdir should be dir")
                    exit(-1)
                self.encodedir()
        if self.isdecode:
            self.decode()

if __name__ == '__main__':
    srclist1 = [r'C:\Users\wen\Desktop\b']
    excludelist1 = ['sh']
    endlist1 = ['py']
    dstdir1=r"C:\Users\wen\Desktop"
    ed = ED(srclist1,dstdir1, endlist1, excludelist1)
    # ed.isencode = 1
    # ed.isdecode = 1
    ed.forward()
