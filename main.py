import argparse
from scraper import pictureScraper

if __name__ == "__main__":
    rps = pictureScraper()
    
    parser = argparse.ArgumentParser(description="The Reddit Picture Scraper is a Python application designed for fetching and downloading images from specified subreddits.")
    parser.add_argument("-ip", "--inputpath", help="The file with all your subreddit links (old.reddit.com)", type=str, required=True)
    parser.add_argument("-q", "--quantity", help="number of pictures you would like to download for each subreddit", type=int, required=True)
    parser.add_argument("-op", "--outputpath", help="output path for the pictures", required=True)
    parser.add_argument("-d", "--driver", help="your driver for scraping", type=str, choices=["Safari", "Chrome", "Firefox"], required= True)
    parser.add_argument("-p", "--proxy", help="proxy, ip:port", default=None, required=False)

    args = parser.parse_args()

    file_path = args.inputpath
    quantity = args.quantity
    output_path = args.outputpath
    driver_option = args.driver
    proxy = args.proxy

    subreddits = rps.read_file(file_path)
    driver = rps.setup_driver(driver_option, proxy)
    
    for subreddit_link in subreddits:
        print(f"\nStarting with {subreddit_link}.\n")
        imagelinks = rps.fetch_imagelinks(driver, subreddit_link, quantity)
        rps.downloading_imagelinks(imagelinks, output_path)