from distutils import command
from logging import root
import tkinter as tk
from tkinter import *
import sys
from main import PlaylistCrawler
from main import CrawlFromFile
from main import Transcriber

root = tk.Tk()
root.title("Repo")

f1 = Frame(root, height=100, width=100).pack()

label = tk.Label(text="Enter playlist link or local text file  holding video IDs. ").pack()
entry = tk.Entry()
entry.pack()

## text file input, (link = 'Filename.txt'), if it doesn't exist an error is thrown in the terminal and no content will be retrieved

## 2023-0420: In-Parts or One-Process modes

def one_process_crawlandtranscribe():
	link=entry.get()
	PlaylistCrawler(link)
	Transcriber(link)

def crawl():
	link=entry.get()
	PlaylistCrawler(link)

def transcribe():
	link=entry.get()
	Transcriber(link)

def read_from_file():
	link=entry.get()
	CrawlFromFile(link)

crawl_file = tk.Button(
	root,
	text="Crawl file links",
	width=20,
	height=3,
	bg="grey",
	fg="black",
	command=lambda: read_from_file()
).pack()

crawl_getter = tk.Button(
	root,
	text="Get",
	width=20,
	height=3,
	bg="grey",
	fg="black",
	command=lambda: crawl()
).pack()
## ^^^^^^
## if the transcribe function is automatically called from `retrieve` and `read` theres not much point in making it a seperate button
transcribe = tk.Button(
	root, 
	text="Transcribe",
	width=20,
	height=3,
	bg="orange",
	fg="black",
	command=lambda: transcribe()
)

batch_single_process = tk.Button(
	root,
	text="Get (Crawl&Transcribe)",
	width=20,
	height=3,
  	bg="orange",
	fg="black",
	command=lambda: one_process_crawlandtranscribe()
).pack()

# Add crawler option for .txt files

exit = tk.Button(
	root,
	text="Exit",
	width=15,
	height=3,
	bg="orange",
	fg="black",
	command=lambda: sys.exit()
).pack()

root.mainloop()

