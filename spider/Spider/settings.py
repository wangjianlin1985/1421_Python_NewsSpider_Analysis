# 配置文件

import os
import configparser
import random

BOT_NAME = 'Spider'

SPIDER_MODULES = ['Spider.spiders']
NEWSPIDER_MODULE = 'Spider.spiders'

# 禁用 robots.txt 规则
ROBOTSTXT_OBEY = False

# 为同一网站的请求配置延迟 (默认: 0)
DOWNLOAD_DELAY = 5

USER_AGENT_LIST = [
   'MSIE (MSIE 6.0; X11; Linux; i686) Opera 7.23',
   'Opera/9.20 (Macintosh; Intel Mac OS X; U; en)',
   'Opera/9.0 (Macintosh; PPC Mac OS X; U; en)',
   'iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)',
   'Mozilla/4.76 [en_jp] (X11; U; SunOS 5.8 sun4u)',
   'iTunes/4.2 (Macintosh; U; PPC Mac OS X 10.2)',
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:5.0) Gecko/20100101 Firefox/5.0',
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:9.0) Gecko/20100101 Firefox/9.0',
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:16.0) Gecko/20120813 Firefox/16.0',
   'Mozilla/4.77 [en] (X11; I; IRIX;64 6.5 IP30)',
   'Mozilla/4.8 [en] (X11; U; SunOS; 5.7 sun4u)'
]

# 重写默认请求头
DEFAULT_REQUEST_HEADERS = {
   # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
   'user-agent': random.choice(USER_AGENT_LIST)
}

# 配置 item_pipelines
ITEM_PIPELINES = {
   'Spider.pipelines.SpiderPipeline': 300,
}

LOG_ENABLED = True
COOKIES_ENABLED = False

config = configparser.ConfigParser()

config.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config/config.ini'), encoding='utf-8')

# db 配置
TYPE = config.get('db', 'type')
HOST = config.get('db', 'host')
PORT = config.get('db', 'port')
DATABASE = config.get('db', 'database')
USER = config.get('db', 'user')
PASSWORD = config.get('db', 'password')
