# Projeto web crawler
# Processo seletivo para a empresa Semantix
# ------------------------------------------
# Autor: Alberto Barrios
# Data: 11/04/2020
# ------------------------------------------
# -*- coding: utf-8 -*-

import scrapy
from semantix.items import SemantixItemNasdaq

class NasdaqSpider(scrapy.Spider):
    name = 'nasdaq'
    start_urls = ['https://www.investing.com/equities/StocksFilter?index_id=20']

    def parse(self, response):
        item = SemantixItemNasdaq()

        item['name'] = response.xpath('//table//td//a[re:test(@title, "")]/text()').getall()
        item['last_usd'] = response.xpath('//td[contains(@class, "last")]/text()').getall()
        item['high_usd'] = response.xpath('//td[contains(@class, "high")]/text()').getall()
        item['low_usd'] = response.xpath('//td[contains(@class, "low")]/text()').getall()
        item['chg'] = response.xpath('//td[contains(@class, "pc")]/text()').getall()
        item['chper'] = response.xpath('//td[contains(@class, "pcp")]/text()').getall()
        item['vol'] = response.xpath('//td[contains(@class, "turnover")]/text()').getall()
        item['time'] = response.xpath('//td[contains(@class, "time")]/text()').getall()
        return item

#        yield {
#            'name': name,
#            'last_usd': last_usd,
#            'high_usd': high_usd,
#            'low_usd': low_usd,
#            'chg': chg,
#            'ch%': chgper,
#            'vol': vol,
#            'time': time
#        }



