from pytube import YouTube
import os

# Specify the URL of the video to download
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Create a YouTube object
yt = YouTube(url)

# Get the first available video stream
stream = yt.streams.first()

# Specify the folder to save the video in
folder = "videos"

# Create the folder if it doesn't exist
if not os.path.exists(folder):
    os.makedirs(folder)

# Download the video into the folder
stream.download(output_path=folder)
