# -*- coding: utf-8 -*-
import scrapy
import urlparse
from espn.items import EspnItem


class EspnSpider(scrapy.Spider):
    name = "ff"
    allowed_domains = ["scores.espn.go.com"]
    start_urls = [
      'http://scores.espn.go.com/nfl/scoreboard?seasonYear=2014&seasonType=1&weekNumber=5'
    ]

    def parse(self, response):
      game_url='http://scores.espn.go.com/nfl/playbyplay?gameId=%s'
      games=response.css("div[id$='-gameContainer'] span.sort").xpath('text()').extract()
      for game_id in games:
        yield scrapy.Request(game_url % game_id, callback=self.parse_game)
        

    def parse_game(self,response):
      for qtr in range(1,4):
        yield scrapy.Request(response.url + "&period=%d" % qtr ,callback=self.parse_quarters)

    
    def parse_quarters(self,response):
      item = EspnItem()
      parsed = urlparse.urlparse(response.url)
      qtr=urlparse.parse_qs(parsed.query)['period']
      gameId=urlparse.parse_qs(parsed.query)['gameId']
      for sel in response.css('div.mod-container table tr'):
        item["qtr"]=qtr
        item["gameId"]=gameId
        item["downDist"] = sel.xpath('td[1]/text()').extract()
        item["play"]=sel.xpath('td[2]/text()').extract()
        item["score1"]=sel.xpath('td[3]/text()').extract()
        item["score2"]=sel.xpath('td[4]/text()').extract()
        yield item
      


        
