import youtube2podcast.config

from boto.s3.connection import S3Connection
from boto.s3.key import Key

import boto.elastictranscoder

class Bucket:
  def __init__( self, bucket_name ):
    self.connection = S3Connection()
    self.bucket = self.connection.get_bucket( bucket_name )

  def upload_file( self, filename, target_filename=None ):
    if target_filename == None:
      target_filename = filename

    key = Key(self.bucket)
    key.key = target_filename
    key.set_contents_from_filename( filename )
    key.set_acl('public-read')

  def upload_string( self, string, target_filename ):
    key = Key(self.bucket)
    key.key = target_filename
    key.set_contents_from_string( string )
    key.set_acl('public-read')

  def list_files( self, prefix=None ):
    files = []

    for item in self.bucket.list(prefix):
      files.append( item.key )

    return files

  def get_file( self, filename ):
    return self.bucket.get_key( filename )

  def delete_file( self, filename ):
    return self.bucket.delete_key( filename )

  def get_url( self, filename ):
    key = self.bucket.get_key( filename )

    if key:
      return key.generate_url(expires_in=-1, query_auth=False, force_http=True)
    else:
      return None

  def get_size( self, filename ):
    key = self.bucket.get_key( filename )

    if key:
      return key.size
    else:
      return None

class Transcoder:
  def __init__( self ):
    self.connection = boto.elastictranscoder.connect_to_region( youtube2podcast.config.ET_REGION )
    self.outputs = {}

  def convert_to_mp3( self, input_filename=None, output_filename=None ):
    if input_filename and output_filename:
      self.add_input_file( input_filename, output_filename )

    for input_file in self.outputs:
      self.connection.create_job( youtube2podcast.config.ET_PIPELINE_ID, input_name = { 'Key' : input_file }, outputs = [self.outputs[input_file]] )
    

  def add_input_file( self, input_filename, output_filename ):
    # could only find this format documented here: http://docs.aws.amazon.com/elastictranscoder/latest/developerguide/create-job.html
    self.outputs[input_filename] = { 'Key' : output_filename, 'PresetId' : youtube2podcast.config.ET_PRESET_ID } 

  def list_pipelines( self ):
    return self.connection.list_pipelines()['Pipelines']
