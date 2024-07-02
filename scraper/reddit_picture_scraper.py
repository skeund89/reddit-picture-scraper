import os
import time
import re
from typing import Literal, get_args
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib

webdriver_TYPES = Literal["Safari", "Chrome", "Firefox"]

class pictureScraper:
    def __init__(self) -> None:
        pass

    def read_file(self, file_path: str) -> list[str]: # reads every link in file in a list
        with open(file_path) as file:
            links = [line.rstrip() for line in file]
        
        return links
    
    def fetch_imagelinks(self, webdriver_option: webdriver_TYPES, proxy: None, subreddit_link: str, number_images: int = 25) -> list[str]: # scrapes links of pictures of the given subreddit link 
        extraced_links = []
        options = get_args(webdriver_TYPES)
        assert webdriver_option in options, f"'{webdriver_option}' is not an option, only Safari, Chrome and Firefox."

        options = Options()
        options.add_argument(f"--proxy-server={proxy}")

        if webdriver_option == "Safari":
            driver = webdriver.Safari(options)

        elif webdriver_option == "Chrome":
            driver = webdriver.Chrome(options)

        elif webdriver_option == "Firefox": 
            driver = webdriver.Firefox(options)

        driver.get(subreddit_link)

        NEXTPAGE_BUTTON_PATH = "//div[@class='nav-buttons']//a[text()='Weiter ›']"
        while len(extraced_links) < number_images:
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, NEXTPAGE_BUTTON_PATH)))
            thumbnail_elements = driver.find_elements(By.CSS_SELECTOR, 'a.thumbnail')
            
            for element in thumbnail_elements:
                link = element.get_attribute("href")
                
                if link not in extraced_links:
                    extraced_links.append(link)
            
                if len(extraced_links) >= number_images:
                    break
                    
            try:
                nextPage_button = driver.find_element(By.XPATH, NEXTPAGE_BUTTON_PATH)
            except Exception as err:
                print(err)
                return err
            finally:
                driver.execute_script("arguments[0].click();", nextPage_button)

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

if __name__ == "__main__":
    rps = pictureScraper()
    extracted_links = rps.fetch_imagelinks("https://old.reddit.com/r/pics/", 100)
    print(extracted_links)