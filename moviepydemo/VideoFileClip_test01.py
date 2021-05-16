from moviepy.video.io.VideoFileClip import VideoFileClip
source = r".\resource\jingtian.wmv"
video = VideoFileClip(source)#视频文件加载
print(f"{type(video)}")
# print(f"{video.fl_time()}")
print(f"{video.duration}") # 906.04
print(dir(video))
# exit()
start_time = 100
stop_time = 300
# source = r".\resource\jingtian.wmv"
target = r".\save\clip_video.mp4"
video = video.subclip(int(start_time), int(stop_time))#执行剪切操作
video.to_videofile(target, fps=20, remove_temp=True)#输出文件
