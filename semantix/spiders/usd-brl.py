#Projeto web crawler
#Processo seletivo para a empresa Semantix
#------------------------------------------
#Autor: Alberto Barrios
#Data: 11/04/2020
#------------------------------------------

# -*- coding: utf-8 -*-

import scrapy


class IbovespaSpider(scrapy.Spider):
    name = 'usd-brl'
    start_urls = ['https://m.investing.com/currencies/usd-brl']

    def parse(self, response):
        import ipdb; ipdb.set_trace()
        pass
