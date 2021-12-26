# importing the module
import os
from pytube import YouTube

def downloadYouTube(videourl, path):

    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)

if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=r3PqnITCfY0"
    save_path = "downloads"
    downloadYouTube(url,save_path)
