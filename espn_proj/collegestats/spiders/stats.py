# -*- coding: utf-8 -*-
import scrapy
import traceback
from scrapy.http import Request
from collegestats.items import CollegestatsItem


class StatsSpider(scrapy.Spider):
    name = "stats"
    allowed_domains = ["http://www.espn.com/college-football/statistics"]
    pageSize = int(40)
    years = ['2004','2005']
    maxPage = int(12)
    url = str('http://www.espn.com/college-football/statistics/player/_/stat/passing/sort/passingYards/year/{0}/qualified/false/count/{1}')
    
    def start_requests(self):
        for year in self.years:
            self.currentYear = year
            for page in range(self.maxPage):
                pageNumber = page * self.pageSize + 1
                print year, pageNumber
                yield Request(self.url.format(year, pageNumber), self.parse)

    def parse(self, response):
        year=response.xpath('//h1[@class="h2"]/text()')[0].extract().split('-')[2]
        print 'current year', year
        previous_rank=0
        for row in response.xpath("//table//tr"):
            item = CollegestatsItem()
            rank=row.xpath("td[1]/text()").extract()
            try:
                if rank[0]=='RK':
                    continue
                previous_rank=rank[0]    
                item['year'] = year
                if rank=='':
                    rank=previous_rank
                item['rank'] = rank
                name_pos = row.xpath('td[2]//text()').extract()
                item['name'] = name_pos[0]
                item['pos'] = name_pos[1]
                yield item
            except Exception, e:
                traceback.print_exec()

            