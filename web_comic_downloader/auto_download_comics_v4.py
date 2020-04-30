#!/usr/bin/env python3
#  auto_download_comics_v4.py - Automatically download from websites
# Python - Automate the Boring Stuff, pg 253
# Author: octarine123
# Error handling goal If no host supplied then skip to next
# PEP8 Style compliant according to pystylecode module


import webbrowser
import sys
import requests
import bs4
import os
import logging
import time
comic_file = 'xkcd_v4'
url = 'https://xkcd.com/'

# ISSUES - there is an issue w/ comics: 2067, 1525
# requests.exceptions.InvalidURL:
# Invalid URL "http: /2067/asset/challengers_header.png": No host supplied
# url = "https: //xkcd.com/" homepage url
os.makedirs(comic_file, exist_ok=True)
num_comics = 0

# Create Logger
logging.basicConfig(filename='auto_download_comics_v4_log.txt',
                    level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s'
                    )

logger = logging.getLogger()

print(logger.level)


def check_url():
    res_1 = requests.get(url)
    print('Checking url...', url)
    try:
        res_1.raise_for_status()
        logger.info('url check complete')
        print('url check complete')
    except Exception as exc:
        print('There was a problem: %s' % (exc))
        logger.error('There was an issue with the url')


def find_next():
    # Get previous button's url
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')


def download(url):
    try:
        global num_comics
        while not url.endswith('#'):
            num_comics += 1
            print('Downloading page %s...' % url)
            # Step 1: Download the page.
            res = requests.get(url)
            soup = bs4.BeautifulSoup(res.text, 'html.parser')
            comicElm = soup.select('#comic img')
            # Step 2: Find url of the comic image
            logger.info('Step 1 Complete')
            if comicElm == []:
                print('Could not find comic image')
            else:
                comic_url = 'http:' + comicElm[0].get('src')
                print('Comic URL...', comic_url)
                print('Downloading image %s...' % (comic_url))
                res = requests.get(comic_url)
                res.raise_for_status()
                logger.info('Step 2 Complete')

                imageFile = open(os.path.join(comic_file,
                                              os.path.basename(comic_url)),
                                 'wb')
                logger.info('Step 3 initiated')
                for chunk in res.iter_content(100000):
                    imageFile.write(chunk)
                    logger.info('File written')
                imageFile.close()
                print(comic_url, ' Downloaded.')
                logger.info('Step 3 complete')
                print(num_comics, 'Comics Downloaded.')

            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prevLink.get('href')
            logger.info('Step 4 complete')
            check_url()
    except requests.exceptions.InvalidURL:
        logger.error('Exception tripped')
        print('Error with url ', url)
        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'http://xkcd.com' + prevLink.get('href')
        logger.info('comic skipped')
        print('Comic skipped. moving onto url:,', url)
        download(url)
    finally:
        print('Done.', num_comics, 'Comics downloaded in total.')


def main():
    global url
    check_url()
    download(url)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Program aborted.')
        raise SystemExit
