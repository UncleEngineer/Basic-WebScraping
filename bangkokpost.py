

from urllib.request import urlopen
from bs4 import BeautifulSoup


def BangkokPost(cat='business'):
	url = 'https://www.bangkokpost.com/{}/'.format(cat)

	webopen = urlopen(url)
	pagehtml = webopen.read().decode('utf-8')
	webopen.close()

	data = BeautifulSoup(pagehtml,'html.parser')
	# print(data.get_text().replace('\n',' '))

	news_row = data.find_all('div',{'class':'listnews-text'})
	# print(news_row[0].h3.a['href'])

	result = []

	for n in news_row:
		title = n.h3.text
		detail = n.p.text
		link = 'https://www.bangkokpost.com'+ n.h3.a['href']
		print(title)
		print(detail)
		print(link)
		result.append([title,detail,link])
		print('--------')

	return result

BangkokPost('tech')