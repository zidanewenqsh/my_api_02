#!/e/Soft/Python/Python38/python
# -*- coding: utf-8 -*- #
# ------------------------------------------------------------------
# @File Name:        CompositeVideoClip_test01.py
# @Author:           wen
# @Version:          ver0_1
# @Created:          2021/5/9 22:45
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

from moviepy.editor import*
source = r".\resource\jingtian.wmv"
target = r".\save\clip_video2.mp4"
# 剪辑50-60秒的音乐 00:00:50 - 00:00:60
video =CompositeVideoClip([VideoFileClip(source).subclip(50,60)])
# 写入剪辑完成的音乐
video.write_videofile(target)
