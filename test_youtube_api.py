from apiclient.discovery import build
import config

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

#assert not config.YOUTUBE_API_KEY, "No YouTube API key specified - please add it to the config.py file"

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=config.YOUTUBE_API_KEY )

search_response = youtube.channels().list(
    part="contentDetails,id",
    maxResults=10,
    forUsername="mindcracknetwork",
    fields="items/contentDetails/relatedPlaylists/uploads,items/id"
  ).execute()

channel_id = search_response['items'][0]['id']
uploads_playlist = search_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

assert channel_id == 'UCAWQEAjn8udSFKN6D4NlqWQ', "Recieved unexpected channel ID"
assert uploads_playlist == 'UUAWQEAjn8udSFKN6D4NlqWQ', "Recieved unexpected uploads playlist ID"

uploaded_videos = youtube.playlistItems().list(
    part="id",
    maxResults=10,
    playlistId=uploads_playlist
  ).execute()
