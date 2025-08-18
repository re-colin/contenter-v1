import os
import time
import whisper
from datetime import date
from pytube import YouTube

from environment_variables import transcript_outputs

def transcribe_video(video_link: str, whisper_model_size: str):
	if not os.path.exists(transcript_outputs):
		os.mkdir(transcript_outputs)

	start = time.time()
	cwd = os.getcwd()

	model = whisper.load_model(whisper_model_size)

	video_link_id = video_link['contentDetails']['videoId'] 
	
	video_link = f"https://www.youtube.com/watch?v={video_link_id}"

	transcription = f"{transcript_outputs}/{video_link_id}"
	transcription = os.path.join(transcript_outputs, video_link_id)

	if not os.path.exists(transcription):

		pytube_link = YouTube(video_link)

		stream = pytube_link.streams.filter(only_audio=True).first()
		download = stream.download()

		result = model.transcribe(download)
		
		with open(transcription, 'a') as f:
			f.write(result["text"])
	else:
		print(f"\n\nTranscribed audio with name {transcription} already exists - Skipping.\n\n")

	end = time.time()
	total_runtime = end - start
	print(f"Session / Runtime completed in {total_runtime} seconds.")