from apiclient.discovery import build
import config

class YouTubeChannel:
  def __init__(self,channel_username):
    self.channel_username = channel_username

    self.youtube_api = build(config.YOUTUBE_API_SERVICE_NAME, config.YOUTUBE_API_VERSION, developerKey=config.YOUTUBE_API_KEY )

    search_response = self.youtube_api.channels().list(
        part="contentDetails,id",
        maxResults=10,
        forUsername=channel_username,
        fields="items/contentDetails/relatedPlaylists/uploads,items/id"
      ).execute()

    self.channel_id = search_response['items'][0]['id']
    self.channel_title = '' # TODO
    self.channel_description = '' # TODO
    self.uploads_playlist = search_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

  def get_uploaded_videos(self,max_results=20):
    uploaded_videos = self.youtube_api.playlistItems().list(
        part="id,snippet,contentDetails",
        maxResults=max_results,
        playlistId=self.uploads_playlist,
        fields="items/id,items/snippet/title,items/snippet/description,items/contentDetails/videoId"
      ).execute()

    return uploaded_videos
