# -*- coding: utf-8 -*-

# Scrapy settings for tianmao project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tianmao'

SPIDER_MODULES = ['tianmao.spiders']
NEWSPIDER_MODULE = 'tianmao.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tianmao (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Cookie':'e1=%7B%22pid%22%3A%22qd_P_xiangqing%22%2C%22eid%22%3A%22qd_G15%22%2C%22l1%22%3A3%7D; e2=%7B%22pid%22%3A%22qd_P_xiangqing%22%2C%22eid%22%3A%22qd_G55%22%2C%22l1%22%3A14%7D; _csrfToken=Dcsh7fOrSTegXSs0dzQgMRjLtXFSYkbU7vphsin6; newstatisticUUID=1521679291_992550182; qdrs=0%7C3%7C0%7C0%7C1; qdgd=1; e1=%7B%22pid%22%3A%22qd_P_limitfree%22%2C%22eid%22%3A%22qd_E05%22%2C%22l1%22%3A5%7D; e2=%7B%22pid%22%3A%22qd_P_fin%22%2C%22eid%22%3A%22qd_A18%22%2C%22l1%22%3A3%7D; rcr=1009607977%2C1006629321%2C1011058239%2C1011240458%2C1011260655; bc=1011260655%2C1011240458%2C1011058239%2C1006629321%2C1009607977; lrbc=1009607977%7C372704205%7C0%2C1006629321%7C372544594%7C1%2C1011260655%7C397802976%7C0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.23 Safari/537.36',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'tianmao.middlewares.TianmaoSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   #'tianmao.middlewares.TianmaoDownloaderMiddleware': 543,
        'tianmao.tiammaomiddlewares.Tianmaomiddlewares': 1,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'tianmao.pipelines.TianmaoPipeline': 300,
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
#日志文件
LOG_FILE = 'sys.log'

#日志等级
LOG_LEVEL = 'ERROR'

#是否启用日志
LOG_ENABLED = True #启用日志

#日志编码
# LOG_ENCODING='utf-8'

#如果是True,进程当中 所有标准输出（包括错误）将会被
#重定向中到log中。例如，代码当中的print()
LOG_STDOUT = False#(默认值为False)