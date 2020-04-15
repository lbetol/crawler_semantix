#Projeto web crawler
#Processo seletivo para a empresa Semantix
#------------------------------------------
#Autor: Alberto Barrios
#Data: 11/04/2020
#------------------------------------------

# -*- coding: utf-8 -*-

import scrapy
from semantix.items import SemantixItemCotacao

class UsdBrlSpider(scrapy.Spider):
    name = 'usdbrl'
    start_urls = ['https://m.investing.com/currencies/usd-brl']

    def parse(self, response):
        item = SemantixItemCotacao()
        item['currency'] = response.xpath('//h1[contains(@class, "instrumentH1inlineblock")]/text()').getall()
        item['value'] = response.xpath('//span[contains(@class, "last")]/text()').getall()
        item['change'] = response.xpath('//i[contains(@class, "pc")]/text()').getall()
        item['perc'] = response.xpath('//div//i[contains(@class, "pcp")]/text()').getall()
        item['timestamp'] = response.xpath('//div//i[contains(@class, "time")]/text()').getall()
        return item