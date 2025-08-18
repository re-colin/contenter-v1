import os
from get_channel_items import get_channel_items
from get_playlist_items import get_playlist_items
from get_video_data import get_video_data
from read_links_from_file import read_links_from_file
from write_outputs_to_json_canvas import write_outputs_to_json
from environment_variables import video_outputs
from environment_variables import transcript_outputs
from pathlib import Path

BLUE = '\033[96m' 
YELLOW = '\u001b[33m' 
ENDC = '\033[0m'

if __name__ == "__main__":
    print(f"""
    {BLUE}
    ==================
    Enter a YouTube link (playlist, channel, video, ...).

    Can be an absolute file path containing links to a playlist, channel or video.
    Alternatively, pass in a single link directly. 

    Output directories are in {video_outputs} and {transcript_outputs}        
    {ENDC}
    """)

    if os.path.exists(video_outputs) == False:
        os.mkdir(video_outputs)

    json_mode = False
    transcribe_videos = False

    mode_select = input(f"\nUse JSON Canvas output? (makes outputs viewable in Obsidian Canvas) [ Y/N ] {YELLOW}> {ENDC}")

    if mode_select.upper() == "Y":
        json_mode = True

    mode_select = input(f"\nCreate video transcripts? [ Y/N ]{YELLOW}> {ENDC}")

    if mode_select.upper() == "Y":
        transcribe_videos = True


    while (1):
        user_in = input(f"{YELLOW}> {ENDC}")

        if user_in == "exit":
            print("\nEXITING")
            exit(0)

        if Path(user_in).is_file() == True: 
            links = read_links_from_file(user_in)

            for link in links:
                if "@" in link or link.startswith('UC'):
                    channel_videos_list = get_channel_items(link)

                    channel_video_uploads = get_playlist_items(channel_videos_list)

                    for video in channel_video_uploads:
                        vid_data = get_video_data(video)


                if "playlist?" in link:
                    playlist = get_playlist_items(link)

                    for video in playlist:
                        vid_data = get_video_data(video)


                if "watch?v=" in link:
                    vid_data = get_video_data(link)

                   


    # this might be redundant, maybe focus on input as file instead
    if user_in.contains("watch?v="):
        pass

    if user_in.contains("playlist?"):
        pass

    if user_in.contains("@"):
        pass

