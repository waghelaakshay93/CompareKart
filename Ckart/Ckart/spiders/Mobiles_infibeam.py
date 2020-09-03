import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from Ckart.items import CkartItem
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.http import Request, Response

class Mobiles_infibeam(CrawlSpider):
    name = "mobile_infi"
    allowed_domains = ["infibeam.com"]
    start_urls = ['http://www.infibeam.com/Mobiles/']

    #rules = (Rule(LxmlLinkExtractor(allow=('')),callback="parse_item",follow=True))
    #rules = (Rule(LxmlLinkExtractor(allow='/Mobiles',allow_domains=("www.infibeam.com"),)
     #   ,callback='parse_item',follow=True))

    #rules = (Rule(LxmlLinkExtractor(allow=(''),restrict_xpaths=('//div[@class="searchCont"]')),callback="parse_item", follow=True))
                                            #/Mobiles/search\?make
    rules = (Rule(LxmlLinkExtractor(allow=("/Mobiles/search\?make"),deny=('\?/pricerange','/?\features','\?/sort')),callback="parse_item", follow=True),)
#,restrict_xpaths=('//div[@id="searchCont"]')

    def parse_item(self, response):

        items = []
        count = -1
        mobile = response.xpath('//*[@class="thumbnail"]')
        for sel in mobile:
        	item = CkartItem()
    		item['title'] = sel.xpath('//div[@class="title"]/a/text()').extract()[count]
                item['price'] = sel.xpath('//span[@class="final-price"]/text()').extract()[count]
                item['url'] = response.url
                items.append(item)
                count+=1   
        #return items

        for item in items:
            yield item
        
        """next_page = sel.xpath("//li[@class='level-1']/a/@href").extract()
        if next_page:
            for x in next_page:
                link_page = x
                url = 'http://www.infibeam.com{}'.format(''.join(link_page))
                yield Request(url, self.parse_item)"""