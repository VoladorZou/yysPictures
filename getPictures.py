from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib import request

import json
import time

#任务：爬取阴阳师官网的原画壁纸
def main():
    browser = webdriver.Chrome()
    browser.implicitly_wait(200)#这是延时等待。由于网速时快时慢，而get方法会在网页框架加载结束后停止执行，
    #这就会导致有些时候我们打算获取的内容还没被加载进来便结束了获取页面数据，最后报错，拿不到想要的数据。
    url = 'https://yys.163.com/media/picture.html'
    browser.get(url)
    #遇到class name中的复合情况（即有多个class name中间是空格隔开的）
    #选取其中一个具有全局唯一性的class name即可准确定位所要查找的结点内容
    Pictures = browser.find_elements_by_class_name('mask')
    x=1
    for Picture in Pictures:
        #对于需要点击才显示出来的页面内容（隐藏内容）需要使用下面的方法获取文本信息
        #result = browser.execute_script("return arguments[0].textContent", Abstract)
        result = Picture.find_element_by_xpath("./a[3]").get_attribute("href")
        print(result)
        #保存图片
        fname = str(x)+'.jpg'
        request.urlretrieve(result, './yysTest/'+fname)
        x+=1

if __name__ == "__main__":
    main()