# Projeto web crawler
# Processo seletivo para a empresa Semantix
# ------------------------------------------
# Autor: Alberto Barrios
# Data: 11/04/2020
# ------------------------------------------
# -*- coding: utf-8 -*-

import scrapy
from semantix.items import SemantixItemNasdaq

# classe NasdaqSpider realiza todos os crawler solicitados
class NasdaqSpider(scrapy.Spider):

    # Identificação do crawler e a URL onde o crawler atuará
    name = 'nasdaq'
    start_urls = ['https://www.investing.com/equities/StocksFilter?index_id=20']

    # Função parse realiza o crawler, extraindo o que foi solicitado e o
    # guarda em um objeto que se chama item
    def parse(self, response):
        item = SemantixItemNasdaq()

        tds = response.xpath('//td')
        for td in tds:
            item['name'] = td.xpath('//table//td//a[re:test(@title, "")]/text()').getall()
            item['last_usd'] = td.xpath('//td[contains(@class, "last")]/text()').getall()
            item['high_usd'] = td.xpath('//td[contains(@class, "high")]/text()').getall()
            item['low_usd'] = td.xpath('//td[contains(@class, "low")]/text()').getall()
            item['chg'] = td.xpath('//td[contains(@class, "pc")]/text()').getall()
            item['chper'] = td.xpath('//td[contains(@class, "pcp")]/text()').getall()
            item['vol'] = td.xpath('//td[contains(@class, "turnover")]/text()').getall()
            item['timenq'] = td.xpath('//td[contains(@class, "time")]/text()').getall()
            return item



