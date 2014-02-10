from youtube import YouTubeChannel  
import config

def test_api_key():
  assert config.YOUTUBE_API_KEY, "No YouTube API key specified - please add it to the config.py file"

def test_query_channel_information():
  test_object = YouTubeChannel( "mindcracknetwork" )

  assert test_object.channel_id == 'UCAWQEAjn8udSFKN6D4NlqWQ', "Recieved unexpected channel ID"
  assert test_object.uploads_playlist == 'UUAWQEAjn8udSFKN6D4NlqWQ', "Recieved unexpected uploads playlist ID"

def test_query_channel_videos():
  test_object = YouTubeChannel( "mindcracknetwork" )
  uploaded_videos = test_object.get_uploaded_videos()

  try:
    for video in uploaded_videos['items']:
      assert video['snippet']['title']
      assert video['contentDetails']['videoId']
  except KeyError:
    assert False, "Missing id, snippet.title or contentDetails.videoId"
