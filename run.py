import os
from youtube2podcast.sources.youtube import YouTubeChannel
from youtube2podcast.sources.amazon import Bucket, Transcoder

import jinja2

import pickle

debug = False

# --
file_extension = 'mp3'
youtube_channel = 'mindcracknetwork'
# --

s3_bucket = Bucket('egranlund.podcast')
elastic_transcoder = Transcoder()

channel = YouTubeChannel( youtube_channel )

# Pickle input stuff
try:
  pickle_file = open( 'data.pkl', 'rb' )
  previous_videos = pickle.load( pickle_file )
  pickle_file.close()
except:
  previous_videos = {}

# Grab and iterate through all of the videos on the channel
videos = channel.get_uploaded_videos(5)

for video in videos:
  filename = videos[video].get_audio_filename()

  if videos[video].id in previous_videos:
    print "Not downloading/uploading video with id of " + videos[video].id + ": Record of video already exists in Pickle file"
    videos[video] = previous_videos[video]
    del previous_videos[video]

  else:
    try:
      if s3_bucket.get_file( filename ):
        print "Not downloading/uploading video with id of " + videos[video].id + ": File already exists on S3"
      elif debug == False:
        videos[video].download_audio( filename )
        s3_bucket.upload_file( filename )
        elastic_transcoder.convert_to_mp3( filename, filename[:-3] + file_extension )
        os.unlink( filename )
    except AttributeError:
      print "Unable to download video with id of '" + videos[video].id + "'"
    else:
      videos[video].size = s3_bucket.get_size( filename[:-3] + file_extension )
      videos[video].podcast_url = s3_bucket.get_url( filename )[:-3] + file_extension

  # Delete any extra m4a files
  #for existing_file in s3_bucket.list_files( filename[:-3] ):
  #  if existing_file and existing_file[-3:] != file_extension and debug == False:
  #    s3_bucket.delete_file( existing_file )

# Dump the pickle file
output = open( 'data.pkl', 'wb' )
pickle.dump( videos, output )
output.close()

# Render the podcast
package_loader=jinja2.PackageLoader('youtube2podcast', 'templates')
env = jinja2.Environment( loader=package_loader, autoescape=True )
template = env.get_template( 'minimal.xml' )

print "Generating podcast XML file"
podcast_rss = template.render( { 'channel' : channel, 'videos' : videos } )

# Update the rss.xml file on the S3 Instance
print "Uploading podcast XML file"
with open( youtube_channel + '.xml', "wb") as fh:
  fh.write(podcast_rss)

s3_bucket.upload_file( youtube_channel + '.xml' )

# Delete the podcast file from the local machine
os.unlink( youtube_channel + '.xml' )

print "Done"
