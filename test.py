# -*- coding: utf-8 -*-
import requests, re, time

root_url = 'http://www.biqugexsw.com/0_508/'
reponse = requests.get(root_url)
reponse.encoding = 'gbk'
html = reponse.text
title_url = re.findall(r'<dd><a href="(.*?)">.*</a></dd>', html)
urls = title_url
for url in urls:
    page_url = 'http://www.biqugexsw.com' + url
    page_reponse = requests.get(page_url)
    page_reponse.encoding = 'gbk'
    page_html = page_reponse.text
    title = re.findall(r'<title> (.*?)_清穿守则_其他小说_笔趣阁小说网</title>', page_html)
    time.sleep(1)
    print(title[0])
    content = re.findall(r'&nbsp;&nbsp;&nbsp;&nbsp;(.*)<br />', page_html)
    time.sleep(1)
    with open('0.txt', 'a', encoding='gbk') as a:
        a.write(title[0] + '\n')
    for line in content:
        try:
            with open('0.txt', 'a', encoding='gbk') as f:
                f.write('  ' + line + '\n')
        except IOError as e:
            raise e

