
from scrapy import Spider, Request
import urllib


class TvSpider(Spider):
    name = 'tvspider'
    start_urls = ['https://www.channel4.com/categories']



    def parse(self, response):
        for title in response.css('div.all4-slice-item__label::text'):
            yield {'title': title.get()}

        iter = 20
        page = response.css('a.all4-primary-button::attr(href)').get()
        with iter < 80:
            next_page = page.replace(page, page[:-2]+str(20+iter))
            next_page = response.urljoin(next_page)
            yield Request(next_page, callback=self.parse)
            iter+= iter
