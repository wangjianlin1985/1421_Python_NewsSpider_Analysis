# 数据容器文件

import scrapy

class SpiderItem(scrapy.Item):
    pass

class WangyixinwenItem(scrapy.Item):
    # 来源
    laiyuan = scrapy.Field()
    # 标题
    biaoti = scrapy.Field()
    # 封面
    fengmian = scrapy.Field()
    # 来自
    laizi = scrapy.Field()
    # 跟帖
    gentie = scrapy.Field()
    # 关键字
    guanjianzi = scrapy.Field()
    # 发布时间
    fabushijian = scrapy.Field()
    # 内容
    detail = scrapy.Field()

