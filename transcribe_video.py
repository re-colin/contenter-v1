import os
import time
import whisper
from datetime import date
# from pytube import YouTube
from pytubefix import YouTube
from pytubefix.cli import on_progress
from environment_variables import transcript_outputs

video_folder = "Video Downloads"

def transcribe_video(video_id: str, whisper_model_size: str):
	if not os.path.exists(transcript_outputs):
		os.mkdir(transcript_outputs)

	start = time.time()

	model = whisper.load_model(whisper_model_size, device='cpu')

	video_link = f"https://www.youtube.com/watch?v={video_id}"
	print(video_link)

	transcription = os.path.join(transcript_outputs, video_id)

	if not os.path.exists(transcription):
		pytube_link = YouTube(video_link)

		stream = pytube_link.streams.get_audio_only() 
		
		download = stream.download(output_path="Video Downloads")

		result = model.transcribe(download)
		
		# with open(transcription, 'a') as f:
		# 	f.write(result["text"])
	else:
		print(f"\n\nTranscribed audio with name {transcription} already exists - Skipping.\n\n")

	pytube_output = os.path.join(video_folder, download)
	os.remove(pytube_output)

	end = time.time()
	total_runtime = end - start
	print(f"Session / Runtime completed in {total_runtime} seconds.")

	return result['text']