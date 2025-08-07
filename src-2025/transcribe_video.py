import os
import time
import whisper
from datetime import date
from pytube import YouTube


def transcribe_video(video_link: str, whisper_model_size: str):
	transcript_output_dir = os.environ['TRANSCRIPTION_OUT']

	if not os.path.exists(transcript_output_dir):
		os.mkdir(transcript_output_dir)

	start = time.time()
	cwd = os.getcwd()

	model = whisper.load_model(whisper_model_size)

	video_link_id = video_link['contentDetails']['videoId'] 
	
	video_link = f"https://www.youtube.com/watch?v={video_link_id}"

	transcript_output = f"{transcript_output_dir}/{video_link_id}"

	if not os.path.exists(transcript_output):

		pytube_link = YouTube(video_link)

		stream = pytube_link.streams.filter(only_audio=True).first()
		download = stream.download()

		result = model.transcribe(download)
		
		with open(transcript_output, 'a') as f:
			f.write(result["text"])
	else:
		print(f"\n\nTranscribed audio with name {transcript_output} already exists. Skipping...\n\n")

	end = time.time()
	total_runtime = end - start
	print(f"Session / Runtime completed in {total_runtime} seconds.")