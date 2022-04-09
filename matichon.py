# matichon.py

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.matichon.co.th/bkkpataya/governorbkk'
#url = 'https://www.matichon.co.th/politics'

webopen = urlopen(url)
pagehtml = webopen.read().decode('utf-8')
webopen.close()

# start = pagehtml.find('<title>') + len('<title>')
# end = pagehtml.find('</title>')
# print(pagehtml[start:end])

data = BeautifulSoup(pagehtml,'html.parser')
# print([data.get_text().replace('\n',' ')])

title = data.find_all('h3',{'class':'entry-title td-module-title'}) #หลายหัวข้อออกมาเป็นลิสต์

message = ''

for t in title:
	# print(t.a['title'])
	# print(t.a['href'])
	# print('------')
	message = message + t.a['title'] + '\n'
	message = message + t.a['href'] + '\n\n'

print(message)

import songline
token = 'Lsee35a6GlC2RNbxEtQ4cWiKPglvPPnADpY4PE4DI0y'
messenger = songline.Sendline(token)
messenger.sendtext(message)

