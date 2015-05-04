'''
Created on Apr 23, 2015

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
    name = "rastko"
    allowed_domains = ["rastko.rs"]
    start_urls = [
        "http://www.rastko.rs/",
              
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
        filename = "files_rastko/"+response.url.split("/")[-1]+"_crawled.html"
        with open(filename, 'wb') as f:
            f.write(response.body)