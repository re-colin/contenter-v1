import os
from googleapiclient.discovery import build
import urllib.request
from datetime import date
import time 

def retrieval(link):
      api_key = 'AIzaSyDlxWH6xyt7O4glzuDq-7A-iKafwAI2fGY'
      youtube = build('youtube', 'v3', developerKey=api_key)

      ## Test link: https://youtube.com/playlist?list=PLm18TxJckGNE6dYvDpeZujliLZWcz-d2u

      cwd = os.getcwd()
      output_folder = os.path.join(cwd, "output")

      start = time.time()
      print(f"Full Link {link}")
      api_playlist_link = str(link).split('=')[1]
      api_playlist_link = api_playlist_link.split('&')[0]
      print(f"Split Link: {api_playlist_link}")
      print("\n\n" + "Fetching playlist contents..." + "\n\n")
      videos = []
      next_page_token = None 
      today = str(date.today())
      print("Today's date:", today)

      while 1:
            playlist_items_request = youtube.playlistItems().list(
                  part="contentDetails, snippet",
                  playlistId=api_playlist_link,
                  maxResults=100,
                  pageToken=next_page_token
            )

            playlist_items_response = playlist_items_request.execute()

            videos += playlist_items_response['items']

            next_page_token = playlist_items_response.get('nextPageToken')
            if not next_page_token:
                  break

      for video in videos:
            video_id = video['contentDetails']['videoId']

            video_details = youtube.videos().list(
                  part='snippet, statistics',
                  id=video_id
            ).execute()

            title = video['snippet']['title']
            thumbnail_url = video_details['items'][0]['snippet']['thumbnails']['default']['url']
            publish_date = video_details['items'][0]['snippet']['publishedAt']
            description = video_details['items'][0]['snippet']['description']
            channel_id = video_details['items'][0]['snippet']['channelId']
            channel_name = video_details['items'][0]['snippet']['channelTitle']
            urllib.request.urlretrieve(thumbnail_url, video_id + '.jpg') 
            
            next_page_token = None
            video_file = os.path.join(cwd, video_id + '.md')
            if not os.path.exists(video_file):
                  with open(video_file, 'w') as f:
                        f.write(f"Video title: {title}\n")
                        f.write(f"Video ID: {video_id} \n")
                        f.write(f"Channel ID: {channel_id} \n")
                        f.write(f"Channel Name: {channel_name} \n")
                        f.write(f"Video published at: {publish_date} \n")
                        f.write(f"Date of writing file: {today} \n")
                        f.write(f"\nDescription: \n {description}\n")
                        f.write(f"\n\nDESCRIPTION BREAK\n\n")
                        f.write(f"\n\nCOMMENTS START\n\n")
            else: 
                  print(f"\n\nFile with name {video_id} already exists. Skipping...\n\n")
                  continue

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

                              with open(video_id + '.md', 'a') as f:
                                    print(f"{author_name}: {comment_text}")
                                    f.write(f"\n\n{author_name}:\n{comment_text}\n")
                                    
            except: 
                  print("\n\nComments are disabled for this video, or an exception occured. Skipping...\n\n")

      end = time.time()
      total_runtime = end - start
      print('\n--------------------------------------------\n')
      print(f'\n\nSession runtime completed in {total_runtime} seconds. \n\n')


retrieval('Videos.txt')
