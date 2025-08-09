import os
from get_channel_items import get_channel_items
from get_playlist_items import get_playlist_items
from get_video_data import get_video_data
from read_links_from_file import read_links_from_file
from write_outputs_to_file import write_outputs_to_file
from write_outputs_to_json_canvas import write_outputs_to_json

BLUE = '\033[96m' 
YELLOW = '\u001b[33m' 
ENDC = '\033[0m'

if __name__ == "__main__":
    print(f"""\n
        {BLUE}
        ==================
        Enter a YouTube link (playlist, channel, video, ...).

        Can be an absolute file path containing links to a playlist, channel or video.
        Alternatively, pass in a single link directly. 
        
        {ENDC}
    """)

    json_mode = False
    transcribe_videos = False

    mode_select = input(f"Use JSON Canvas output? (makes outputs viewable in Obsidian Canvas) [ Y/N ] {YELLOW}> {ENDC}")

    if mode_select.upper() == "Y":
        json_mode = True

    mode_select = input(f"Create video transcripts? [ Y/N ]{YELLOW}> {ENDC}")

    if mode_select.upper() == "Y":
        transcribe_videos = True


    while (1):
        user_in = input(f"{YELLOW}> {ENDC}")
        
        if user_in == "exit":
            print("\nEXITING")
            exit(0)

        user_in_is_file = os.str(user_in).path.exists

        if user_in_is_file == True: 
            links = read_links_from_file(user_in)

            for link in links:
                if link.contains("watch?v="):
                    get_video_data(link)


                if link.contains("playlist?"):
                    playlists = get_playlist_items(link)
                    for playlist in playlists:
                        
                        vid_data = get_video_data(playlist)
                        

                if link.contains("@"):
                    channel_videos = get_channel_items(link)
                    videos = get_playlist_items(channel_videos)

                    for vid in videos:
                        get_video_data(vid)



        # this might be redundant, maybe focus on input as file instead
        if user_in.contains("watch?v="):
            pass

        if user_in.contains("playlist?"):
            pass

        if user_in.contains("@"):
            pass

