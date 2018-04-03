# -*- coding: utf-8 -*-
import scrapy
from tianmao.items import TianmaoItem
import json

class MaoSpider(scrapy.Spider):
    name = 'mao'
    start_urls = ['https://list.tmall.com/search_product.htm?s=0&q=%B1%CA%BC%C7%B1%BE%B5%E7%C4%D4']

    def parse(self, response):
        #a = response.text
        nao_list=response.xpath('//div[@id="content"]//div[@class="view grid-nosku view-noCom"]/div')
        for i in nao_list:
            item = TianmaoItem()
            name = i.xpath('./div[@class="product-iWrap"]/div[@class="productTitle productTitle-spu"]/a[1]/text()').extract()
            name= self.getvalue(name)
            xianka = i.xpath('./div[@class="product-iWrap"]/div[@class="productTitle productTitle-spu"]/a[2]/text()').extract()
            xianka= self.getvalue(xianka).strip()
            CPU = i.xpath('./div[@class="product-iWrap"]/div[@class="productTitle productTitle-spu"]/a[3]/text()').extract()
            CPU= self.getvalue(CPU).strip()
            PMsize= i.xpath('./div[@class="product-iWrap"]/div[@class="productTitle productTitle-spu"]/a[4]/text()').extract()
            PMsize= self.getvalue(PMsize).strip()
            #详情页URL
            url = i.xpath('./div[@class="product-iWrap"]/div[@class="productImg-wrap"]/a[1]/@href').extract()
            url ='https:'+self.getvalue(url).strip()

            item["name"]=name
            item["xianka"]=xianka
            item["CPU"] = CPU
            item["PMsize"] =PMsize
            item["url"] = url

            yield scrapy.Request(url=url,callback=self.xiangqing,meta={"data":item,"phantomjs":True},dont_filter=True)

    def xiangqing(self,response):

        item  =response.meta.get('data')
        #天猫详情页
        comment = response.xpath('//*[@id="J_ItemRates"]/div/span[2]/text()').extract()
        comment = self.getvalue(comment)
        item['comment'] = comment
        xiaoliang = response.xpath('//*[@id="J_DetailMeta"]/div/div[1]/div/ul/li[1]/div/span[2]/text()').extract()
        xiaoliang = self.getvalue(xiaoliang)
        item['xiaoliang'] = xiaoliang
        for i in range(1,10):
            url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=558682286451&spuId=878586816&sellerId=686773455&order=3&currentPage=2&append=0&content=1'
            yield  scrapy.Request(url=url,meta={"data":item},callback=self.pingjia,dont_filter=True)
    #用户名家
    def pingjia(self,response):
        item  = response.meta['data']
        xinxi = response.body.decode('utf-8')
        item['pingjia'] = xinxi
        yield item
    def getvalue(self,value):
        return value[0] if value else '无'

