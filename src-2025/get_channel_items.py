import os
import time
import urllib.request
from googleapiclient.discovery import build
from datetime import date
from yt import youtube

from get_playlist_items import get_playlist_items

def get_channel_items(channel_link: str):
    channel_name = channel_link
    channel_id = None
    channel_items_response = None
    channel_items_request = None 

    # channel ID
    if channel_name.startswith("UC") and len(channel_name) >= 20:
        channel_items_request = youtube.channels().list(
            part="snippet,contentDetails,statistics",
            id=channel_name
        )


    # @handle
    if '@' in channel_name:        
        if 'https://www.youtube.com/@' in channel_name:
            channel_name = channel_name.split('https://www.youtube.com/@')[1]

        channel_items_request = youtube.search().list(
            part="snippet",
            forHandle=channel_name,
            maxResults=1
        )


    channel_items_response = channel_items_request.execute()

    print(channel_items_response)

    get_playlist_items(channel_items_response)