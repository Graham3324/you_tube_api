import constants
from googleapiclient.discovery import build

youtube = build('youtube', 'v3', developerKey=constants.youtube_APIKEY)

