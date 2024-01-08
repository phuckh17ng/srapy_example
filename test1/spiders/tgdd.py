# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class TggSpider(CrawlSpider ):
    name = "tgdd" # tên của spider
    allowed_domains = ["thegioididong.com"] # dont't config https://www...
    # ta điền link cần cào
    start_urls = [
        'https://www.thegioididong.com/',
    ]

    rules = (
        # Rule(LinkExtractor(allow="catalogue")),
        # Rule(LinkExtractor(allow="truyen/name")),
        Rule(LinkExtractor(allow="may-tinh-bang"), callback="parse_item"),
    )
    # rules = (
    #     Rule(LinkExtractor(allow="truyen"), callback="parse_item"),
    #     Rule(LinkExtractor(allow="truyen", deny="name"), callback="parse_item")
    # )

    def parse_item(self, response):       
        item = {}
        # yield {
        #     "title": response.css("#__next > div > div > div.info > div > div.d-block.d-sm-flex.pt-2 > div.right.flex-grow-1.pl-sm-5.pl-0.px-3 > div:nth-child(1) > div.d-flex.flex-column.mt-3.mt-sm-0 > h3::text").get(),
        #     # "price": response.css(".price_color::text").get(),
        #     "description": response.css("#__next > div > div > div.info > div > div.d-block.d-sm-flex.pt-2 > div.right.flex-grow-1.pl-sm-5.pl-0.px-3 > div:nth-child(1) > div.text-normal.overflow-none::text").get(),
        # }
        item["title"] = response.css("#categoryPage > div.container-productbox > ul > li:nth-child(1) > a.main-contain > h3::text").get()
        # item["description"] = response.css("#__next > div > div > div.info > div > div.d-block.d-sm-flex.pt-2 > div.right.flex-grow-1.pl-sm-5.pl-0.px-3 > div:nth-child(1) > div.text-normal.overflow-none::text").get()

        yield item
