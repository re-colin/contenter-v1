import os
import time
import urllib.request
from googleapiclient.discovery import build
from datetime import date
from yt import youtube

from get_playlist_items import get_playlist_items

def get_channel_items(channel_link: str):
    
    videos = [] 

    channel_items_request = youtube.channels().list(
        part="contentDetails",
        id=channel_link
    ).execute()

    channel_items_response = channel_items_request["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

    # This assumes that the URL for playlists and channel videos generally match 
    get_playlist_items(channel_items_response)