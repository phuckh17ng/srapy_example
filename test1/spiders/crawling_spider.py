from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CrawlingSpider(CrawlSpider):
    name = "mycrawler"
    allowed_domains = ["toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    # allowed_domains = ["allinvn.net"]
    # start_urls = ["https://allinvn.net/truyen/name"]


    # PROXY_SERVER = "172.68.1.1"

    rules = (
        Rule(LinkExtractor(allow="catalogue/category")),
        Rule(LinkExtractor(allow="catalogue", deny="category"), callback="parse_item")
    )
    # rules = (
    #     Rule(LinkExtractor(allow="truyen"), callback="parse_item"),
    #     Rule(LinkExtractor(allow="truyen", deny="name"), callback="parse_item")
    # )

    def parse_item(self, response):
        yield {
            "title": response.css(".product_main h1::text").get(),
            "price": response.css(".price_color::text").get(),
            # "description": response.css(".sub-header h2:text").get(),
        }

        
    # def parse_item(self, response):
    #     yield {
    #         "title": response.css(".bluetext::text").get(),
    #         "des": response.css(".text-normal div::text").get(),
    #         # "availability": response.css(".availability::text")[2].get().replace("\n", "").replece(" ", ""),
    #     }