import os
from youtube import YouTubeChannel
from amazon import Bucket, Transcoder

s3_bucket = Bucket('egranlund.podcast')
elastic_transcoder = Transcoder()

channel = YouTubeChannel('mindcracknetwork')

for video in channel.get_uploaded_videos(1):
  try:
    filename = video.get_audio_filename()
    
    print "Downloading video"
    video.download_audio( filename )
    print "Uploading file"
    s3_bucket.upload_file( filename )
    print "Transcoding file"
    elastic_transcoder.convert_to_mp3( filename, filename[:-3] + 'mp3' )

    print "deleting file"
    os.unlink( filename )

  except AttributeError:
    print "Unable to download '" + video.title + "'"
