# Projeto web crawler
# Processo seletivo para a empresa Semantix
# ------------------------------------------
# Autor: Alberto Barrios
# Data: 11/04/2020
# ------------------------------------------

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class SemantixItemNasdaq(scrapy.Item):
        # Todos os item que serão capturados do spider
        # Itens da Nasdaq
        name = scrapy.Field()
        last_usd = scrapy.Field()
        high_usd = scrapy.Field()
        low_usd = scrapy.Field()
        chg = scrapy.Field()
        chper = scrapy.Field()
        vol = scrapy.Field()
        time = scrapy.Field()

class SemantixItemIbovespa(scrapy.Item):
        # Itens do Ibovespa
        name = scrapy.Field()
        last_rs = scrapy.Field()
        high_rs = scrapy.Field()
        low_rs = scrapy.Field()
        chg = scrapy.Field()
        chper = scrapy.Field()
        vol = scrapy.Field()
        time = scrapy.Field()

class SemantixItemCotacao(scrapy.Item):
        # Itens da da cotação
        currency = scrapy.Field()
        value = scrapy.Field()
        change = scrapy.Field()
        perc = scrapy.Field()
        timestamp = scrapy.Field()

