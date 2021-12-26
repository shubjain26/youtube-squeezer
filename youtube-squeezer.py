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
    url = input("enter the link: ")
    save_path = "downloads"
    print("file is being downloaded to downloads directory")
    downloadYouTube(url,save_path)
