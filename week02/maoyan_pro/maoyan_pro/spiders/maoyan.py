import scrapy
from scrapy.selector import Selector
from maoyan_pro.items import MaoyanItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    # def parse(self, response):
    #     pass

    def parse(self, response):
        details = Selector(response=response).xpath(
            '//div[@class="movie-item film-channel"]')

        for i in range(30):
            detail = details[i]
            title = detail.xpath(
                './/span[contains(@class,"name")]/text()').extract_first()
            hover_texts = detail.xpath(
                './/span[@class="hover-tag"]/../text()').extract()
            types = hover_texts[1].strip('\n').strip()
            plan_date = hover_texts[5].strip('\n').strip()

            item = MaoyanItem()
            item['title'] = title
            item['types'] = types
            item['plan_date'] = plan_date
            yield item
