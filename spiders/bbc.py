# -*- coding: utf-8 -*-
import scrapy


class BbcSpider(scrapy.Spider):
    name = "bbc"
    allowed_domains = ["bbc.com"]
    start_urls = (
        'http://www.bbc.com/',
    )

    def parse(self, response):
        pass
