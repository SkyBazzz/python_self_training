from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

MIN_IN_HOUR = 60

url = input("Give url: ")

yt = YouTube(url)
yt.streams.get_highest_resolution().download("video")

# example of cutting video
ffmpeg_extract_subclip("original.mp4", 45 * MIN_IN_HOUR + 5.5, 45 * MIN_IN_HOUR + 22, targetname="result.mp4")
