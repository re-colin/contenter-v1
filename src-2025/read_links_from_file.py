def read_links_from_file(file_path: str) -> list:
	links = []

	with open(file_path, 'r') as file:
		for link in file:
			links.append(link)

	print(links)	
	return links