from lxml import etree
import pandas as pd
import requests
from tqdm import tqdm

pattern = '//td[@class="listbg"]/a/@href'
url = 'https://www.taptap.com/app/168332/review?order=default&page=244'
article_urls=[]
r = requests.get(url)

html = etree.HTML(r.content)
article_urls = html.xpath("//i[@class='colored']/@style")
# article_urls.fromkeys()
# article_urls = list(set(article_urls))
# print(article_urls)
# article_urls.remove('/Article/ShowClass.asp?ClassID=3')


title_p = '//div[@class="main_articletitle "]/text()'
# content_p='//div[@id=fontzoom]//p[2]/text()'
content_p='//p[@class="MsoNormal"]//text()'
title =[]
content=[]
new_base = 'http://www.shibei.edu.sh.cn'
for a in tqdm(article_urls):
    new_url = new_base + str(a)
    r = requests.get(new_url)
    if(r.ok):
        # print(r.content)
        html=etree.HTML(r.content)
        a = html.xpath(content_p)
        a = "".join(a)
        # b = a.xpath('string()')
        title.append(html.xpath(title_p))
        content.append(a)
data = pd.DataFrame({'title':title,'content':content})
data.to_csv('jiang.csv')