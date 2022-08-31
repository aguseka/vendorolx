# -*- coding: utf-8 -*-

# Scrapy settings for vendorolx project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "vendorolx"

SPIDER_MODULES = ["vendorolx.spiders"]
NEWSPIDER_MODULE = "vendorolx.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'vendorolx (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False
COOKIES_ENABLED = False
COOKIES_DEBUG = False

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'vendorolx.middlewares.VendorolxSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'vendorolx.middlewares.VendorolxDownloaderMiddleware': 543,
# }
PROXY_POOL_ENABLED = True
DOWNLOADER_MIDDLEWARES = {
    "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
    # "scrapy_proxy_pool.middlewares.ProxyPoolMiddleware": 610,
    # "scrapy_proxy_pool.middlewares.BanDetectionMiddleware": 620,
    "scrapy_user_agents.middlewares.RandomUserAgentMiddleware": 800,
}
# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
EXTENSIONS = {
    "scrapy.extensions.telnet.TelnetConsole": 0,
}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    "vendorolx.pipelines.PhonePipeline": 810,
    "vendorolx.pipelines.FilterPipeline": 850,
    "vendorolx.pipelines.DuplicatesPipeline": 860,
    "vendorolx.pipelines.CategoryPipeline": 870,
    "vendorolx.pipelines.CreateURLPipeline": 880,
    "vendorolx.pipelines.WhatsappPipeline": 890,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
FEED_FORMAT = "csv"
FEED_URI = "/Users/ekaaditya/Desktop/ScrapeResult/%(name)s/%(time)s.csv"
FEED_EXPORT_FIELDS = [
    "category_id",
    "user_name",
    "user_tlp",
    "prop_addrs",
    "lst_val",
    "lt",
    "lb",
    "proc_status",
    "human_url",
    "link_whatsapp",
    "user_url",
]
