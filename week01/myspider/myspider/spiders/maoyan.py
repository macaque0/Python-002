import scrapy
from scrapy.selector import Selector
from myspider.items import MyspiderItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):
        print(f"======================parse start{response.url}")
        divs = Selector(response=response).xpath(
            '//div[@class="movie-hover-info"]')
        for index in range(len(divs)):
            if(index < 10):
                item = MyspiderItem()
                # 名称
                name = divs[index].xpath('./div[1]/span[1]/text()').extract_first()
                # print(name)
                item['name'] = name
                # 类型
                cat = divs[index].xpath('./div[2]/text()').extract()[1].strip().replace('\n', '').replace('\r', '')
                # print(cat)
                item['cat'] = cat
                # 日期
                date = divs[index].xpath('./div[4]/text()').extract()[1].strip().replace('\n', '').replace('\r', '')
                # print(date)
                item['date'] = date
                yield item
