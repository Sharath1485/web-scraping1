# -*- coding: utf-8 -*-
"""Untitled14.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hhGlyFFvzDnLe-cdFAGkSGpmxtPe3vHD
"""

'''
Name: Sharath Kumar mandalapu
Date created: March 21, 2021
Version of Python: 3.8.8
'''
#script to download image from wikipedia page. 

#import require libraries
import requests
import bs4

#using requests library to get html content from any wikipedia url
res = requests.get("https://en.wikipedia.org/wiki/Mahatma_Gandhi")
#make a soup object from above requests
soup = bs4.BeautifulSoup(res.text, 'lxml')

#getting image tag whose class is thumbimage
image_1 = soup.select('.thumbimage')[0]

#getting url of image from src attribute of above image tag and getting the content using requests library
image_link = requests.get('https:'+image_1['src'])

#saving the content in image files
f = open('image_1.jpg', 'wb')
f.write(image_link.content)
f.close()
from google.colab import files
files.download('image_1.jpg')