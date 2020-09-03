import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from Ckart.items import CkartItem
from scrapy.http import Request, Response
from Ckart.settings import *

class HDDSpider(CrawlSpider):
    name = "hard_disk_infibeam"
    allowed_domains=['infibeam.com']
    start_urls = ['http://www.infibeam.com/Hard_Disk_Computers_Accessories/']
    allow_url="^(http:\/)?\/?([^:\/\s]+)((\/\w+)*\/)([\w\-\.]+[^#?\s]+)(.*)?(#[\w\-]+)?$"

    #rules = (Rule( LxmlLinkExtractor(allow=allow_url,allow_domains=("www.infibeam.com"),)
      #  ,callback='parse',follow=True))
    #rules = (Rule(LxmlLinkExtractor(allow=('/Hard_Disk_Computers_Accessories'),restrict_xpaths=('//div[@id="searchCont"]')),callback="parse", follow=True),)

    def parse(self, response):
        #hxs = Selector(response)

        product_name = response.xpath('//*[@class="thumbnail"]')
        items = []
        count_title = -1
        for prod_name in product_name:
            item = CkartItem()
            
            item ['title'] = prod_name.xpath("//div[@class='title']/a/text()")[count_title].extract()
            item ['price'] = prod_name.xpath("//span[@class='final-price']/text()")[count_title].extract()
            #item ['url'] = response.url

            items.append(item)
            count_title+=1

        for item in items:
            yield item
        
        next_page = response.xpath("//span[@class='see-more']/a/@href").extract()
        if next_page:
            for x in next_page:
                link_page = x
                url = 'http://www.infibeam.com{}'.format(''.join(link_page))
                yield Request(url, self.parse)

