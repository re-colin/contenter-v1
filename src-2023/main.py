import os
from googleapiclient.discovery import build
import urllib.request
from datetime import date
import time 
from pytube import YouTube
import whisper

API_KEY = os.environ['YT_API_KEY']
youtube = build('youtube', 'v3', developerKey=API_KEY)

link_items = []

def CrawlFromFile(input_link):

	start = time.time()

	cwd = os.getcwd()
	today = date.today()

	print("Retrieving...")
	with open(input_link, 'r') as f:
		for line in f:
			link_id = line.split('=')[1]
			link_id = link_id.split('&')[0]
			link_items.append(link_id)
			
			print(link_id)

			video_details = youtube.videos().list(
				part='snippet, contentDetails',
				id=link_id
			).execute()

			print(video_details)

			video_id = video_details['items'][0]['id']
			print(f"\n\nVideo ID: {video_id}\n")

			title = video_details['items'][0]['snippet']['title']
			print(f"Title: {title}")

			thumbnail_url = video_details['items'][0]['snippet']['thumbnails']['default']['url']
			print(f"Thumbnail URL : {thumbnail_url}")

			publish_date = video_details['items'][0]['snippet']['publishedAt']
			print(f"Publish Date : {publish_date}")

			description = video_details['items'][0]['snippet']['description']
			print(f"Description : {description}")

			channel_id = video_details['items'][0]['snippet']['channelId']
			print(f"Channel ID : {channel_id}")

			channel_name = video_details['items'][0]['snippet']['channelTitle']
			print(f"Channel Name : {channel_name}")
			print('------------------------------------')

			urllib.request.urlretrieve(thumbnail_url, video_id + '.jpg')

			video_file = os.path.join(cwd, video_id + '.md')
			if not os.path.exists(video_file):
				with open(video_file, 'w') as f:
					f.write(
							f"Video title: {title}\n Video ID: {video_id} \n Channel ID: {channel_id} \n Channel Name: {channel_name} \n Video published at: {publish_date} \n Date of writing file: {today} \n \nDescription: \n {description}\n \n\n#### COMMENTS:\n\n"
						)
			else:
				print(f"\n\nFile with name {video_id} already exists. Skipping...\n\n")
				continue

			comments_response = youtube.commentThreads().list(
				part="snippet, replies",
				videoId=video_id
			).execute()

			comments_index = 0  # this might be redundant because enumerate() is a thing
			reply_index = 0

			global replies
			replies = []

			while comments_response:
				for item in comments_response['items']:

					comment = item['snippet']['topLevelComment']['snippet']['textDisplay']

					comment_author = item['snippet']['topLevelComment']['snippet']['authorDisplayName']

					comments_index += 1

					reply_count = item['snippet']['totalReplyCount']

					if reply_count > 0:
						for reply in item['replies']['comments']:
							reply_index += 1
							reply_author = reply['snippet']['authorDisplayName']
							reply = reply['snippet']['textDisplay']
							replies.append(reply_author)
							replies.append(reply)

					print(comments_index, comment, replies, end='\n\n')

					with open(video_id + '.md', 'a') as f:
						f.write(
							f"{comments_index}: {comment_author} \n {comment} \n\n \tReplies: {replies}\n\n")

					replies = []

				if 'nextPageToken' in comments_response:
					p_token = comments_response['nextPageToken']
					comments_response = youtube.commentThreads().list(
						part='snippet, replies', videoId=video_id, pageToken=p_token).execute()
				else:
					print("\n\nNo more pages to be found, passing...\n\n")
					break

		end = time.time()
		total_runtime = end - start
		print(f"Session / Runtime completed in {total_runtime} seconds.")

def PlaylistCrawler(input_link):
	start = time.time()

	next_page_token = None
	
	input_link = input_link.split('=')[1] 
	input_link = input_link.split('&')[0]

	print(f'Playlist ID: {input_link}')

	today = date.today()
	cwd = os.getcwd()

	link_items = []
	while 1:
		playlist_items_request = youtube.playlistItems().list(
			part="contentDetails, snippet",
			playlistId=input_link,
			maxResults=100,
			pageToken=next_page_token
		)

		playlist_items_response = playlist_items_request.execute()

		link_items += playlist_items_response['items']

		next_page_token = playlist_items_response.get('nextPageToken')
		if not next_page_token:
			break

	for item in link_items:
		print(f"Link item: {item}")
		# print(f"Item list: {link_items}")

		video_id = item['contentDetails']['videoId']

		video_details = youtube.videos().list(
			part='snippet, statistics',
			id=video_id,
			maxResults=100
		).execute()

		title = item['snippet']['title'] 
		thumbnail_url = video_details['items'][0]['snippet']['thumbnails']['default']['url']
		publish_date = video_details['items'][0]['snippet']['publishedAt']
		description = video_details['items'][0]['snippet']['description']
		channel_id = video_details['items'][0]['snippet']['channelId']
		channel_name = video_details['items'][0]['snippet']['channelTitle']
		urllib.request.urlretrieve(thumbnail_url, video_id + '.jpg') 

		video_file = os.path.join(cwd, video_id + '.md')
		if not os.path.exists(video_file):
			with open(video_file, 'w') as f:
				f.write(
					f"Video title: {title}\n Video ID: {video_id} \n Channel ID: {channel_id} \n Channel Name: {channel_name} \n Video published at: {publish_date} \n Date of writing file: {today} \n \nDescription: \n {description}\n \n\n#### COMMENTS:\n\n"
					)
		else: 
			print(f"\n\nFile with name {video_id} already exists. Skipping...\n\n")
			continue

		comments_response = youtube.commentThreads().list(
			part="snippet, replies",
			videoId=video_id
		).execute()

		comments_index = 0 ## this might be redundant because enumerate() is a thing
		reply_index = 0

		global replies
		replies = []

		while comments_response:
			for item in comments_response['items']:

				comment = item['snippet']['topLevelComment']['snippet']['textDisplay']

				comment_author = item['snippet']['topLevelComment']['snippet']['authorDisplayName']

				comments_index += 1

				reply_count = item['snippet']['totalReplyCount']

				if reply_count > 0:
					for reply in item['replies']['comments']:
						reply_index += 1
						reply_author = reply['snippet']['authorDisplayName']
						reply = reply['snippet']['textDisplay']
						replies.append(reply_author)
						replies.append(reply)
						print(f"Replies: {replies}")

				print(comments_index, comment, replies, end='\n\n')

				with open(video_id + '.md', 'a') as f:
					f.write(
						f"{comments_index}: {comment_author} \n {comment} \n\n \tReplies: {replies}\n\n")
				
				replies = []

			if 'nextPageToken' in comments_response:
				p_token = comments_response['nextPageToken']
				comments_response = youtube.commentThreads().list(
					part='snippet, replies', videoId=video_id, pageToken=p_token).execute()
			else:
				print("\n\nNo more pages to be found, passing...\n\n")
				break

	end = time.time()
	total_runtime = end - start
	print(f"Session / Runtime completed in {total_runtime} seconds.")



# Transcribes video inputs.
def Transcriber(input_link):

	print("\n\nPreparing transcription...\n\n")
	cwd = os.getcwd()
	start = time.time()
	model = whisper.load_model("small")

	for item in link_items:
		og_link = item['contentDetails']['videoId']
		print(f"\n\nOG Video link contained is: {og_link}\n\n")
		default_video_link = f"https://www.youtube.com/watch?v={og_link}"

		print(f"Item link: {default_video_link}\n")

		transcription_output = os.path.join(cwd, default_video_link + "--TRANSCRIPTION" + '.md')

		if not os.path.exists(transcription_output):
			pytube_link = YouTube(default_video_link)
			print(f"Current ID being processed: {default_video_link}")

			stream = pytube_link.streams.filter(only_audio=True).first()
			print(stream)
			download = stream.download()

			print(f"\nDownloading audio: {download}\n")
			result = model.transcribe(download)
			print(result["text"])
			with open(transcription_output, 'w') as f:
				f.write(result["text"])
		else:
			print(
				f"\n\nTranscribed audio with name {transcription_output} already exists. Skipping...\n\n")
			continue

		print(f'\n\n{item} processed! Proceeding...\n\n')

	end = time.time()
	total_runtime = end - start
	print(f"Session / Runtime completed in {total_runtime} seconds.")


# Transcriber('https://youtube.com/playlist?list=PLvPRfhd35wZr-yXqGbwRdtchywWMJDc_n')