# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from Crawler.items import CrawlerItem

class BbcSpider(scrapy.Spider):
    name = "bbc"
    #Crawler will no go beyond this domains
    allowed_domains = ["bbc.com"]
    #Where to start crawling
    start_urls = (
        'http://www.bbc.com/news/world-us-canada-38777437',
    )
    
    
    def parse(self, response):
        #fetching the title of the news
        item = CrawlerItem()
        item['text'] = response.xpath('//*[@id="page"]/div[2]/div[2]/div/div[1]/div[1]/div[3]/p[1]//text()').extract()[0]
        item['author'] = "BBC News Media"
        item['headline'] = response.xpath('//*[@id="page"]/div[2]/div[2]/div/div[1]/div[1]/h1//text()').extract()[0]
        item['url'] = response.url
        yield item      
        