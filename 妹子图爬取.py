#!/usr/bin/env python
#-*-coding:utf-8-*-
__author__ = 'lvyiny'

import requests
import re
import time
import os
#妹子图抓取http://www.meizitu.com
header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
for i in range(1,73):
    url = 'http://www.meizitu.com/a/more_{}.html'.format(i)     #打开列表页
    open_url = requests.get(url)
    open_url.encoding = 'gb2312'
    html = open_url.text
    data = re.findall('_blank\' href="(.*?)">.*?<b>(.*?)</b>',html)     #筛选列表页中的链接
    #print(data)

    for x,y in data:
        open_data = requests.get(x,headers = header)     #打开列表页中的链接
        open_data.encoding = 'gb2312'
        open_data_text = open_data.text
        data_re = re.findall('<img alt="(.*?)" src="(.*?)" />',open_data_text)   #提取图片
        #print(data_re)
        os.mkdir(y)
        os.chdir(y)
        for a,b in data_re:
            down_url = requests.get(b,headers = header)
            time.sleep(0.5)
            with open (a + '.jpg','wb') as f:           #保存图片
                f.write(down_url.content)
        os.chdir('../')