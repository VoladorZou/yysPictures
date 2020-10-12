import requests
import re
from urllib import error
import urllib.request
#此程序为CSDN作者C-V coder所著
#请求
url = 'https://yys.163.com/media/picture.html'
data = requests.get(url)
#解析
regex = re.compile('.*?href="(.*?)1920x1080.jpg"')
urls=regex.findall(data.text)
#保存
''' 封装成函数方便使用'''
def download(url,index):
    try:
        response = urllib.request.urlopen(url)
        yys = response.read()
        fname = str(index) + '.jpg'
        with open('./Pictures/'+fname, 'wb')as f:
            f.write(yys)
    except error.HTTPError as e:
        print("图片"+str(index)+"不存在")
    
i=0
for lis in urls:
    li = lis+'1920x1080.jpg'
    i+=1
    download(li,i)
#别人的程序确实写的比我的好。正则表达式很强大，亏在当初缺乏耐心。