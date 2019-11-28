# import requests
# from lxml import etree
# import time
# import urllib
# header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
# url = 'https://pixabay.com/images/search/cat/?pagi=1'
# r = requests.get(url,headers=header).text
# s = etree.HTML(r)
# q=s.xpath('//img/@data-lazy')
# for i in q:
#         imglist = i.replace('__340', '_960_720')
#         # print(imglist)
#         name = imglist.split('/')[-1]#图片名称
#         # print(name)
#         urllib.request.urlretrieve(imglist,name)
#         time.sleep(1)
import os
import requests
from lxml import html
import time
import urllib
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# 禁用安全请求警告、
# os.mkdir('meizi')#第一次运行新建meizi文件夹，手动建可以注释掉

for page in range(1,852):
    url='http://www.mmonly.cc/mmtp/list_9_%s.html'%page
    # url = 'https://pixabay.com/zh/images/search/cat/?pagi=%s' % page
    print(url)
    response=requests.get(url,verify=False).text

    selector=html.fromstring(response)
    imgEle=selector.xpath('//div[@class="ABox"]/a')
    print(len(imgEle))
    for index,img in enumerate(imgEle):
        imgUrl=img.xpath('@href')[0]
        response=requests.get(imgUrl,verify=False).text
        selector = html.fromstring(response)
        pageEle = selector.xpath('//div[@class="wrapper clearfix imgtitle"]/h1/span/span[2]/text()')[0]
        print(pageEle)
        imgE=selector.xpath('//a[@class="down-btn"]/@href')[0]

        imgName = '%s_%s_1.jpg' % (page,str(index+1))
        coverPath = '%s/meizi/%s' % (os.getcwd(), imgName)
        urllib.request.urlretrieve(imgE, coverPath)

        for page_2 in range(2,int(pageEle)+1):
            url=imgUrl.replace('.html', '_%s.html' % str(page_2))
            response = requests.get(url).text
            selector = html.fromstring(response)
            imgEle = selector.xpath('//a[@class="down-btn"]/@href')[0]
            print(imgEle)
            imgName='%s_%s_%s.jpg'%(page,str(index+1),page_2)
            coverPath = '%s/meizi/%s' % (os.getcwd(), imgName)
            urllib.request.urlretrieve(imgEle, coverPath)
    time.sleep(2)