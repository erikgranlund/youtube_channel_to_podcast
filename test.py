import pafy

url = 'http://www.youtube.com/watch?v=I5XagzU9seA'

youtube_video = pafy.new(url)

print youtube_video

video = youtube_video.getbest(preftype="mp4")
video.download()
