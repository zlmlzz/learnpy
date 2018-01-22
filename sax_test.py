# -*- coding: utf-8 -*-


###这边没看懂，所以代码是搜的，不是我自己写的


from xml.parsers.expat import ParserCreate
from urllib import request
import time


class DefaultSaxHandler(object):
    def __init__(self):
        self.location = {}
        self.forecast = []


    def start_element(self, name, attrs):
        if name == 'yweather:location':
            self.location = attrs
        if name == 'yweather:forecast':
            data = {}
            date = time.strftime('%Y-%m-%d' , time.strptime(attrs['date'],'%d %b %Y'))
            data['date'] = date
            data['high'] = attrs['high']
            data['low'] = attrs['low']
            self.forecast.append(data)

    def end_element(self, name):
        pass


    def char_data(self, text):
        pass



def parseXml(xml_str):
    handler = DefaultSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml_str)
    return {
        'city': handler.location['city'],
        'forecast': handler.forecast
    }

# 测试:
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
assert result['city'] == 'Beijing'
print('ok')