from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from selenium import webdriver
import scrapy

class CrawlingSpider(scrapy.Spider):
    # name for spider
    name = "testcsr"

    # allowed_domains = ["s3-website-us-east-1.amazonaws.com"]
    start_urls = ["http://khang-imdb.s3-website-us-east-1.amazonaws.com/"]
    
    def __init__(self):
        self.driver = webdriver.Firefox()

    rules = (
        Rule(LinkExtractor(), callback="parse_item"),
    )

    def parse(self, response):
       pass  

    # def parse_item(self, response):       
    #     item = {}


        # yield item
