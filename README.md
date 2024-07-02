# Reddit Picture Scraper

## Introduction

The Reddit Picture Scraper is a Python application that uses Selenium to fetch and download images from specified subreddits. It navigates through multiple pages to extract image URLs and saves them to a local directory specified by the user.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

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

To use the Reddit Picture Scraper, execute the `main.py` script and follow the prompts:

```bash
python main.py
```

You will be prompted to provide:
- Path to a file containing subreddit links (in the format used by old Reddit).
- Number of pictures to download per subreddit (default is 25).
- Path where the downloaded pictures should be saved.

The script will then fetch images from each subreddit link provided in the file and save them to the specified output path.
