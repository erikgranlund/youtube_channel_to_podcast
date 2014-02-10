import pafy
import os

url = 'http://www.youtube.com/watch?v=SmnkYyHQqNs'
youtube_video = pafy.new(url)

def test_video_download():
  test_filename = "test.mp4"


  print youtube_video

  if os.path.isfile( test_filename ):
    assert False, "Test file " + test_filename + " already exists! Unable to run the test because I don't want to overwrite an existing file"

  video = youtube_video.getbest(preftype="mp4")
  video.download(filepath=test_filename)

  assert os.path.isfile( test_filename )

  os.unlink( test_filename )

  assert os.path.isfile( test_filename ) == False, "Was not able to delete the test file"

def test_video_metadata():
  expected_name = 'YouTube Rewind 2011'
  expected_description_contains = 'http://www.youtube.com/rewind'
  expected_author = 'YouTube Spotlight'

  assert youtube_video.title == expected_name
  assert youtube_video.author == expected_author
  assert expected_description_contains in youtube_video.description
