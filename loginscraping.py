# loginscraping.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys #คีย์บอร์ด

# ระบุตำแหน่งของ webdriver
path = r'C:\Users\Uncle Engineer\Desktop\Python Bootcamp 2022\Web Scraping\chromedriver_win32\chromedriver.exe'
ser = Service(path)

# รันแบบไม่ต้องเปิด google chrome
opt = webdriver.ChromeOptions()
opt.add_argument('headless')

# สร้าง driver
driver = webdriver.Chrome(service=ser, options=opt)

# url เริ่มต้น
url = 'http://uncle-machine.com/login/'
driver.get(url)

# ค้นหา element ในการล็อกอิน
username =  driver.find_element(By.ID, 'username')
username.send_keys('EMAIL')

password =  driver.find_element(By.ID, 'password')
password.send_keys('PASSWORD')

# password.send_keys(Keys.RETURN)

# Button by xpath
btn_xpath = '/html/body/div[2]/form/button'
btn = driver.find_element(By.XPATH, btn_xpath)
btn.click()

###########SENSOR#############
url_sensor = 'http://uncle-machine.com/sensor/'
driver.get(url_sensor)

sid = driver.find_element(By.NAME,'sid')
sid.send_keys('TM-1001')
sid.send_keys(Keys.RETURN) # กดปุ่ม Enter

############หาด้วย selenium#############
temp = driver.find_element(By.CLASS_NAME, 'temp')
humid = driver.find_element(By.CLASS_NAME, 'humid')
print('{} {}'.format(temp.text, humid.text))

############หาด้วย bs4 #############
from bs4 import BeautifulSoup
html = driver.page_source # แสดง source html
data = BeautifulSoup(html,'html.parser')

temp2 = data.find('div',{'class':'temp'}).text # .find หาผลลัพธ์เดียว
humid2 = data.find('div',{'class':'humid'}).text

print('{} {}'.format(temp2, humid2))

print('----------------')

print(data.get_text())

text = data.get_text()

with open('export.txt','w',encoding='utf-8') as file:
	file.write(text)

driver.close() #ปิด driver