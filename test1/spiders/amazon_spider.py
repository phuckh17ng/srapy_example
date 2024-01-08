from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CrawlingSpider(CrawlSpider):
    # name for spider
    name = "amazon-crawler"

    # a list of domains that this spider is allowed to crawl
    # allowed_domains = ["toscrape.com"]

    # a list of domains that this spider will be allowed to crawl from, when no particular URLs are specified
    # start_urls = ["http://books.toscrape.com/"]

    allowed_domains = ["amazon.com"]
    # start_urls = ["https://amazon.com/"]
    start_urls = ["https://www.amazon.com/s?i=specialty-aps&bbn=16225007011&rh=n%3A16225007011%2Cn%3A13896617011&ref=nav_em__nav_desktop_sa_intl_computers_tablets_0_2_6_4"]
    # PROXY_SERVER = "172.68.1.1"

    rules = (
        # Rule(LinkExtractor(allow="catalogue")),
        # Rule(LinkExtractor(allow="truyen/name")),
        Rule(callback="parse_item"),
    )
    # rules = (
    #     Rule(LinkExtractor(allow="truyen"), callback="parse_item"),
    #     Rule(LinkExtractor(allow="truyen", deny="name"), callback="parse_item")
    # )

    def parse_item(self, response):       
        item = {}
        item["title"] = response.css("#search > div.s-desktop-width-max.s-desktop-content.s-wide-grid-style-t1.s-opposite-dir.s-wide-grid-style.sg-row > div.sg-col-20-of-24.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16 > div > span.rush-component.s-latency-cf-section > div.s-main-slot.s-result-list.s-search-results.sg-row > div:nth-child(7) > div > div > span > div > div > div.a-section.a-spacing-small.puis-padding-left-small.puis-padding-right-small > div.a-section.a-spacing-none.a-spacing-top-small.s-title-instructions-style > h2 > a > span::text").get()
        # item["title"] = response.css("#__next > div > div > div.info > div > div.d-block.d-sm-flex.pt-2 > div.right.flex-grow-1.pl-sm-5.pl-0.px-3 > div:nth-child(1) > div.d-flex.flex-column.mt-3.mt-sm-0 > h3::text").get()
        # item["description"] = response.css("#__next > div > div > div.info > div > div.d-block.d-sm-flex.pt-2 > div.right.flex-grow-1.pl-sm-5.pl-0.px-3 > div:nth-child(1) > div.text-normal.overflow-none::text").get()
        # image_url = response.css("#__next > div > div > div.info > div > div.d-block.d-sm-flex.pt-2 > div.left.d-flex.d-sm-block.justify-content-center.align-items-center > div.position-relative.mr-4.mr-sm-0 > div > span > img::attr(src)").get()
        
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