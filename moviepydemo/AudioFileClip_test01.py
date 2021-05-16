# 1、使用moviepy模块 提取视频中的音频文件
from moviepy.editor import AudioFileClip

my_audio_clip = AudioFileClip(r".\resource\jingtian.wmv")
print(type(my_audio_clip))  # <class 'moviepy.audio.io.AudioFileClip.AudioFileClip'>

#  提取视频中的音频文件  m4v,mp3等音频格式也是支持的
my_audio_clip.write_audiofile(r".\save\extract_audio.wav")
'''
MoviePy - Writing audio in ./extract_audio.wav
MoviePy - Done.
'''
