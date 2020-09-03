import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from Ckart.items import CkartItem
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor

class Mobiles_snapdeal(CrawlSpider):
    name = "mobile_snapdeal"
    allowed_domains = ["snapdeal.com"]
    start_urls = ['http://www.snapdeal.com/products/mobiles?sort=plrty&']

    def parse(self, response):

        items = []
        count = 0
        mobile = response.xpath('//div[@class="productWrapper"]')
        for sel in mobile:
        	item = CkartItem()
    		item['title'] = map(unicode.strip, sel.xpath('//div[@class="product-title"]/a/text()').extract())[count]
                item['price'] = map(unicode.strip, sel.xpath('//div[@class="product-price"]/div/span[@id="price"]/text()').extract())[count]
                items.append(item)
                count+=1
        return items

        