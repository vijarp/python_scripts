import pytube

# Get the video URL from the user
video_url = input("Enter the YouTube video URL: ")

# Create a YouTube object
yt = pytube.YouTube(video_url)

# Get the highest resolution stream available
video = yt.streams.get_highest_resolution()

# Download the video
try:
    video.download()  # Downloads to current working directory by default
    print("Video downloaded successfully!")
except Exception as e:
    print("Error downloading video:", e)