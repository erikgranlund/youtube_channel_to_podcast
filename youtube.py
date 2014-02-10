from apiclient.discovery import build
import config

class YouTubeChannel:
  def __init__(self,channel_username):
    self.channel_username = channel_username

    self.youtube_api = build(config.YOUTUBE_API_SERVICE_NAME, config.YOUTUBE_API_VERSION, developerKey=config.YOUTUBE_API_KEY )

    search_response = self.youtube_api.channels().list(
        part="contentDetails,id,snippet",
        maxResults=10,
        forUsername=channel_username,
        fields="items/contentDetails/relatedPlaylists/uploads,items/id,items/snippet/title,items/snippet/description"
      ).execute()

    channel = search_response['items'][0]

    self.channel_id = channel['id']
    self.channel_title = channel['snippet']['title']
    self.channel_description = channel['snippet']['description']
    self.uploads_playlist = channel['contentDetails']['relatedPlaylists']['uploads']

  def get_uploaded_videos(self,max_results=20):
    videos = []

    video_list_response = self.youtube_api.playlistItems().list(
        part="id,snippet,contentDetails",
        maxResults=max_results,
        playlistId=self.uploads_playlist,
        fields="items/id,items/snippet/title,items/snippet/description,items/contentDetails/videoId"
      ).execute()

    for video in video_list_response['items']:
      videos.push( video['contentDetails']['videoId'] )

    return uploaded_videos


import pafy

class YouTubeVideo:
  def __init__(self,video_id):
    self.id = video_id

    self.url = 'http://www.youtube.com/watch?v=' + self.id


    self.pafy_object = pafy.new(self.url)

    self.title = self.pafy_object.title
    self.author = self.pafy_object.author
    self.description = self.pafy_object.description

  def download(self,filepath=None):
    self.pafy_object.getbest(preftype="mp4").download(filepath)

