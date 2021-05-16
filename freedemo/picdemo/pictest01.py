#!/e/Soft/Python/Python38/python
# -*- coding: utf-8 -*- #
# ------------------------------------------------------------------
# @File Name:        pictest01.py
# @Author:           wen
# @Version:          ver0_1
# @Created:          2021/5/11 20:13
# @Description:      Main Function:    xxx
# Function List:     hello() -- print helloworld
# History:
#       <author>    <version>   <time>      <desc>
#       wen         ver0_1      2020/12/15  xxx
# ------------------------------------------------------------------
import os
import numpy as np
import torch
import logging
import argparse
import shutil
import cv2
import time
import threading
import multiprocessing
from pathlib import Path
from tqdm import tqdm
from matplotlib import pyplot as plt

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    torch.set_printoptions(precision=2, threshold=np.inf, sci_mode=False)
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', type=str, default=r'', help='')
    parser.add_argument('-b', type=int, default=0, help='')
    parser.add_argument('-c', nargs='+', type=int, default=[0, 1], help='')
    parser.add_argument('-d', action='store_true', help='')
    parser.add_argument('-e', nargs='?', const=True, default=False, help='')
    opt = parser.parse_args()
    basepath = Path(r"J:\视频\眼镜蛇王\备份\反应文献\spectial\sp\a\Syukou-club\OSK 放尿")
    savedir = Path("./save")
    savedir.mkdir(parents=True, exist_ok=True)
    for subdir in basepath.iterdir():
        # print(subdir)
        imglist = list(subdir.glob("*.jpg"))
        # print(len(imglist))
        # print(imglist[-1])
        # imgpath = imglist[-1]
        pbar =tqdm(enumerate(imglist), total=len(imglist))
        for i, imgpath in pbar:
            savename = rf"{imgpath.parent.name}_{imgpath.name}"
            # print(savename)
            savepath = savedir/savename
            if not savepath.exists():shutil.copy(str(imgpath), str(savepath))
            # exit()