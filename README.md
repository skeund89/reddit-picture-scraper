# Reddit Picture Scraper

## Introduction

The Reddit Picture Scraper is a Python application designed to fetch and download images from specified subreddits. It utilizes web scraping techniques to extract image URLs from Reddit's HTML structure and downloads them to a local directory specified by the user.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
  - [Arguments](#arguments)
  - [Example](#example)
- [Implementation Details](#implementation-details)
- [Important Notes](#important-notes)
- [Example File Format](#example-file-format)

## Installation

To install and run the Reddit Picture Scraper, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/skeund89/reddit-picture-scraper.git
   cd reddit-picture-scraper
   ```

2. Install dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the Reddit Picture Scraper, execute the `main.py` script with the appropriate arguments:

```bash
python main.py -ip <inputpath> -q <quantity> -op <outputpath> -d <driver> [-p <proxy>]
```

### Arguments

- `-ip`, `--inputpath` (required): Path to a file containing subreddit links (in the format used by old Reddit).
- `-q`, `--quantity` (required): Number of pictures to download per subreddit.
- `-op`, `--outputpath` (required): Path where the downloaded pictures should be saved.
- `-d`, `--driver` (required): Web driver to be used for scraping (choices: "Safari", "Chrome", "Firefox").
- `-p`, `--proxy` (optional): Proxy server in the format `ip:port`.

### Example

```bash
python main.py -ip subreddits.txt -q 100 -op ./images -d Chrome -p 127.0.0.1:8080
```

This will read subreddit links from `subreddits.txt`, download 100 pictures per subreddit, and save them to the `./images` directory using the Chrome web driver and the specified proxy.

## Implementation Details

The script performs the following steps:

1. **Reading Subreddit Links**: Reads all subreddit links from the provided file.
2. **Fetching Image Links**: For each subreddit link, fetches the specified number of image links using the specified web driver.
3. **Downloading Images**: Downloads each image from the fetched image links to the specified output directory.

## Important Notes

- The proxy argument is optional. If not provided, the script will connect directly without using a proxy.

## Example File Format

The input file containing subreddit links should have one link per line, for example:

```
https://old.reddit.com/r/pics/
https://old.reddit.com/r/aww/
https://old.reddit.com/r/funny/
```