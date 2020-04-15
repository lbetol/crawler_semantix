#Projeto web crawler
#Processo seletivo para a empresa Semantix
#------------------------------------------
#Autor: Alberto Barrios
#Data: 11/04/2020
#------------------------------------------

# -*- coding: utf-8 -*-

import scrapy
from semantix.items import SemantixItemCotacao

# classe UsdBrlSpider realiza todos os crawler solicitados
class UsdBrlSpider(scrapy.Spider):

    # Identificação do crawler e a URL onde o crawler atuará
    name = 'usdbrl'
    start_urls = ['https://m.investing.com/currencies/usd-brl']


    # Função parse realiza o crawler, extraindo o que foi solicitado e o
    # guarda em um objeto que se chama item
    def parse(self, response):
        item = SemantixItemCotacao()

        # Os comando a baixo extrai o conteúdo solicitado da página
        item['currency'] = response.xpath('//h1[contains(@class, "instrumentH1inlineblock")]/text()').getall()
        item['value'] = response.xpath('//span[contains(@class, "last")]/text()').getall()
        item['change'] = response.xpath('//i[contains(@class, "pc")]/text()').getall()
        item['perc'] = response.xpath('//div//i[contains(@class, "pcp")]/text()').getall()
        item['timestamp'] = response.xpath('//div//i[contains(@class, "time")]/text()').getall()
        return item