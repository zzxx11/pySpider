# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from fake_useragent import UserAgent

class UserAgentMiddleware(object):
    def process_request(self, request, spider):

        request.headers.setdefault(b'User-Agent', UserAgent().random)

class Proxy_Middleware(object):
    def process_request(self, request, spider):
        request.meta['proxy'] = 'http://111.202.37.195:47818'
        # request.meta['proxy'] = 'http://user:passwd@111.202.37.195:47818'

from selenium import webdriver
from scrapy.http import HtmlResponse

class SeleniumMiddleware(object):
    def __init__(self):
        self.chrom = webdriver.Chrome()

    def __del__(self):
        self.chrom.close()

    def process_request(self,request,spider):
        url = request.url
        self.chrom.get(url)
        html = self.chrom.page_source
        return HtmlResponse(url=url,body=html,request=request,encoding='utf-8')

