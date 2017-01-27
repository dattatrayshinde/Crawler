# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from Crawler.items import CrawlerItem
from scrapy.selector import HtmlXPathSelector

class BbcSpider(CrawlSpider):
    name = "bbc"
    #Crawler will no go beyond this domains
    allowed_domains = ["bbc.com"]
    #Where to start crawling
    start_urls = (
        'http://www.bbc.com/',
    )
    rules = (
        Rule(LinkExtractor(allow=r'/news/[A-Za-z0-9]'), callback='parse_item', follow=True),
        #Rule(LinkExtractor(allow=r'/news/[a-z]'), callback='parse_item', follow=True),
    )
    
    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        item = CrawlerItem()
        #item['text'] = response.xpath('//*[@id="page"]/div[2]/div[2]/div/div[1]/div[1]/div[3]/p[1]//text()').extract()[0]
        item['text'] = hxs.select('//p[@class="story-body__introduction"]/text()').extract()
        item['author'] = "BBC News Media"
        #item['headline'] = response.xpath('//*[@id="page"]/div[2]/div[2]/div/div[1]/div[1]/h1//text()').extract()[0]
        item['headline'] =  hxs.select('//h1[@class="story-body__h1"]/text()').extract()
        item['url'] = response.url
        yield item 
