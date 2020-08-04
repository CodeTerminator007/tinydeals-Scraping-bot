# -*- coding: utf-8 -*-
import scrapy


class SpecialSpider(scrapy.Spider):
    name = 'special'
    allowed_domains = ['www.tinydeal.com']
    start_urls = ['https://www.tinydeal.com/specials.html']

    def parse(self, response):
        for row in response.xpath('//ul[@class="productlisting-ul"]/div[@class="p_box_wrapper"]'):
            yield {
                'Product' : row.xpath('.//li/a[@class="p_box_title"]/text()').get(),
                'Link'  :  response.urljoin(row.xpath('.//li/a[@class="p_box_title"]/@href').get()),
                'Special Price' : row.xpath('.//li/div[@class="p_box_price"]/span[1]/text()').get(),
                'Price' : row.xpath('.//li/div[@class="p_box_price"]/span[2]/text()').get()
               
                
                }
            
        next_pagee = response.xpath('//a[@class="nextPage"]/@href').get()
        
        if next_pagee:
            yield scrapy.Request(url=next_pagee, callback=self.parse)
            
            
            