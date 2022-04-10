from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys #คีย์บอร์ด
import time



# ระบุตำแหน่งของ webdriver
#path = r'C:\Users\Uncle Engineer\Desktop\Python Bootcamp 2022\Web Scraping\chromedriver_win32\chromedriver.exe'
#ser = Service(path)

'''
options = webdriver.ChromeOptions()
# options.headless = True
# options.add_argument("start-maximized")
options.add_argument('--enable-javascript')

# สร้าง driver
driver = webdriver.Chrome(service=ser,options=options)

# url เริ่มต้น
url = 'https://pantip.com/forum/blueplanet'
driver.get(url)
'''

from bs4 import BeautifulSoup
from urllib.request import urlopen

#print(driver.page_source)
# url = 'https://pantip.com/forum/blueplanet'
url = 'https://pantip.com/forum/sinthorn'
webopen = urlopen(url)
html = webopen.read().decode('utf-8')
webopen.close()

# html = driver.page_source
data = BeautifulSoup(html, 'html.parser')
# print(data.get_text())

data = data.find('div',{'id':'pt-topic-left'})

forum = data.find_all('a',{'class':'gtm-latest-topic gtm-topic-layout-compact gtm-topic-type-filter-all'})

count = 1

for f in forum:
	if f.i != None:
		print('No.',count)
		print(f.text)
		print(f['href'])
		count = count + 1
		detailurl = f['href']
		webopen = urlopen(detailurl)
		html = webopen.read().decode('utf-8')
		webopen.close()
		data = BeautifulSoup(html, 'html.parser')
		detail = data.find('div',{'class':'display-post-story'})
		print('====')
		print(detail.text.strip().replace('\xa0',''))

		print('-----')

print('COUNT:',len(forum))