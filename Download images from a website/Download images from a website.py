# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 20:29:27 2020
@author: Thinh Le
Reference: https://towardsdatascience.com/how-to-download-an-image-using-python-38a75cfa21c
"""

# Importing necessary modules
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import os 


def readPage(_url):
    response = requests.get(_url)
    htmlData = BeautifulSoup(response.text, 'html.parser')
    return htmlData

def downloadImagesFromUrl(_url, _cssSelector, _fileAttribute):
    '''Download all images from a given url and CSS selector'''

    # get raw HTML text from the URL
    htmlData = readPage(url)
    # find all image tags by the CSS selector
    images = htmlData.select(_cssSelector)
    # download each image to local computer
    count = 1
    for image in images:
        # make image name
        imageName = _fileAttribute['filename'] + str(count) + '.' + _fileAttribute['filetype']
        # if the image source doesn't start with http
        if image['src'].startswith("http") == False:
            image['src'] = 'http:' + image['src']
        # start to download image
        response = requests.get(image['src'])
        # set the output folder and combine with the image name
        outputFileName = os.path.dirname(os.path.realpath(__file__)) + '\\output\\' + imageName
        file = open(outputFileName, "wb")
        file.write(response.content)
        file.close()
        count = count + 1


url = 'https://www.nettruyen.com/truyen-tranh/toi-thang-cap-mot-minh/chap-110/550446'
cssSelector = 'div.reading-detail div[id^="page"] img'
fileAttribute = {
    'filename': 'Solo leveling_Chapter 106_',
    'filetype': 'jpg'
}
downloadImagesFromUrl(url, cssSelector, fileAttribute)

