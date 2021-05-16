#!/e/Soft/Python/Python38/python
# -*- coding: utf-8 -*- #
# ------------------------------------------------------------------
# @File Name:        librosatest01.py
# @Author:           wen
# @Version:          ver0_1
# @Created:          2021/5/9 21:42
# @Description:      Main Function:    xxx
# Function List:     hello() -- print helloworld
# History:
#       <author>    <version>   <time>      <desc>
#       wen         ver0_1      2020/12/15  xxx
# ------------------------------------------------------------------
# 2、使用librosa分析音频
import librosa
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision=2)
# 加载音频文件
audio, freq = librosa.load(r".\save\extract_audio.wav")
print(f"audio: {audio[5119245:5119285]} and audio shape: {audio.shape}\nfreq: {freq}")
print(f"audio type: {type(audio)}\nfreq type: {type(freq)}")
print(f"{np.max(audio)=}")
print(f"{np.argmax(audio)=}")
time = len(audio) / freq
print(time)  # 94.3
'''
audio: [ 0.          0.          0.         ... -0.00216522 -0.00011788
 -0.00167476] and audio shape: (2079315,)
freq: 22050
audio type: <class 'numpy.ndarray'>
freq type: <class 'int'>


# 上面的这段音频 采样点共：2079315   采样频率为：22050
这段音频的时长为：2079315 / 22050 = 94.3   因此这段音频的时长约为94秒
也就是每秒采样 22050个数据
'''


time = np.arange(0, len(audio)) / freq
# np.arange(0, len(audio))  = (0,1,2,3,...,2079314)
print(time.shape)  # (2079315,)
print(np.min(time), np.max(time))  # 94.29995464852608  0.0

fig, ax = plt.subplots()
ax.plot(time, audio)
print(f"{len(time)=}, {len(audio)=}")
ax.set(xlabel="Time(s)", ylabel="Sound Amplitude")
plt.show()
plt.clf()
# 可以使用librosa 库的工具来分析，可以修掉音频首尾的其他信息，画信号强度图的方式如下
import librosa.display
# 其实绘制的点一共有2079315个，但是由于我们的时间范围是0-94,因此音频信号看起来很拥挤
audio, _ = librosa.effects.trim(audio)
librosa.display.waveplot(audio, sr=freq)
plt.show()