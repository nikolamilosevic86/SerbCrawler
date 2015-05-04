'''
Created on Apr 22, 2015

@author: Nikola

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy import log
from scrapy.tests.mockserver import Follow

class TarzSpider(CrawlSpider):
    name = "tarzanija"
    allowed_domains = ["tarzanija.com"]
    start_urls = [
        "http://tarzanija.com",
        "http://www.tarzanija.com/objasnjavanje/",
        "http://www.tarzanija.com/objasnjavanje/page/2/",
        "http://www.tarzanija.com/objasnjavanje/page/3/",
        "http://www.tarzanija.com/objasnjavanje/page/4/",
        "http://www.tarzanija.com/objasnjavanje/page/5/",
        "http://www.tarzanija.com/objasnjavanje/page/6/",
        "http://www.tarzanija.com/objasnjavanje/page/7/",
        "http://www.tarzanija.com/objasnjavanje/page/8/",
        "http://www.tarzanija.com/objasnjavanje/page/9/",
        "http://www.tarzanija.com/objasnjavanje/page/10/",
        "http://www.tarzanija.com/objasnjavanje/page/11/",
        
    ]
    
    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        #Rule(LinkExtractor(allow=('a', ))),

        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(LinkExtractor(allow=('', )), callback='parse_item',follow=True),
    )

    def parse_item(self, response):
        log.msg("URL:"+response.url, level=log.DEBUG)
        filename = "files/"+response.url.split("/")[-2]+"_crawled.html"
        with open(filename, 'wb') as f:
            f.write(response.body)