# 数据爬取文件

import scrapy
import pymysql
#import pymssql
from ..items import WangyixinwenItem
import time
from datetime import datetime,timedelta
import re
import random
import platform
import json
import os
import urllib
from urllib.parse import urlparse
import requests
import emoji

# 网易新闻
class WangyixinwenSpider(scrapy.Spider):
    name = 'wangyixinwenSpider'
    spiderUrl = 'https://news.163.com/special/cm_guonei/?callback=data_callback'
    start_urls = spiderUrl.split(";")
    protocol = ''
    hostname = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def start_requests(self):

        plat = platform.system().lower()
        if plat == 'linux' or plat == 'windows':
            connect = self.db_connect()
            cursor = connect.cursor()
            if self.table_exists(cursor, '72ti7_wangyixinwen') == 1:
                cursor.close()
                connect.close()
                self.temp_data()
                return

        pageNum = 1 + 1
        for url in self.start_urls:
            if '{}' in url:
                for page in range(1, pageNum):
                    next_link = url.format(page)
                    yield scrapy.Request(
                        url=next_link,
                        callback=self.parse
                    )
            else:
                yield scrapy.Request(
                    url=url,
                    callback=self.parse
                )

    

    # 数据库连接
    def db_connect(self):
        type = self.settings.get('TYPE', 'mysql')
        host = self.settings.get('HOST', 'localhost')
        port = int(self.settings.get('PORT', 3306))
        user = self.settings.get('USER', 'root')
        password = self.settings.get('PASSWORD', '123456')

        try:
            database = self.databaseName
        except:
            database = self.settings.get('DATABASE', '')

        if type == 'mysql':
            connect = pymysql.connect(host=host, port=port, db=database, user=user, passwd=password, charset='utf8')
        else:
            connect = pymysql.connect(host=host, port=port, db=database, user=user, passwd=password, charset='utf8')
            #connect = pymssql.connect(host=host, user=user, password=password, database=database)

        return connect

    # 断表是否存在
    def table_exists(self, cursor, table_name):
        cursor.execute("show tables;")
        tables = [cursor.fetchall()]
        table_list = re.findall('(\'.*?\')',str(tables))
        table_list = [re.sub("'",'',each) for each in table_list]

        if table_name in table_list:
            return 1
        else:
            return 0

    # 数据缓存源
    def temp_data(self):

        connect = self.db_connect()
        cursor = connect.cursor()
        sql = '''
            insert into `wangyixinwen`(
                id
                ,laiyuan
                ,biaoti
                ,fengmian
                ,laizi
                ,gentie
                ,guanjianzi
                ,fabushijian
                ,detail
            )
            select
                id
                ,laiyuan
                ,biaoti
                ,fengmian
                ,laizi
                ,gentie
                ,guanjianzi
                ,fabushijian
                ,detail
            from `72ti7_wangyixinwen`
            where(not exists (select
                id
                ,laiyuan
                ,biaoti
                ,fengmian
                ,laizi
                ,gentie
                ,guanjianzi
                ,fabushijian
                ,detail
            from `wangyixinwen` where
                `wangyixinwen`.id=`72ti7_wangyixinwen`.id
            ))
            limit {0}
        '''.format(random.randint(10,15))

        cursor.execute(sql)
        connect.commit()

        connect.close()
