# Projeto web crawler
# Processo seletivo para a empresa Semantix
# ------------------------------------------
# Autor: Alberto Barrios
# Data: 11/04/2020
# ------------------------------------------

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from semantix.spiders.ibovespa import IbovespaSpider
from semantix.spiders.nasdaq import NasdaqSpider
from semantix.spiders.usdbrl import UsdBrlSpider
import threading


def temporizador():
    process = CrawlerProcess(get_project_settings())
    process.crawl(NasdaqSpider)
    process.crawl(IbovespaSpider)
    process.crawl(UsdBrlSpider)
    process.start()

    t = threading.Timer(25, temporizador)
    t.start()
    temporizador()

temporizador()