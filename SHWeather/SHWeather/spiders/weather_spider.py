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
        # temperature
        teminfo = tree.cssselect('p.tem > span')
        tem_from = teminfo[0].text
        tem_to = teminfo[1].text
        # wind
        wininfo = tree.cssselect('p.win > span')
        win_from = wininfo[0].text
        win_to = wininfo[1].text
        # Output
        item = ShweatherItem()
        item['time'] = GetDateStamp()
        item['wea_from'] = wea_from
        item['wea_to'] = wea_to
        item['tem_from'] = tem_from
        item['tem_to'] = tem_to
        item['win_from'] = win_from
        item['win_to'] = win_to
        yield item



