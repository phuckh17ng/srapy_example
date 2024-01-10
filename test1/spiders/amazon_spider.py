from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import scrapy
class CrawlingSpider(CrawlSpider):
    # name for spider
    name = "amazon-crawler"

    # a list of domains that this spider is allowed to crawl
    # allowed_domains = ["toscrape.com"]

    # a list of domains that this spider will be allowed to crawl from, when no particular URLs are specified
    # start_urls = ["http://books.toscrape.com/"]

    # allowed_domains = ["s3-website-us-east-1.amazonaws.com"]
    # start_urls = ["https://amazon.com/"]
    start_urls = ["http://khang-imdb.s3-website-us-east-1.amazonaws.com/"]
    # PROXY_SERVER = "172.68.1.1"

    rules = (
        Rule(LinkExtractor(), callback="parse_item"),
    )
    # rules = (
    #     Rule(LinkExtractor(), callback="parse_item", follow=True),
    # )

    # def parse_item(self, response):
    #     filename = response.url.split("/")[-2] + '.html'
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
  
    def parse_item(self, response):       
        print("khang123", response)
        print("khang111", self)
        item = {}
        # for item_url in response.css(".level-title::text").extract():
        #     item["skill"] = item_url
        #     yield item
        # item["title"] = response.css("#root > main > div.w-full.bg-black > div:nth-child(3) > div.flex.items-center > label::text").get()
        # item["rating"] = response.css("#root > main > div.w-full.bg-black > div:nth-child(3) > div:nth-child(3) > div > div.slick-list > div > div:nth-child(3) > div > div > div.bg-zinc-800\/70.w-full > div > div.flex.items-center.pt-3 > span:text").get()
        
        # item["title"] = response.css("#__next > div > div > div.info > div > div.d-block.d-sm-flex.pt-2 > div.right.flex-grow-1.pl-sm-5.pl-0.px-3 > div:nth-child(1) > div.d-flex.flex-column.mt-3.mt-sm-0 > h3::text").get()
        # item["description"] = response.css("#__next > div > div > div.info > div > div.d-block.d-sm-flex.pt-2 > div.right.flex-grow-1.pl-sm-5.pl-0.px-3 > div:nth-child(1) > div.text-normal.overflow-none::text").get()
        # image_url = response.css("#root > main > div.w-full.bg-black > div:nth-child(3) > div:nth-child(3) > div > div.slick-list > div > div:nth-child(2) > div > div > div.relative.h-full.w-full.cursor-pointer.transition-all.duration-500.hover\:brightness-75 > a > img::attr(src)").get()
        
        # image_url = response.urljoin(image_url)
        # item['image_urls'] = [image_url]
        # print("khang123", image_url)

        yield item

        
    # def parse_item(self, response):
    #     yield {
    #         "title": response.css(".bluetext::text").get(),
    #         "des": response.css(".text-normal div::text").get(),
    #         # "availability": response.css(".availability::text")[2].get().replace("\n", "").replece(" ", ""),
    #     }