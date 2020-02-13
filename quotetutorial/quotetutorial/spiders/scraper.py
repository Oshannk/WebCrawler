import scrapy
import  re

from ..items import QuotetutorialItem

class scraper(scrapy.Spider):
    name = 'myspider'

    #start_urls = ['http://quotes.toscrape.com/']

    def start_requests(self):
        urls = ['http://quotes.toscrape.com/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        #print('url:', response.url)

        #for pattern in ['word']:
        #print('>>> pattern:', pattern)
        #result = response.css('body').re(pattern)
        #print('>>>          re:', len(result), result)

        items = QuotetutorialItem()

        result = re.findall('world', response.text)
        print('url:', response.url)
        print('>>> response.re:', len(result), result)

        #item['meta'] = response.xpath("//meta[@class='keywords']/@content").get()
        items['meta'] = response.xpath("//meta[@class='keywords']/@content").get()
        #print('meta:', meta_content)

        #gg = response.url
        yield items

