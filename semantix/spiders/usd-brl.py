#Projeto web crawler
#Processo seletivo para a empresa Semantix
#------------------------------------------
#Autor: Alberto Barrios
#Data: 11/04/2020
#------------------------------------------

# -*- coding: utf-8 -*-

import scrapy


class UsdBrlSpider(scrapy.Spider):
    name = 'usd-brl'
    start_urls = ['https://m.investing.com/currencies/usd-brl']

    def parse(self, response):
        currency = response.xpath('//td[contains(@class, "center")]/text()').getall()
        value = response.xpath('//td[contains(@class, "last")]/text()').getall()
        change = response.xpath('//span[contains(@class, "pc")]/text()').getall()
        perc = response.xpath('//td[contains(@class, "pch")]/text()').getall()
        timestamp = response.xpath('//td[contains(@class, "tim")]/text()').getall()

        yield {
            'currency': currency,
            'value': value,
            'change': change,
            'perc': perc,
            'timestamp': timestamp
        }