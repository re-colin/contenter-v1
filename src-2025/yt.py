import os
from googleapiclient.discovery import build

API_KEY = os.environ['YT_API_KEY']
youtube = build('youtube', 'v3', developerKey=API_KEY)