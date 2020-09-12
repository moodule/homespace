# -*- coding: utf-8 -*-

# Scrapy settings for adspying project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import os
import random

BOT_NAME = 'adspying'

SPIDER_MODULES = ['adspying.spiders']
NEWSPIDER_MODULE = 'adspying.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
__useragents_file_path = os.path.join(
		os.path.dirname(os.path.realpath(__file__)),
		"_data/user-agents_mid.txt")
with open(__useragents_file_path, 'r') as __useragents_file:
	USER_AGENT_LIST = [line for line in __useragents_file.readlines()]
USER_AGENT = random.choice(USER_AGENT_LIST)

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 16

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
   'adspying.middlewares.RandomUserAgentMiddleware': 100,
   'adspying.middlewares.AdspyingSpiderMiddleware': 543,
}

# The maximum depth that will be allowed to crawl for any site.
# If zero, no limit will be imposed.
DEPTH_LIMIT = 2

# As depth increases, positive values of DEPTH_PRIORITY decrease
# request priority (BFO), while negative values increase request priority (DFO).
DEPTH_PRIORITY = 1

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'adspying.middlewares.AdspyingDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Parent location of all the exports
EXPORT_FOLDER_PATH = os.path.realpath('./data/')
MONGO_URI = 'mongodb://localhost:27017/'
MONGO_DATABASE = 'adspying'

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'adspying.pipelines.CsvPipeline': 300,
   'adspying.pipelines.HtmlTablePipeline': 301,
   'adspying.pipelines.JsonPipeline': 302,
   'adspying.pipelines.MongoDbPipeline': 303
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
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 3600
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
