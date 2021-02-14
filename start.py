import constants
from googleapiclient.discovery import build

youtube = build("youtube", "v3", developerKey=constants.youtube_APIKEY)

request = youtube.channels().list(part="statistics", forUsername="schefer5")

response = request.execute()

print(response)

print("Got here")