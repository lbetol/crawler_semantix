#Projeto web crawler
#Processo seletivo para a empresa Semantix
#------------------------------------------
#Autor: Alberto Barrios
#Data: 11/04/2020
#------------------------------------------

# -*- coding: utf-8 -*-

import scrapy


class IbovespaSpider(scrapy.Spider):
    name = 'ibovespa'
    start_urls = ['https://www.investing.com/equities/StocksFilter?index_id=17920']

    def parse(self, response):
        name    = response.xpath('//table//td//a[re:test(@title, "")]/text()').getall()
        last_rs = response.xpath('//td[contains(@class, "last")]/text()').getall()
        high_rs = response.xpath('//td[contains(@class, "high")]/text()').getall()
        low_rs  = response.xpath('//td[contains(@class, "low")]/text()').getall()
        chg     = response.xpath('//td[contains(@class, "pc")]/text()').getall()
        chgper  = response.xpath('//td[contains(@class, "pcp")]/text()').getall()
        vol     = response.xpath('//td[contains(@class, "turnover")]/text()').getall()
        time    = response.xpath('//td[contains(@class, "time")]/text()').getall()
        yield {
            'name': name,
            'last_rs': last_rs,
            'high_rs': high_rs,
            'low_rs': low_rs,
            'chg': chg,
            'ch%': chgper,
            'vol': vol,
            'time': time
        }



