import os
import requests
import re
from bs4 import BeautifulSoup
import urllib

class pictureScraper:
    def __init__(self) -> None:
        pass

    def read_file(self, file_path: str) -> list[str]: # reads every link in file in a list
        with open(file_path) as file:
            links = [line.rstrip() for line in file]
        
        return links
    
    def fetch_imagelinks(self, subreddit_link: str, number_images: int = 25) -> list[str]: # scrapes links of pictures of the given subreddit link 
        extraced_links = []
        req = requests.get(subreddit_link)
        parser = BeautifulSoup(req.content, "html.parser")

        thumbnail_tag = parser.find_all('a', class_='thumbnail')
        
        # Extracts and collects valid image URLs from 'thumbnail_tag'
        for tag in thumbnail_tag[:number_images]:
            image_url = tag.get('href')

            if image_url != None:
                print(image_url)
                extraced_links.append(image_url)

        return extraced_links

    def downloading_imagelinks(self, image_links: list[str], output_path: str) -> None: # downloads every picture
        pattern = r'(?<=\/)([^\/]+\.(jpg|jpeg|png))$'

        for link in image_links:
            # Extract the matching part from the link and construct the full image path
            match = re.search(pattern, link)
            if match:
                jpg_part = match.group(1)
            
            image_path = os.path.join(output_path, jpg_part) 

            # Downloads the pictures 
            try:
                urllib.request.urlretrieve(link, image_path)
                print(f"Picture {image_path} from {link} got downloaded.")
            except Exception as err:
                print(err)