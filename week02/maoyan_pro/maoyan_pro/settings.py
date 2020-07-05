# Scrapy settings for maoyan_pro project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'maoyan_pro'

SPIDER_MODULES = ['maoyan_pro.spiders']
NEWSPIDER_MODULE = 'maoyan_pro.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
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
    'Cookie': '''uuid_n_v=v1; uuid=9723B330B85D11EA9B3075693A212BAF01F225023F47431C97B6440322F271D6; _csrf=5ae25f10be0efec67167e4b4eef026bdf596e29569609aa3069e8e492c308b00; mojo-uuid=545a2986730bccc76547d372a7c4ee19; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593252281; _lxsdk_cuid=172f53c7ac6c8-090694edfaaf9f-4353761-1fa400-172f53c7ac6c8; _lxsdk=9723B330B85D11EA9B3075693A212BAF01F225023F47431C97B6440322F271D6; mojo-session-id={"id":"51f1ded86820ce4c85b41672a8323b35","time":1593970534344}; mojo-trace-id=6; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593972836; __mta=108418493.1593252282066.1593971920589.1593972837557.10; _lxsdk_s=173200f3240-857-c2f-f09%7C%7C10'''
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'maoyan_pro.middlewares.MaoyanProSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'maoyan_pro.middlewares.MaoyanProDownloaderMiddleware': 543,
#}
DOWNLOADER_MIDDLEWARES = {
    'maoyan_pro.middlewares.MaoyanProDownloaderMiddleware': 543,
    'maoyan_pro.middlewares.RandomHttpProxyMiddleware': 400,
}

HTTP_PROXY_LIST = [
    '1.255.48.197;8080',
    '101.37.118.54:8888',
    '101.4.136.34:81'
]

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'maoyan_pro.pipelines.MaoyanProPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
