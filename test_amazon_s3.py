import config
from aws import S3

from boto.s3.key import Key

s3 = S3('egranlund.podcast')

def test_s3_read_write():
  bucket = s3.bucket

  test_file = "test.tst"
  test_string = "This is a test of Amazon S3 functionality"

  assert bucket.get_key( test_file ) == None, "Test file already exists"

  # Create the test file, and make sure it's public readable
  s3.upload_string( test_string, test_file )

  # TODO: Test public read ability

  # Try to find the file we just created
  assert s3.get_file( test_file ),"Test file doesn't exist on S3!"

  # Remove the test file
  s3.delete_file( test_file )
  assert s3.get_file( test_file ) == None, "Unable to delete Test file"
