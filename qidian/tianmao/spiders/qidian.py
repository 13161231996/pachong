# -*- coding: utf-8 -*-
import scrapy
from tianmao.items import qidianItem
from urllib import request
class QidianSpider(scrapy.Spider):
    name = 'qidian'
    allowed_domains = ['qidian.com']
    start_urls = ['https://www.qidian.com/free/all?orderId=&vip=hidden&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=1&page=1']
    def parse(self, response):
        #获取每一个书的url
        book = response.xpath('//div[@class="book-mid-info"]/h4/a/@href').extract()
        for bookurl in book:
            yield scrapy.Request("https:"+bookurl, callback=self.parsebook,dont_filter=True)
        #下一页
        next_url = response.xpath('//a[@class="lbf-pagination-next "]/@href').extract()[0]
        next_url = request.urljoin(response.url,next_url)
        #是否是最后一页
        last_page = response.xpath('//a[@class="lbf-pagination-next lbf-pagination-disabled"]/@href').extract()
        #防止列表没有值
        last_page = self.getvalue(last_page)
        #最后一页结束进行判断
        if last_page != 'javascript:;':
            yield scrapy.Request(url=next_url,callback=self.parse)

    def parsebook(self,response):
        a = response.xpath('//div[@class="volume-wrap"]/div[@class="volume"]/ul[@class="cf"]/li')
        #小说名
        shuming = response.xpath('//div[@class="book-info "]/h1/em/text()').extract()[0]
        item = qidianItem()
        item['title']=shuming
        for i in a:
            #获取每个章节的url
            charturl = i.xpath('./a/@href').extract()[0]
            yield scrapy.Request("https:"+charturl, callback=self.parse_chart,meta={'data':item},dont_filter=True)

    def parse_chart(self,response):
        item =response.meta['data']
        # 获取章节名
        biaoti =response.xpath('//h3[@class="j_chapterName"]/text()').extract()
        content = ''
        for biaot in biaoti:
            content = content+biaot+'\n'
        #     #获取每一章的内容
        text = response.xpath('//div[@class="read-content j_readContent"]//p/text()').extract()
        wenben =''
        for wen in text:
            wenben = wenben+wen.strip()
        item['desc']=content+wenben
        yield item

    def getvalue(self,value):
        return value[0] if value else ''


