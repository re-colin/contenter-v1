from yt import youtube


def get_channel_items(channel_link: str) -> str:
    channel_name = channel_link
    channel_items_response = None
    channel_items_request = None

    if '\n' in channel_name:
        channel_name = channel_name.split('\n')[0]

    if '\r' in channel_link:
        channel_link = channel_link.split('\r')[0]

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

        if '?si=' in channel_name:
            channel_name = channel_name.split('?si=')[0]

        channel_items_request = youtube.channels().list(
            part="snippet,contentDetails",
            forHandle=channel_name,
            maxResults=1
        )

    channel_items_response = channel_items_request.execute()

    uploads_playlist_link = channel_items_response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

    print(f"Uploads: {uploads_playlist_link}")

    return uploads_playlist_link