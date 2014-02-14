from youtube import YouTubeChannel

channel = YouTubeChannel('mindcracknetwork')

for video in channel.get_uploaded_videos(10):
  try:
    video.download_audio()
  except AttributeError:
    print "Unable to download '" + video.title + "'"
