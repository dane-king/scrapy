# -*- coding: utf-8 -*-
import traceback
import scrapy
from scrapy.http import Request
from collegestats.items import CollegestatsItem


class StatsSpider(scrapy.Spider):
    name = "stats"
    allowed_domains = ["http://www.espn.com/college-football/statistics"]
    pageSize = int(40)

    url="http://www.espn.com/college-football/statistics/player/_/stat/%s/year/%s/qualified/false/count/%s"
    
    def __init__(self, startYear=2004, endYear=2016, maxPages=12, *args, **kwargs):
        super(StatsSpider, self).__init__(*args, **kwargs)
        self.startYear = int(startYear)
        self.endYear = int(endYear)
        self.maxPages = int(maxPages)
        
    def start_requests(self):
        print 'getting results for %s, from %s to %s for %s pages' % (self.type, self.startYear, self.endYear, self.maxPages)
        for year in range(self.startYear, self.endYear):
            for page in range(self.maxPages):
                pageNumber = page * self.pageSize + 1
                yield Request(self.url % (self.type, year, pageNumber), self.parse)

    def parse(self, response):
        year = response.xpath('//h1[@class="h2"]/text()')[0].extract().split('-')[2]
        #print 'current year', year

        for row in response.xpath("//table//tr[contains(@class,'player')]"):
            item = CollegestatsItem()
            holder=[]
            holder.append(year.strip())
            try:
                name_pos = row.xpath('td[2]//text()').extract()
               
                holder.append(name_pos[0].strip())
                if len(name_pos) > 1:
                     holder.append(name_pos[1].replace(",","").strip())
                
                data = row.xpath('td[position()>2]//text()').extract()
                holder = holder+data
                
                item['data'] = holder
                
                yield item
            except Exception:
                print name_pos
                traceback.print_exc()

            