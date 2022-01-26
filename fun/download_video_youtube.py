import pytube


url = input("Give url: ")

youtube = pytube.YouTube(url)
video = youtube.streams.get_highest_resolution()
video.download()
