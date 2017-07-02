import scrapy
import lxml.html
from ..basefunc import GetDateStamp
from ..items import ShweatherItem


class MobikeSpider(scrapy.Spider):

    name = "weather"

    start_urls = [
        'http://www.weather.com.cn/weather1d/101020100.shtml'
    ]

    def parse(self, response):
        html = response.body.decode('utf-8')
        tree = lxml.html.fromstring(html)
        # weather
        weainfo = tree.cssselect('p.wea')
        wea_from = weainfo[0].text
        wea_to = weainfo[1].text
        print('Weather From {} To {}'.format(wea_from, wea_to))
        # temperature
        teminfo = tree.cssselect('p.tem')
        tem_from = teminfo[0].text
        tem_to = teminfo[1].text
        print('Temperature From {} To {}'.format(tem_from, tem_to))
        # wind
        wininfo = tree.cssselect('p.tem > span')
        win_from = wininfo[0].text
        win_to = wininfo[1].text
        print('Wind From {} To {}'.format(win_from, win_to))

        item = ShweatherItem()
        item['time'] = GetDateStamp()
        yield item



