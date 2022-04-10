
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys #คีย์บอร์ด
import time

# ระบุตำแหน่งของ webdriver
path = r'C:\Users\Uncle Engineer\Desktop\Python Bootcamp 2022\Web Scraping\chromedriver_win32\chromedriver.exe'
ser = Service(path)

# รันแบบไม่ต้องเปิด google chrome
opt = webdriver.ChromeOptions()
opt.add_argument('headless')

# สร้าง driver
driver = webdriver.Chrome(service=ser, options=opt)

# url เริ่มต้น
url = 'https://www.pttor.com/th/oil_price'
driver.get(url)

allresult = []

for i in range(2,5):
	# range(2,5) เลือกดรอปดาวจาก 2-5 ต้องเช็ค xpath
	dropdown = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/section/div[2]/div/div/div[2]/form/div[2]/select/option[{}]'.format(i))
	dropdown.click()
	time.sleep(1) #รอเวลาประมวลผล
	table = driver.find_element(By.TAG_NAME,'table')
	row = table.find_elements(By.TAG_NAME,'tr')

	for r in row:
		column = r.find_elements(By.TAG_NAME,'td')
		day = []
		for c in column:
			# print(c.text)
			day.append(c.text)
		# print(day)
		if len(day) != 0:
			allresult.append(day)

	#print(table.text)
	print('-------------')

print(allresult)

driver.close()