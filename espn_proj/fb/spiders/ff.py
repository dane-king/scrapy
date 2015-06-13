# -*- coding: utf-8 -*-
import scrapy
import urlparse
from fb.items import FBItem


class FBSpider(scrapy.Spider):
    name = "fb"
    allowed_domains = ["www.footballdb.com"]
    start_urls = [
        'http://www.footballdb.com/stats/stats.html?mode=P&yr=2014&lg=NFL'
    ]

    def parse(self, response):
        for row in response.xpath("//table[@class='statistics scrollable']//tr"):
            item = FBItem()
            item['player_name'] = row.select("td[1]//a[1]/text()").extract()
            item['team_name'] = row.select("td[2]//a[1]/text()").extract()
            yield item


        
