import os
from pytubefix import YouTube
from pytubefix.cli import on_progress

def pytube_download(video_link: str, output_path: str, audio_only: False, video_res: str): 

    if "https://" in video_link:
        video_id = video_link.split("https://")[1]
    else:
        video_id = video_link
 
    pytube_link = YouTube(video_id)

    if audio_only == True:
        stream = pytube_link.streams.get_audio_only()
    else:
        stream = pytube_link.streams.filter(progressive=True) 

    download = stream.download(output_path=output_path)
