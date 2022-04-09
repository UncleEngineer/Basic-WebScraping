# stock-table.py

# https://www.settrade.com/C04_02_stock_historical_p1.jsp?txtSymbol=PTT&selectPage=2&max=180&offset=0

from urllib.request import urlopen
from bs4 import BeautifulSoup

# GRAPH
import matplotlib.pyplot as plt

def HistoralStock(CODE,days=180):

	url = 'https://www.settrade.com/C04_02_stock_historical_p1.jsp?txtSymbol={}&selectPage=2&max={}&offset=0'.format(CODE,days)

	webopen = urlopen(url)
	pagehtml = webopen.read()
	webopen.close()

	data = BeautifulSoup(pagehtml,'html.parser')

	# print(data.get_text())

	table = data.find('table',{'class':'table table-info table-hover'})
	# ถ้ามี table ที่มีชื่อคลาสนี้แค่คลาสเดียว สามารถใช้ .find ได้ ซึ่งจะออกมาแค่ 1 รายการ ไม่ต้องรันลูป

	table = table.find_all('tr')[1:]
	# print(table)

	result = []

	for row in table:
		#print(row)
		column = row.find_all('td')
		#print(column)
		cl = []
		for i,c in enumerate(column):
			if i!= 0:
				cl.append(float(c.text.replace(',','')))
			else:
				cl.append(c.text)
		#print(cl)
		result.append(cl)
		#print('----')

	return result

result = HistoralStock('PTT',10)
print(result)

price = []
day = []

for rs in result:
	price.append(rs[5])
	day.append(rs[0])

print(price)

x = range(len(price))

# สลับข้อมูลจากหน้าไปหลังจากหลังไปหน้า
price.reverse()
day.reverse()

plt.plot(x,price)
plt.xticks(x,day)
plt.show()