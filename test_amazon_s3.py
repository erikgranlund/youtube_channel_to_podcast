import boto
import config
import boto

from boto.s3.connection import S3Connection
from boto.s3.key import Key

def get_connection():
  connection = S3Connection( config.S3_ACCESS_KEY_ID, config.S3_SECRET_ACCESS_KEY )
  bucket = connection.get_bucket('egranlund.podcast')
  return bucket

def test_s3_read_write():
  bucket = get_connection()

  test_file = "test.tst"
  test_string = "This is a test of Amazon S3 functionality"

  assert bucket.get_key( test_file ) == None, "Test file already exists"

  key = Key(bucket)
  key.key = test_file
  key.set_contents_from_string( test_string )
  key.set_acl('public-read')



  bucket = get_connection()
  assert bucket.get_key( test_file ),"Test file doesn't exist on S3!"

  bucket.delete_key( test_file )
  assert bucket.get_key( test_file ) == None, "Unable to delete Test file"
