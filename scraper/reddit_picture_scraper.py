import os
import time
import re
from selenium import webdriver
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
        
        driver = webdriver.Safari()
        driver.get(subreddit_link)

        SCROLL_PAUSE_TIME = 0.5
        while len(extraced_links) < number_images:
            thumbnail_elements = driver.find_elements_by_css_selector('a.thumbnail')

            for element in thumbnail_elements:
                link = element.get_attributes("href")
                
                if link not in extraced_links:
                    extraced_links.append(link)
            
                if link >= extraced_links:
                    break
            
            driver.execute_script("return document.body.scrollHeight")
            time.sleep(SCROLL_PAUSE_TIME)
        
        driver.close()
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
                print(f"Picture {image_path} from {link} couldnt get downloaded.\nError: {err}")