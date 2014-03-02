from youtube2podcast.sources.youtube import YouTubeVideo
import os

id = 'SmnkYyHQqNs'
test_object = YouTubeVideo( id )

def test_audio_download():
  test_filename = "test.ogg"

  print test_object.title

  if os.path.isfile( test_filename ):
    assert False, "Test file " + test_filename + " already exists! Unable to run the test because I don't want to overwrite an existing file"

  test_object.download_audio( test_filename )

  assert os.path.isfile( test_filename )

  os.unlink( test_filename )

  assert os.path.isfile( test_filename ) == False, "Was not able to delete the test file"

def test_video_metadata():
  expected_name = 'YouTube Rewind 2011'
  expected_description_contains = 'http://www.youtube.com/rewind'
  expected_author = 'YouTube Spotlight'

  assert test_object.title == expected_name
  assert test_object.author == expected_author
  assert expected_description_contains in test_object.description
