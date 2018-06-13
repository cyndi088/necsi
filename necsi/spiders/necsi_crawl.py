# -*- coding: utf-8 -*-
import scrapy


class NecsiCrawlSpider(scrapy.Spider):
    name = 'necsi_crawl'
    allowed_domains = ['www.necsi.edu/events/iccs2018']
    start_urls = ['http://www.necsi.edu/events/iccs2018/']

    def parse(self, response):
        resp = response.xpath('//body/div[@class="row"][5]/div[@class="column"]/div[@class="row"]//p//b/text()').extract()
        print('***************************')
        print(resp)
        print('***************************')

