BLUE = '\033[96m' 
YELLOW = '\u001b[33m' 
ENDC = '\033[0m'

if __name__ == "__main__":
    thread_number = input("Enter a thread number> ")

    while (1):
        user_in = input(f"{YELLOW}> {ENDC}")
        
        if user_in == "exit":
            print("\nEXITING")
            exit(0)