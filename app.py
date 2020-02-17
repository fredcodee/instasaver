from bs4 import BeautifulSoup
import requests

pic_url="https://www.instagram.com/p/B76TI8zFdYI/"

source = requests.get(pic_url).text
soup = BeautifulSoup(source, 'lxml')
n= soup.find()