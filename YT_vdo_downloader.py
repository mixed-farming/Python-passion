#pip install pytube
from pytube import YouTube
import os
from pathlib import Path

link = input("Enter YouTube video link here: ")

url = YouTube(link)

print("\nDownloading...Please wait!")

video = url.streams.get_highest_resolution()

# path_to_download_folder = str(os.path.join(Path.home(), "Downloads")) # -> In the downloads folder
path_to_download_folder = "D:/"
video.download(path_to_download_folder)
print("\nDownload complete :)\nYou can find the video at : ",path_to_download_folder)

'''
Initializing 'link' variable as a list and enclosing the YouTube() method & url object inside a loop,
mutiple videos can be downloaded back-to-back.
'''
