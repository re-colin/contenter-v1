from pytube import YouTube
import whisper
import os
import time

def Transcriber(input):
	file = 'Links.txt'
	cwd = os.getcwd()
	input = os.path.join(cwd, 'src', file)

	## Why does this take 13 seconds to run
	# 2025-0805  Because its loading a model, you goof!
	print("\n\n")
	start = time.time()
	model = whisper.load_model("small")
	with open(input, 'r') as f:
		for line in f:
			split_line = str(line).split('=')[1]
			split_line = split_line.split('&')[0]
			transcribed_output = os.path.join(cwd, split_line + '.md')
			if not os.path.exists(transcribed_output):
				py_link = YouTube(line)
				print(f"Current ID being processed: {line}")
				
				stream = py_link.streams.filter(only_audio=True).first()
				print(stream)
				download = stream.download()

				print(f"\nDownloading audio: {download}\n")
				result = model.transcribe(download)
				print(result["text"])
				with open(transcribed_output, 'w') as f:
					f.write(result["text"])
			else:
				print(f"\n\nTranscribed audio with name {line} already exists. Skipping...\n\n")
				continue

			print(f'\n\n{line} processed! Proceeding...\n\n')

	end = time.time()
	total_runtime = end - start
	print(f"Session / Runtime completed in {total_runtime} seconds.")
