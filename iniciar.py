from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
#from PyQt4.QtCore import QTimer

from semantix.spiders.ibovespa import IbovespaSpider
from semantix.spiders.nasdaq import NasdaqSpider
from semantix.spiders.usdbrl import UsdBrlSpider


process = CrawlerProcess(get_project_settings())
process.crawl(NasdaqSpider)
process.crawl(IbovespaSpider)
process.crawl(UsdBrlSpider)
process.start()


#def crawler():
#    iniciar = CrawlerProcess(get_project_settings())
#    iniciar.crawl(IbovespaSpider)
#    iniciar.start()

# iniciar = CrawlerProcess(get_project_settings())
 #   iniciar.crawl(NasdaqSpider)
  #  iniciar.start()

   # iniciar = CrawlerProcess(get_project_settings())
    # iniciar.crawl(UsdBrlSpider)
   # iniciar.start()

    #timer = QTimer()
    #timer.setSingleShot(True)
    #timer.timeout.connect(crawler)
    #timer.start(120000)