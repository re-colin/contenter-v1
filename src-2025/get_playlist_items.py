import os
import time
import urllib.request
from googleapiclient.discovery import build
from datetime import date
from yt import youtube

# Can be used for both playlists and videos returned from a channel AS a playlist
def get_playlist_items(playlist_link: str) -> list:

    playlist_link = playlist_link.split('=')[1]
    playlist_link = playlist_link.split('&')[0]
    videos = []
    next_page_token = None

    while 1:
        playlist_items_request = youtube.playlistItems().list(
            part="contentDetails, snippet",
            playlistId=playlist_link,
            maxResults=100,
            pageToken=next_page_token
        )

        playlist_items_response = playlist_items_request.execute()

        videos.append(playlist_items_response['items'])

        next_page_token = playlist_items_response.get('nextPageToken')

        if not next_page_token:
            break

    return videos