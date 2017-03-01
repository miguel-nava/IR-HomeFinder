from scrapy.spiders import Spider
from scrapy.http import Request
from ZCrawl.items import ZcrawlItem


class RESpider(Spider):
    name = "ZCrawler"
    city = "Dallas, TX"
    start_urls = ["https://www.trulia.com/TX/Dallas/"]

    def parse(self, response):

        for property in response.css('div.smlCol12.lrgCol8.ptm.cardContainer.positionRelative'):
            item = ZcrawlItem()
            item["price"] = property.css('span.cardPrice.h5.man.pan.typeEmphasize.noWrap.typeTruncate::text').extract()
            item["bedroom"] = property.xpath('div/a/div/div/div/ul/li[contains(@data-auto-test, "beds")]/text()')\
                .extract()
            item["bathroom"] = property.xpath('div/a/div/div/div/ul/li[contains(@data-auto-test, "baths")]/text()')\
                .extract()
            item["sqft"] = property.xpath('div/a/div/div/div/ul/li[contains(@data-auto-test, "sqft")]/text()')\
                .extract()
            item["address"] = property.xpath('div/a/div/div/div/p/text()').extract()
            item["link"] = property.xpath('div/a/@href').extract()
            item["city"] = RESpider.city
            yield item

        next_Page = response.xpath('//a[contains(@aria-label, "Next")]/@href').extract()
        if next_Page is not None:
            nextPage = "https:" + next_Page[0]
            print ('\n\n', str(nextPage), '\n\n')
            yield Request(nextPage, callback=self.parse)