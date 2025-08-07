def read_links_from_file(file_path: str) -> list:
	video_ids = []

	with open(file_path, 'r') as file:
		for video_id in file:
			video_ids.append(video_id)

	print(video_ids)	
	return video_ids