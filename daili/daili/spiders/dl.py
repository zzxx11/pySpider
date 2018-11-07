# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request


class DlSpider(scrapy.Spider):
    name = 'dl'
    # allowed_domains = ['daili.com']
    start_urls = ['http://httpbin.org/get']

    def parse(self, response):
        print(response.text)
