#!/usr/bin/python3
# encoding: utf-8
"""
@version: 3.52
@author: Uxeix
@license: Apache Licence 
@contact: Uxeixs@gmail.com
@site: https://github.com/uxiexs
@software: PyCharm
@file: vo73_xmlTest.py.py
@time: 2016/11/20 14:48
"""
# 利用SAX编写程序解析Yahoo的XML格式的天气预报，获取当天和第二天的天气：
# https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22changsha%2C%20china%22)%20and%20u%3D%27c%27%20&format=xml&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeysw%2C%20scotland%22)%20and%20u%3D%27c%27%20&format=xml&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys
# 参数w是城市代码，要查询某个城市代码，可以在weather.yahoo.com搜索城市，浏览器地址栏的URL就包含城市代码。

data = '''
<query xmlns:yahoo="http://www.yahooapis.com/v1/base.rng" yahoo:count="1" yahoo:created="2016-11-20T07:59:36Z" yahoo:lang="en-US">
<results>
<channel>
<yweather:units xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" distance="km" pressure="mb" speed="km/h" temperature="C"/>
<title>Yahoo! Weather - Changsha, Hunan, CN</title>
<link>
http://us.rd.yahoo.com/dailynews/rss/weather/Country__Country/*https://weather.yahoo.com/country/state/city-26198213/
</link>
<description>Yahoo! Weather for Changsha, Hunan, CN</description>
<language>en-us</language>
<lastBuildDate>Sun, 20 Nov 2016 03:59 PM CST</lastBuildDate>
<ttl>60</ttl>
<yweather:location xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" city="Changsha" country="China" region=" Hunan"/>
<yweather:wind xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" chill="59" direction="320" speed="17.70"/>
<yweather:atmosphere xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" humidity="89" pressure="34202.54" rising="0" visibility="25.91"/>
<yweather:astronomy xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" sunrise="6:55 am" sunset="5:33 pm"/>
<image>
<title>Yahoo! Weather</title>
<width>142</width>
<height>18</height>
<link>http://weather.yahoo.com</link>
<url>
http://l.yimg.com/a/i/brand/purplelogo//uh/us/news-wea.gif
</url>
</image>
<item>
<title>Conditions for Changsha, Hunan, CN at 03:00 PM CST</title>
<geo:lat xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">28.252029</geo:lat>
<geo:long xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">113.067749</geo:long>
<link>
http://us.rd.yahoo.com/dailynews/rss/weather/Country__Country/*https://weather.yahoo.com/country/state/city-26198213/
</link>
<pubDate>Sun, 20 Nov 2016 03:00 PM CST</pubDate>
<yweather:condition xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="26" date="Sun, 20 Nov 2016 03:00 PM CST" temp="16" text="Cloudy"/>
<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="39" date="20 Nov 2016" day="Sun" high="18" low="15" text="Scattered Showers"/>
<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="26" date="21 Nov 2016" day="Mon" high="18" low="15" text="Cloudy"/>
<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="39" date="22 Nov 2016" day="Tue" high="16" low="5" text="Scattered Showers"/>
<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="39" date="23 Nov 2016" day="Wed" high="5" low="2" text="Scattered Showers"/>
<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="28" date="24 Nov 2016" day="Thu" high="6" low="1" text="Mostly Cloudy"/>
<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="28" date="25 Nov 2016" day="Fri" high="7" low="4" text="Mostly Cloudy"/>
<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="30" date="26 Nov 2016" day="Sat" high="8" low="5" text="Partly Cloudy"/>
<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="30" date="27 Nov 2016" day="Sun" high="12" low="5" text="Partly Cloudy"/>
<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="30" date="28 Nov 2016" day="Mon" high="9" low="5" text="Partly Cloudy"/>
<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="30" date="29 Nov 2016" day="Tue" high="8" low="4" text="Partly Cloudy"/>
<description>
<![CDATA[<img src="http://l.yimg.com/a/i/us/we/52/26.gif"/> <BR /> <b>Current Conditions:</b> <BR />Cloudy <BR /> <BR /> <b>Forecast:</b> <BR /> Sun - Scattered Showers. High: 18Low: 15 <BR /> Mon - Cloudy. High: 18Low: 15 <BR /> Tue - Scattered Showers. High: 16Low: 5 <BR /> Wed - Scattered Showers. High: 5Low: 2 <BR /> Thu - Mostly Cloudy. High: 6Low: 1 <BR /> <BR /> <a href="http://us.rd.yahoo.com/dailynews/rss/weather/Country__Country/*https://weather.yahoo.com/country/state/city-26198213/">Full Forecast at Yahoo! Weather</a> <BR /> <BR /> (provided by <a href="http://www.weather.com" >The Weather Channel</a>) <BR /> ]]>
</description>
<guid isPermaLink="false"/>
</item>
</channel>
</results>
</query>
'''
from xml.parsers.expat import ParserCreate

class WeatherSaxHandler(object):
    def __init__(self):
        self.result = {'yweather:forecast': {}}
        self.count = 0
    def start_element(self, name, attrs):
        if name == 'yweather:location':
            self.result['yweather:location'] = attrs
        if name == 'yweather:forecast':
            self.count += 1
            if self.count <= 2:
                self.result['yweather:forecast'][str(self.count)] = attrs
            else:
                pass
def parse_weather(xml):
    handler = WeatherSaxHandler()
    parser = ParserCreate()
    # parser.returns_unicode = False
    parser.StartElementHandler = handler.start_element
    parser.Parse(xml)
    weather = {'today': {}, 'tomorrow': {}}
    weather['city'] = handler.result['yweather:location']['city']
    weather['country'] = handler.result['yweather:location']['country']
    weather['today']['text'] = handler.result['yweather:forecast']['1']['text']
    weather['today']['low'] = handler.result['yweather:forecast']['1']['low']
    weather['today']['high'] = handler.result['yweather:forecast']['1']['high']
    weather['tomorrow']['text'] = handler.result['yweather:forecast']['2']['text']
    weather['tomorrow']['low'] = handler.result['yweather:forecast']['2']['low']
    weather['tomorrow']['high'] = handler.result['yweather:forecast']['2']['high']
    return weather

weather = parse_weather(data)
print('weather:')
print('city: %s' % weather['city'])
print('country: %s' % weather['country'])
print('today: {%s, low: %s, high: %s}' % (weather['today']['text'],weather['today']['low'],weather['today']['high']))
print('tomorrow: {%s, low: %s, high: %s}' % (weather['tomorrow']['text'], weather['tomorrow']['low'], weather['tomorrow']['high']))
print(weather)