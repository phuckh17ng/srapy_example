# -*- coding: utf-8 -*-
import scrapy

class TggSpider(scrapy.Spider):
    name = "tgdd" # tên của spider
    allowed_domains = ["thegioididong.com"] # dont't config https://www...
    # ta điền link cần cào
    start_urls = [
        'https://www.thegioididong.com/may-tinh-bang',
    ]

 # lớp để bóc tách dữ liệu
    def parse(self, response):
        # Tìm tất cả các item dựa vào selector
        for item_url in response.css(".listproduct").extract():
            yield scrapy.Request(response.urljoin(item_url), callback=self.parse_tablet) # if have product, call function parse_book_page
        
       # nếu có trang kế thì bóc tiếp
        next_page = response.css("li.next > a ::attr(href)").extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def parse_tablet(self, response):
        item = {}
        # find info of product
        product = response.css(".type0")
        item["title"] = product.css(".rowtop > h1::text").extract_first()
        item['price'] = response.css('.area_price strong ::text').extract_first()
       
        yield item
