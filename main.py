from scraper import pictureScraper

if __name__ == "__main__":
    rps = pictureScraper()
    
    file_path = input("Your path to the file with the subreddits: ")
    quantity = input("How much pictures do you want to download for each subreddit (default is 25): ")
    output_path = input("Where should the pictures get saved (path): ")

    subreddits = rps.read_file(file_path)
    
    for subreddit_link in subreddits:
        imagelinks = rps.fetch_imagelinks(subreddit_link, quantity)
        rps.downloading_imagelinks(imagelinks, output_path)

