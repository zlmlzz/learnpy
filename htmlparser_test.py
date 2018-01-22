# -*- coding: utf-8 -*-

from html.parser import HTMLParser
import urllib.request, re
l = list()

class MyHTMLParser(HTMLParser):

    _tmp = str()
    _is_data = 0
    _flag = 0
    def handle_starttag(self, tag, attrs):

        if tag == 'ul':
            if re.match(r'list-recent-events', attrs[0][1]):
                self._flag = 1
        if tag == 'li' and self._flag:
            self._is_data = 1
            self._tmp = ''
        if tag == 'a' and self._flag:
            self._tmp += '\n' + '会议名称:'
        if tag == 'time' and self._is_data:
            self._tmp += '时间:'
        if tag == 'span' and self._is_data:
            if attrs[0][1] == 'say-no-more':
                self._tmp += '年:'
            if attrs[0][1] == 'event-location':
                self._tmp += '地址:'

    def handle_endtag(self, tag):
        if tag == 'ul':
            self._flag = 0
        if tag == 'li' and self._flag:
            self._is_data = 0
            l.append(re.split(r'\s+', self._tmp))

    def handle_data(self, data):
        if self._is_data:
            if data:
                self._tmp += data

url = 'https://www.python.org/events/python-events/'
data = urllib.request.urlopen(url).read()
data = data.decode('utf-8')
parser = MyHTMLParser()
parser.feed(data)
for i in l:
    print(''.join(i))
