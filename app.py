from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from time import sleep
from bs4 import BeautifulSoup as soup

#for headless browser
options = Options()
options.add_argument("--headless")
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")
CHROMEDRIVER_PATH = "C:\\Users\\Windows 10 Pro\\Downloads\\chromedriver"
browser = webdriver.Chrome(CHROMEDRIVER_PATH, options=options)


#get picture link
pic_url = input("paste the url here:")
def get_piclink():
  browser.get(pic_url)
  sleep(1)
  print("Getting picture......")

  http_contents = soup(browser.page_source, "html.parser")
  n = http_contents.find('img', class_='FFVAD')
  return(n['src'])

try:
  get_piclink()
except:
  print("sorry image url not supported or imgae not found")


#download picture
try:
  url=get_piclink()
  filename =url.split("=")[-1]
  filename+=".jpg"
  r = requests.get(url, timeout=0.5)

  if r.status_code == 200:
    with open(filename, 'wb') as f:
      f.write(r.content)
  print("downloaded")
except:
  print("error please try again")


browser.quit()
exit()



#coded by fredcode
