from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from semantix.spiders.ibovespa import IbovespaSpider
from semantix.spiders.nasdaq import NasdaqSpider
from semantix.spiders.usdbrl import UsdBrlSpider
import threading

process = CrawlerProcess(get_project_settings())
process.crawl(NasdaqSpider)
process.crawl(IbovespaSpider)
process.crawl(UsdBrlSpider)
process.start()

def iniciar():
    process.start()

threading.Timer(120, iniciar).start()





