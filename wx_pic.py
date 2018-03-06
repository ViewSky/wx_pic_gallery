# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from wxpy import *
#import pickle
import PIL.Image as Image
import math

bot=Bot()

all_friend = bot.friends()

x = len(all_friend)
#with open('contacts.pkl','wb') as f:
#    pickle.dump(all_friend,f)
count = 0


for i in all_friend:
    try:
        i.get_avatar(save_path='images/'+str(count)+'.jpg')
        count =  count +  1 
    except:
        pass
numPic = count

#for i in range(1,2):
#    temp = all_friend[i]
#    temp.send(u'炸个稀巴烂之过个旺年~小天')
#    sleep(1)
# get_avatar(save_path=None)

#with open('contacts.pkl','rb') as f:
#    x = pickle.load(f)
eachsize = int(math.sqrt(float(640 * 640) / numPic))
numline = int(640 / eachsize)

toImage = Image.new('RGB', (640, 640))
x = 0
y = 0
for i in range(numPic):
	try:
		#打开图片
		img = Image.open('images/'+str(i) + ".jpg")
        
	except IOError:
		print("Error: 没有找到文件或读取文件失败")
	else:
		#缩小图片
		img = img.resize((eachsize, eachsize), Image.ANTIALIAS)
		#拼接图片
		toImage.paste(img, (x * eachsize, y * eachsize))
		x += 1
		if x == numline:
			x = 0
			y += 1

toImage.save("all.jpg")

bot.logout()
