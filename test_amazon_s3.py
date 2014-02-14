import config
from amazon import Bucket

bucket = Bucket('egranlund.podcast')

def test_s3_read_write():
  test_file = "test.tst"
  test_string = "This is a test of Amazon Bucket functionality"

  assert bucket.get_file( test_file ) == None, "Test file already exists"

  # Create the test file, and make sure it's public readable
  bucket.upload_string( test_string, test_file )

  # TODO: Test public read ability

  # Try to find the file we just created
  assert bucket.get_file( test_file ),"Test file doesn't exist on Bucket!"

  # Remove the test file
  bucket.delete_file( test_file )
  assert bucket.get_file( test_file ) == None, "Unable to delete Test file"
