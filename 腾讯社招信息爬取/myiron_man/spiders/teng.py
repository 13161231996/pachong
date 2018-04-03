# -*- coding: utf-8 -*-
import scrapy
from myiron_man.items import TencentItem
from urllib import request


class TengSpider(scrapy.Spider):
    name = 'teng'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?&start=0']

    def parse(self, response):
        jobs1 =response.xpath('//tr[@class="even"]')
        jobs2 = response.xpath('//tr[@class="odd"]')
        jobs = jobs1+jobs2
        for job in jobs:
            item = TencentItem()
            #url
            href = job.xpath('./td[1]/a/@href').extract()[0]
            href = request.urljoin(response.url,href)

            #工种
            gongzhong = job.xpath('./td[2]/text()').extract()
            gongzhong = self.getvalue(gongzhong)

            #地点
            didian = job.xpath('./td[4]/text()').extract()[0]
            #职位名称
            zhiwei = job.xpath('./td[1]/a/text()').extract()[0]
            #时间
            data = job.xpath('./td[5]/text()').extract()[0]
            item['time'] = data
            item['zhiwu'] = zhiwei
            item['didian'] = didian
            item['gongzhong'] = gongzhong

            yield scrapy.Request(url=href,callback=self.detail,meta={'data':item})

        #下一页
        next_url = response.xpath('//a[@id="next"]/@href').extract()[0]
        next_url = request.urljoin(response.url,next_url)
        print(next_url)

        #是否是最后一页
        last_page = response.xpath('//a[@id="next"]/@class').extract()
        last_page = self.getvalue(last_page)

        if last_page != 'noactive':
            yield scrapy.Request(url=next_url,callback=self.parse)

    def detail(self,response):
        print('aaaaaaaaaaaaaa')
        item = response.meta['data']

        #工作职责
        duty = response.xpath('//tr[@class="c"][1]//li/text()').extract()
        duty = ''.join(duty)
        item["duty"] = duty

        #工作要求
        yq = response.xpath('//tr[@class="c"][2]//li/text()').extract()
        item["yq"] = ''.join(yq)

        yield item

    def getvalue(self,value):
        return value[0] if value else ''