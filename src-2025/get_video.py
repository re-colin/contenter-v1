import os
import time 
import urllib.request
from googleapiclient.discovery import build
from datetime import date
from yt import youtube

video_outputs = os.environ['VIDEO_OUTPUTS']

def get_video(video_link: str):
    video_details = youtube.videos().list(
        part='snippet, statistics',
        id=video_link
    ).execute()

    title = video_details['snippet']['title']
    thumbnail_url = video_details['items'][0]['snippet']['thumbnails']['default']['url']
    publish_date = video_details['items'][0]['snippet']['publishedAt']
    description = video_details['items'][0]['snippet']['description']
    channel_id = video_details['items'][0]['snippet']['channelId']
    channel_name = video_details['items'][0]['snippet']['channelTitle']
    urllib.request.urlretrieve(thumbnail_url, video_link + '.jpg') 
            
    next_page_token = None

    video_file = os.path.join(video_outputs, f"{title}.md")
 
    comments_request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_link,
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

            with open(video_file + '.md', 'a') as f:
                print(f"{author_name}: {comment_text}")
                f.write(f"\n\n{author_name}:\n{comment_text}\n")
                                
    except: 
        print("\n\nComments are disabled for this video, or an exception occured.")