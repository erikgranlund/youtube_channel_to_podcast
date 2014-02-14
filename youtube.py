from apiclient.discovery import build
import config

class YouTubeChannel:
  def __init__(self,username):
    self.username = username

    self.youtube_api = build(config.YOUTUBE_API_SERVICE_NAME, config.YOUTUBE_API_VERSION, developerKey=config.YOUTUBE_API_KEY )

    search_response = self.youtube_api.channels().list(
        part="contentDetails,id,snippet",
        maxResults=10,
        forUsername=username,
        fields="items/contentDetails/relatedPlaylists/uploads,items/id,items/snippet/title,items/snippet/description"
      ).execute()

    channel = search_response['items'][0]

    self.id = channel['id']
    self.title = channel['snippet']['title']
    self.description = channel['snippet']['description']
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
      videos.append( YouTubeVideo( video['contentDetails']['videoId'] ) )

    return videos


import pafy

class YouTubeVideo:
  def __init__(self,video_id):
    self.id = video_id

    self.url = 'http://www.youtube.com/watch?v=' + self.id


    self.pafy_object = pafy.new(self.url)

    self.title = self.pafy_object.title
    self.author = self.pafy_object.author
    self.description = self.pafy_object.description

  def get_audio_filename(self):
    return self.id+'.m4a'

  def get_video_filename(self):
    return self.id+'.mp4'

  def download_audio(self,filepath=None):
    if filepath == None:
      filepath = self.get_audio_filename()

    self.pafy_object.getbestaudio(preftype="m4a").download(filepath,quiet=True)

  def download_video(self,filepath=None):
    if filepath == None:
      filepath = self.get_video_filename()

    self.pafy_object.getbest(preftype="mp4").download(filepath,quiet=True)

