# -*- coding: utf-8 -*-
import scrapy


class NecsiCrawlSpider(scrapy.Spider):
    name = 'necsi_crawl'
    allowed_domains = ['http://www.necsi.edu/events/iccs2018/']
    start_urls = ['http://http://www.necsi.edu/events/iccs2018//']

    def parse(self, response):
        pass
