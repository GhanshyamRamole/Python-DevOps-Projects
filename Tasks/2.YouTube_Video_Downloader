from pytube import YouTube

link = input("Enter a YouTube video URL: ")  # Example: https://youtu.be/dQw4w9WgXcQ

yt = YouTube(link)
yt.streams.first().download()

print("Downloaded:", link)
