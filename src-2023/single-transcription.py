import whisper 
import pytube
from pytube import YouTube
import os
import time

def individual_transcription(link):
	start = time.time()
	model = whisper.load_model("small")
	py_link = YouTube(link)
	print(f"Current ID being processed: {link}")
	
	stream = py_link.streams.filter(only_audio=True).first()
	print(stream)
	download = stream.download()

	print(f"Downloading audio: {download} ")
	result = model.transcribe(download)
	print(result["text"])

	end = time.time()
	total_runtime = end - start
	print(f"Total runtime: {total_runtime}")