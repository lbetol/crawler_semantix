# Projeto web crawler
# Processo seletivo para a empresa Semantix
# ------------------------------------------
# Autor: Alberto Barrios
# Data: 11/04/2020
# ------------------------------------------
# -*- coding: utf-8 -*-

import scrapy
from semantix.items import SemantixItemIbovespa




class IbovespaSpider(scrapy.Spider):
    name = 'ibovespa'
    start_urls = ['https://www.investing.com/equities/StocksFilter?index_id=17920']

    def parse(self, response):
        item = SemantixItemIbovespa()
        item['name'] = response.xpath('//table//td//a[re:test(@title, "")]/text()').getall()
        item['last_rs'] = response.xpath('//td[contains(@class, "last")]/text()').getall()
        item['high_rs'] = response.xpath('//td[contains(@class, "high")]/text()').getall()
        item['low_rs'] = response.xpath('//td[contains(@class, "low")]/text()').getall()
        item['chg'] = response.xpath('//td[contains(@class, "pc")]/text()').getall()
        item['chper'] = response.xpath('//td[contains(@class, "pcp")]/text()').getall()
        item['vol'] = response.xpath('//td[contains(@class, "turnover")]/text()').getall()
        item['time'] = response.xpath('//td[contains(@class, "time")]/text()').getall()
        return item




