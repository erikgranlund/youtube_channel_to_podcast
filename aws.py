import config

from boto.s3.connection import S3Connection
from boto.s3.key import Key

class S3:
  def __init__( self, bucket_name ):
    self.connection = S3Connection( config.S3_ACCESS_KEY_ID, config.S3_SECRET_ACCESS_KEY )
    self.bucket = self.connection.get_bucket( bucket_name )

  def upload_file( self, filename, target_filename ):
    key = Key(self.bucket)
    key.key = target_filename
    key.set_contents_from_filename( filename )
    key.set_acl('public-read')

  def upload_string( self, string, target_filename ):
    key = Key(self.bucket)
    key.key = target_filename
    key.set_contents_from_string( string )
    key.set_acl('public-read')

  def get_file( self, filename ):
    return self.bucket.get_key( filename )

  def delete_file( self, filename ):
    return self.bucket.delete_key( filename )
