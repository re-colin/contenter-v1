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