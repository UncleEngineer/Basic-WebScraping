# shell - oilprice

from urllib.request import urlopen
from bs4 import BeautifulSoup


def Shell():
	url = 'https://www.shell.co.th/th_th/motorists/shell-fuels/fuel-price/app-fuel-prices.html'

	webopen = urlopen(url)
	pagehtml = webopen.read().decode('utf-8')
	webopen.close()

	data = BeautifulSoup(pagehtml,'html.parser')
	# print(data.get_text().replace('\n',' '))

	table = data.find('table',{'class':'cc_cursor'})
	allrow = table.find_all('tr')

	result = []

	for r in allrow[1:]:
		column = r.find_all('td')
		oiltype = column[0].text.replace(':','')
		price = column[1].text
		result.append([oiltype,float(price)])

	return result

res = Shell()
print(res)