# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from SHWeather import settings


class ShweatherPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            port=settings.MYSQL_PORT,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            db=settings.MYSQL_DATABASE,
            use_unicode=True,
            charset="utf8"
        )
        self.cursor = self.connect.cursor()
        self.table_name = settings.MYSQL_TABLE

    def process_item(self, item, spider):
        try:
            sql = 'INSERT INTO %s(`time`, `wea_from`, `wea_to`, `tem_from`, `tem_to`, `win_from`, `win_to`) ' \
                  'VALUES("%s", "%s", "%s", %s, %s, "%s", "%s")' % (self.table_name,
                                                                    item['time'], item['wea_from'],
                                                                    item['wea_to'], item['tem_from'],
                                                                    item['tem_to'], item['win_from'], item['win_to'])
            print(sql)
            self.cursor.execute(sql)
            self.connect.commit()
        except Exception as ex:
            print(ex)
        return item
