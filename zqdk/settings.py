# -*- coding: utf-8 -*-

# Scrapy settings for zqdk project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zqdk'

SPIDER_MODULES = ['zqdk.spiders']
NEWSPIDER_MODULE = 'zqdk.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-AL00 Build/HUAWEIEVA-AL00)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#     'Content-Type': 'application/json; charset=UTF-8',
#     'Accept-Charset': 'UTF-8, ISO-8859-1',
#     'Cookie':'',
#     'deviceUuid': '21610e74de2ed5d1',
#     'jcobToken':'',
#     'Accept': 'application/json,text/html',
#     'sessionLoginCookie': 'fd08dee3-a157-2020-fb69-d687fcd3ddd8',
#     'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-AL00 Build/HUAWEIEVA-AL00)',
#     'Host': 'sport.ttyingqiu.com',
#     'Connection': 'Keep-Alive',
#     'Accept-Encoding': 'gzip',
#     'Content-Length': '118'
#     }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zqdk.middlewares.ZqdkSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'zqdk.middlewares.ZqdkDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'zqdk.pipelines.ZqdkPipeline': 300,
   'zqdk.pipelines.MysqlPipeline':301
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

MYSQL_HOST = 'localhost'
MYSQL_DATABASE = 'newstwo'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'Leng9s9bxs'