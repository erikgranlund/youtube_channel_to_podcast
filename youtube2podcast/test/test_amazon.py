import config
from youtube2podcast.sources.amazon import Bucket, Transcoder

def test_s3_read_write():
  bucket = Bucket('egranlund.podcast')

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

def test_elastic_transcoder():
  elastic_transcoder = Transcoder()

  elastic_transcoder.list_pipelines()[0]['Id'] = config.ET_PIPELINE_ID

  # TODO: Test job submitting?
