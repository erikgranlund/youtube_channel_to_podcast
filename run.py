import os
from youtube import YouTubeChannel
from amazon import Bucket, Transcoder

import jinja2

file_extension = 'mp3'
youtube_channel = 'mindcracknetwork'

s3_bucket = Bucket('egranlund.podcast')
elastic_transcoder = Transcoder()

channel = YouTubeChannel( youtube_channel )

videos = channel.get_uploaded_videos(1)

for video in videos:
  try:
    filename = video.get_audio_filename()

#    video.download_audio( filename )
#    s3_bucket.upload_file( filename )
#    elastic_transcoder.convert_to_mp3( filename, filename[:-3] + file_extension )
#    os.unlink( filename )
 
    video.date = 'Wed, 6 Jul 2005 13:00:00 PDT'
    video.size = s3_bucket.get_size( filename )
    video.podcast_url = s3_bucket.get_url( filename )[:-3] + file_extension

  except AttributeError:
    print "Unable to download '" + video.title + "'"

# Render the podcast
templateLoader = jinja2.FileSystemLoader('.')
env = jinja2.Environment( loader=templateLoader )
template = env.get_template( 'minimal.xml' )

podcast_rss = template.render( { 'channel' : channel, 'videos' : videos } )

# Update the rss.xml file on the S3 Instance
with open( youtube_channel + '.xml', "wb") as fh:
  fh.write(podcast_rss)

s3_bucket.upload_file( youtube_channel + '.xml' )

# Delete the podcast file from the local machine
os.unlink( youtube_channel + '.xml' )
