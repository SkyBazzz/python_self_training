from pytube import YouTube

url = input("Give url: ")

yt = YouTube(url)
yt.streams.get_highest_resolution().download("youtube_downloader/video")
