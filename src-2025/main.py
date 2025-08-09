import os
from get_channel import get_channel_items

from read_links_from_file import read_links_from_file

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
                    pass

                if link.contains("playlist?"):
                    pass

                if link.contains("@"):
                    pass


        # this might be kinda redundant, maybe focus on input as file
        if user_in.contains("watch?v="):
            pass

        if user_in.contains("playlist?"):
            pass

        if user_in.contains("@"):
            pass

