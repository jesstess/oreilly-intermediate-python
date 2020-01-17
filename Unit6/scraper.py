# From the archive, follow each link, find an image in that page, download the image

# Concepts:
# 1. Downloading stuff => urllib
# 2. Parsing stuff out of HTML => BeautifulSoup

# Download the index page
import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import os

base_url = "https://apod.nasa.gov/apod/archivepix.html"
download_directory = "apod_pictures"
content = urllib.request.urlopen(base_url).read()

image_count = read("How many images to download?\n> ")
img_count = 0

# For each link on the Index page:
for link in BeautifulSoup(content, "lxml").findAll("a"):
    print("Following link:", link)
    href = urljoin(base_url, link["href"])
    #   Follow the link and pull down the image on that linked page
    page = urllib.request.urlopen(href).read()
    for img in BeautifulSoup(page, "lxml").findAll("img"):
        img_href = urljoin(href, img["src"])
        print("Downloading image:", img_href)
        img_name = img_href.split("/")[-1]
        urllib.request.urlretrieve(img_href, os.path.join(download_directory, img_name))
        img_count += 1
        if img_count == image_count:
            print("Finished Downloading " + str(img_count) + " images.")
