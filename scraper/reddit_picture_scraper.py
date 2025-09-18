import os
import time
import re
from typing import Literal, get_args
import selenium
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

    def read_file(self, file_path: str) -> list[(str, int)]: # reads every link in file in a list
        links = []
        
        with open(file_path) as file:              
            for line in file:
                link, quantity = re.split(", |,", line, 1)
                links.append((link, int(quantity)))

        return links

    def setup_driver(self, webdriver_option: webdriver_TYPES, proxy: None) -> webdriver:
        options = get_args(webdriver_TYPES)
        assert webdriver_option in options, f"'{webdriver_option}' is not an option, only Safari, Chrome and Firefox."
        
        options = Options()

        if proxy != None:
            options.add_argument(f"--proxy-server={proxy}")

        if webdriver_option == "Safari":
            driver = webdriver.Safari(options)

        elif webdriver_option == "Chrome":
            driver = webdriver.Chrome(options)

        elif webdriver_option == "Firefox": 
            driver = webdriver.Firefox(options)

        return driver

    def fetch_imagelinks(self, driver: webdriver, subreddit_link: str, number_images: int = 25) -> list[(str,str)]: # scrapes links of pictures of the given subreddit link 
        driver.get(subreddit_link)

        # create regex oject with pattern 
        pattern = r'(?<=\/)([^\/]+\.(jpg|jpeg|png))$'
        regexObj = re.compile(pattern)

        extracted_links = [] # Structure of the extraced_link array: [(full link, jpg part), ...]
        NEXTPAGE_BUTTON_PATH = "//div[@class='nav-buttons']//a[text()='Weiter ›']"
        while len(extracted_links) < number_images:
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, NEXTPAGE_BUTTON_PATH)))
            thumbnail_elements = driver.find_elements(By.CSS_SELECTOR, 'a.thumbnail')
            
            for element in thumbnail_elements:
                link = element.get_attribute("href")
                
                if len(extracted_links) >= number_images:
                    break

                if link not in {t[0] for t in extracted_links}:
                    #Extract matching part from the link with regex
                    match = regexObj.search(link)

                    #TODO: Check if href link is even a image link, href links are also used for arctiles etc.
                    if match == None:
                        print(f"No match found in {link} due to various reasons. Continuing with the next link.")
                        continue

                    jpp_part = match.group(1)
                    print(f"Image link {link} of {element} with the jpg part {jpp_part} was found.")

                    extracted_links.append((link, jpp_part))
                    
            time.sleep(1)
            try:
                nextPage_button = driver.find_element(By.XPATH, NEXTPAGE_BUTTON_PATH)
            except Exception as err:
                print(err)
                return err
            finally:
                driver.execute_script("arguments[0].click();", nextPage_button)

        driver.close()
        return extracted_links

    def downloading_imagelinks(self, image_links: list[(str,str)], output_path: str) -> None: # downloads every picture
        for link, jpg_part in image_links:

            image_path = os.path.join(output_path, jpg_part) 

            # Downloads the pictures 
            try:
                urllib.request.urlretrieve(link, image_path)
                print(f"Picture {image_path} from {link} got downloaded.")
            except Exception as err:
                print(f"Picture {image_path} from {link} couldnt get downloaded.\nError: {err}")

if __name__ == "__main__":
    rps = pictureScraper()
    links = rps.read_file("test/subreddit_links.txt")
    driver = rps.setup_driver("Safari", None)

    extracted_links = rps.fetch_imagelinks(driver=driver, subreddit_link="https://old.reddit.com/r/pics/", number_images=200)
    print(f"\n{extracted_links}\n")
    # rps.downloading_imagelinks(extracted_links, "test/output_images")