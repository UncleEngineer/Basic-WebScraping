# twitter

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys #คีย์บอร์ด
import time
from bs4 import BeautifulSoup

# ระบุตำแหน่งของ webdriver
path = r'C:\Users\Uncle Engineer\Desktop\Python Bootcamp 2022\Web Scraping\chromedriver_win32\chromedriver.exe'
ser = Service(path)

# รันแบบไม่ต้องเปิด google chrome
# opt = webdriver.ChromeOptions()
# opt.add_argument('headless')

options = webdriver.ChromeOptions()
options.headless = True
# options.add_argument("start-maximized")
options.add_argument('--enable-javascript')

# สร้าง driver
driver = webdriver.Chrome(service=ser,options=options)

# url เริ่มต้น
# url = 'https://twitter.com/bbcworld'
# url = 'https://twitter.com/Thairath_News'
url = 'https://twitter.com/MatichonOnline'
driver.get(url)

time.sleep(5)
# css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0

#############LOAD DATA###########
start = 20000 #เริ่มต้นครั้งแรก
end = 80001 # เพิ่มจำนวนนี้เพื่อให้ได้ผลลัพธ์มากขึ้น
step = 20000 # ขยับไปครั้งละ 20,000

for i in range(start,end,step):
	driver.execute_script('window.scrollTo(0,{})'.format(i)) # รันสคริปให้ขยับลงมา
	time.sleep(3)
	html = driver.page_source
	data = BeautifulSoup(html, 'html.parser')
	# print(data.get_text())

	post = data.find_all('span',{'class':'css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'})

	prev = ''

	result_post = []

	for p in post:
		if prev == '·':
			#print(p.text)
			result_post.append(p.text)
			#print('-------------')
		prev = p.text

	#print('=============LINK=============')
	link = data.find_all('a',{'class':'css-4rbku5 css-18t94o4 css-901oao r-14j79pv r-1loqt21 r-1q142lx r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-3s2u2q r-qvutc0'})

	result_link = []

	for l in link:
		#print(l)
		result_link.append( 'https://twitter.com' + l['href'] )
		#print('-----')
	#print('=============================')

	for i,(x,y) in enumerate(zip(result_post,result_link),start=1):
		print(i)
		print(x)
		print(y)
		print('---------')