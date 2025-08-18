from yt import youtube

def get_playlist_items(playlist_link: str) -> list:
    if 'playlist?list=' in playlist_link:
        playlist_link = playlist_link.split('=')[1]

    if '&' in playlist_link:
        playlist_link = playlist_link.split('&')[0]

    if '\n' in playlist_link:
        playlist_link = playlist_link.split('\n')[0]

    videos = []
    next_page_token = None

    while 1:
        playlist_items_request = youtube.playlistItems().list(
            part="contentDetails, snippet",
            playlistId=playlist_link,
            maxResults=500,
            pageToken=next_page_token
        )

        playlist_items_response = playlist_items_request.execute()

        video_id = playlist_items_response['items'][0]['contentDetails']['videoId']

        videos.append(video_id)

        next_page_token = playlist_items_response.get('nextPageToken')

        if next_page_token == None:
            break

    print(videos)
    return videos