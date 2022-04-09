# sendline.py
# pip install songline

import songline

token = 'Lsee35a6GlC2RNbxEtQ4cWiKPglvPPnADpY4PE4DI0y'

messenger = songline.Sendline(token)

#messenger.sendtext('hello world')
#messenger.sendimage('https://todaysayhi.com/wp-content/uploads/2020/08/S__1876005-819x1024.jpg')
messenger.sticker(116,1)