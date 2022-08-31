# -*- coding: utf-8 -*-
import scrapy


class BrokerSpider(scrapy.Spider):
    name = 'broker'
    allowed_domains = ['olx.co.id']
    start_urls = ['http://olx.co.id/']

    def parse(self, response):
        pass
