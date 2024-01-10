from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CrawlingSpider(CrawlSpider):
    # name for spider
    name = "mycrawler"

    # a list of domains that this spider is allowed to crawl
    # allowed_domains = ["toscrape.com"]

    # a list of domains that this spider will be allowed to crawl from, when no particular URLs are specified
    # start_urls = ["http://books.toscrape.com/"]

    # allowed_domains = ["allinvn.net"]
    start_urls = ["https://allinvn.net/"]


    # PROXY_SERVER = "172.68.1.1"

    rules = (
        # Rule(LinkExtractor(allow="catalogue")),
        # Rule(LinkExtractor(allow="truyen/name")),
        Rule(callback="parse_item"),
    )
    # rules = (
    #     Rule(LinkExtractor(allow="truyen")),
    #     Rule(LinkExtractor(allow="truyen/name", deny="name"), callback="parse_item")
    # )

    def parse_item(self, response):  
        print("khang123", self)     
        print("khang111", response)     

        item = {}
        # yield {
        #     "title": response.css("#__next > div > div > div.info > div > div.d-block.d-sm-flex.pt-2 > div.right.flex-grow-1.pl-sm-5.pl-0.px-3 > div:nth-child(1) > div.d-flex.flex-column.mt-3.mt-sm-0 > h3::text").get(),
        #     # "price": response.css(".price_color::text").get(),
        #     "description": response.css("#__next > div > div > div.info > div > div.d-block.d-sm-flex.pt-2 > div.right.flex-grow-1.pl-sm-5.pl-0.px-3 > div:nth-child(1) > div.text-normal.overflow-none::text").get(),
        # }
        item["title"] = response.css("#__next > div > div > div.info > div > div.d-block.d-sm-flex.pt-2 > div.right.flex-grow-1.pl-sm-5.pl-0.px-3 > div:nth-child(1) > div.d-flex.flex-column.mt-3.mt-sm-0 > h3::text").get()
        item["description"] = response.css("#__next > div > div > div.info > div > div.d-block.d-sm-flex.pt-2 > div.right.flex-grow-1.pl-sm-5.pl-0.px-3 > div:nth-child(1) > div.text-normal.overflow-none::text").get()
        image_url = response.css("#__next > div > div > div.info > div > div.d-block.d-sm-flex.pt-2 > div.left.d-flex.d-sm-block.justify-content-center.align-items-center > div.position-relative.mr-4.mr-sm-0 > div > span > img::attr(src)").get()
        
        image_url = response.urljoin(image_url)
        item['image_urls'] = [image_url]
        # print("khang123", image_url)

        yield item

        
    # def parse_item(self, response):
    #     yield {
    #         "title": response.css(".bluetext::text").get(),
    #         "des": response.css(".text-normal div::text").get(),
    #         # "availability": response.css(".availability::text")[2].get().replace("\n", "").replece(" ", ""),
    #     }