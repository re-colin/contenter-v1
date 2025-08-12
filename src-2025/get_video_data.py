import os
import time 
import urllib.request
from googleapiclient.discovery import build
from datetime import date
from yt import youtube
from environment_variables import video_outputs


def get_video_data(video_link: str):
    video_id = None
    
    if isinstance(video_link, dict):
        video_id = video_link['contentDetails']['videoId']
    else:
        video_id = video_link.split('\n')[0]
        video_id = video_id.split('watch?v=')[1]
        video_id = video_id.split('&si=')[0]

    video_details = youtube.videos().list(
        part='snippet, statistics, contentDetails',
        id=video_id
    ).execute()

    title = "No" 
#    thumbnail_url = video_details['items'][0]['snippet']['thumbnails']['default']['url']
    publish_date = video_details['items'][0]['snippet']['publishedAt']
    description = video_details['items'][0]['snippet']['description']
    channel_id = video_details['items'][0]['snippet']['channelId']
    channel_name = video_details['items'][0]['snippet']['channelTitle']
#    urllib.request.urlretrieve(thumbnail_url, video_id + '.jpg') 
            
    next_page_token = None

    video_file = os.path.join(video_outputs, f"{title}.md")

    with open(video_file, 'a', encoding="utf-8") as file:
        file.write(f"""
            TITLE: {title}
            CHANNEL: {channel_name}
            PUBLISH DATE: {publish_date}
            DESCRIPTION: \n{description}\n\n\n
        """)

    comments_request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100,
        pageToken=next_page_token,
    )
    try: 
        comments_response = comments_request.execute()
        for comment in comments_response['items']:
            author_name = comment['snippet']['topLevelComment']['snippet']['authorDisplayName']
            comment_text = comment['snippet']['topLevelComment']['snippet']['textOriginal']

            next_page_token = comments_response.get('nextPageToken')
            if not next_page_token:
                break

            with open(video_file, 'a') as file:
                file.write(f"\n\n{author_name}:\n{comment_text}\n")
                                
    except: 
        print("\n\nComments are disabled for this video, or an exception occured.")