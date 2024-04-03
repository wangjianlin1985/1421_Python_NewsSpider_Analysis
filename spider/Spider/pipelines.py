# 管道文件

import pymysql
#import pymssql
from itemadapter import ItemAdapter

class SpiderPipeline(object):

    # 打开数据库
    def open_spider(self, spider):
        type = spider.settings.get('TYPE', 'mysql')
        host = spider.settings.get('HOST', 'localhost')
        port = int(spider.settings.get('PORT', 3306))
        user = spider.settings.get('USER', 'root')
        password = spider.settings.get('PASSWORD', '123456')

        try:
            database = spider.databaseName
        except:
            database = spider.settings.get('DATABASE', '')

        if type == 'mysql':
            self.connect = pymysql.connect(host=host, port=port, db=database, user=user, passwd=password, charset='utf8')
        else:
            self.connect = pymysql.connect(host=host, port=port, db=database, user=user, passwd=password, charset='utf8')
            #self.connect = pymssql.connect(host=host, user=user, password=password, database=database)
            
        self.cursor = self.connect.cursor()

    # 关闭数据库
    def close_spider(self, spider):
        self.connect.close()

    # 对数据进行处理
    def process_item(self, item, spider):
        self.insert_db(item, spider.name)
        return item

    # 插入数据
    def insert_db(self, item, spiderName):
        values = tuple(item.values())
        # print(values)

        qmarks = ', '.join(['%s'] * len(item))
        cols = ', '.join(item.keys())

        sql = "INSERT INTO %s (%s) VALUES (%s)" % (spiderName.replace('Spider', ''), cols, qmarks)

        self.cursor.execute(sql, values)
        self.connect.commit()
