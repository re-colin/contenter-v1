## METHOD 2: VIDEO LINKS FROM A TEXT FILE
# 
import os
from googleapiclient.discovery import build
import urllib.request
from datetime import date
import time

def read_from_file(file):
	start = time.time()

	cwd = os.getcwd()
	file = 'Links.txt'  # User input
	link = os.path.join(cwd, 'src', file)

	api_key = 'AIzaSyDlxWH6xyt7O4glzuDq-7A-iKafwAI2fGY'
	youtube = build('youtube', 'v3', developerKey=api_key)

	today = str(date.today())
	video_ids = []

	with open(link, 'r') as f:
		for line in f:
			link_id = line.split('=')[1]
			link_id = link_id.split('&')[0]
			print(f"Video ID : {link_id}")

			video_ids.append(link_id.strip())
			print(f"\n\nIter Link ID: {link_id}\n\n")

			video_details = youtube.videos().list(
				part='snippet, contentDetails',
				id=link_id
			).execute()

			print(f"\n\nVideo details: {video_details}\n\n")
			video_id = video_details['items'][0]['id']
			print(f"\n\nVideo details: {video_id}\n\n")

			title = video_details['items'][0]['snippet']['title']
			thumbnail_url = video_details['items'][0]['snippet']['thumbnails']['default']['url']
			publish_date = video_details['items'][0]['snippet']['publishedAt']
			description = video_details['items'][0]['snippet']['description']
			channel_id = video_details['items'][0]['snippet']['channelId']
			channel_name = video_details['items'][0]['snippet']['channelTitle']

			urllib.request.urlretrieve(thumbnail_url, video_id + '.jpg')

			next_page_token = None
			video_file = os.path.join(cwd, link_id + '.md')
			if not os.path.exists(video_file):
				with open(video_file, 'w') as f:
					f.write(f"Video title: {title}\n")
					f.write(f"Video ID: {video_id} \n")
					f.write(f"Channel ID: {channel_id} \n")
					f.write(f"Channepl Name: {channel_name} \n")
					f.write(f"Video published at: {publish_date} \n")
					f.write(f"Date of writing file: {today} \n")
					f.write(f"\nDescription: \n {description}\n")
					f.write(f"\n\n### DESCRIPTION BREAK\n\n")
					f.write(f"\n\n### COMMENTS START\n\n")
			else:
				print(f"\nFile with name {video_id} already exists. Skipping...\n")
				continue

			comments_request = youtube.commentThreads().list(
				part="snippet",
				videoId=link_id,
				maxResults=100,
				pageToken=next_page_token
			)

			try:
				comments_response = comments_request.execute()
				print(f"Comments response Items: {comments_response}")
				for comment in comments_response['items']:
					author_name = comment['snippet']['topLevelComment']['snippet']['authorDisplayName']
					comment_text = comment['snippet']['topLevelComment']['snippet']['textOriginal']

					next_page_token = comments_response.get('nextPageToken')
					if not next_page_token:
						break

					with open(link_id + '.md', 'a') as f:
						print(f"{author_name}: {comment_text}")
						f.write(f"\n\n{author_name}:\n{comment_text}\n")
			except:
				print("\n\nComments are disabled for this video, or an exception occured. Skipping...\n\n")

		end = time.time()
		total_runtime = end - start
		print(f"Session / Runtime completed in {total_runtime} seconds.")