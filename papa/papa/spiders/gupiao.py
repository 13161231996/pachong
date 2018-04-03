# -*- coding: utf-8 -*-
import scrapy
import json
import re
from papa.items import PapaItem


class GupiaoSpider(scrapy.Spider):
    name = 'gupiao'
    allowed_domains = ["www.zhihu.com"]
    start_urls = ['http://www.zhihu.com']
    start_user = 'excited-vczh'
    #用户的基本信息
    user_url = 'https://www.zhihu.com/api/v4/members/{user}?include={include}'
    #include
    user_query ='allow_message%2Cis_followed%2Cis_following%2Cis_org%2Cis_blocking%2Cemployments%2Canswer_count%2Cfollower_count%2Carticles_count%2Cgender%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics'
    #这个用户关注了谁
    follows_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&offset={offset}&limit={limit}'
    #用户关注的include
    follows_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'
    #谁关注了这个用户
    followers_url = 'https://www.zhihu.com/api/v4/members/{user}/followers?include={include}&offset={offset}&limit={limit}'
    #关注永固的include
    followers_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'
    def start_requests(self):
        #用户查询
        yield  scrapy.Request(url=self.user_url.format(user =self.start_user,include=self.user_query),callback=self.parse_user)
        #用户关注的列表
        yield  scrapy.Request(url=self.follows_url.format(user=self.start_user,include=self.follows_query,offset=0,limit=20),callback=self.parse_follows)
        #关注用户的列表
        yield  scrapy.Request(url=self.followers_url.format(user=self.start_user,include=self.follows_query,offset=0,limit=20),callback=self.parse_followers)

    def parse_user(self, response):
        #返回时json 直接loads
        result = json.loads(response.text)
        item = PapaItem()
        #判断拿到的信息是否在自己定义的字段中
        for field in item.fields:
            if field in result.keys():
                #把json数据中相应键的值，进行赋值
                item[field] = result.get(field)
        yield item
        #调用用户关注的用户的信息，url_token是每个用户的名称，为字母
        yield scrapy.Request(self.follows_url.format(user = result.get('url_token'),include=self.follows_query,offset=0,limit=20),callback=self.parse_follows)
       #调用关注用户的信息
        yield scrapy.Request(self.followers_url.format(user = result.get('url_token'),include=self.followers_query,offset=0,limit=20),callback=self.parse_followers)
    #用户关注
    def parse_follows(self,response):
        results = json.loads(response.text)
        #用户关注的dada键的值筛选目标值
        if 'data' in results.keys():
            for result in results.get('data'):
                yield scrapy.Request(self.user_url.format(user=result.get('url_token'),include=self.user_query),callback=self.parse_user)
        #判断是否有下一页
        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            #获取下一页链接
            next_page = results.get('paging').get('next')
            #回调
            yield scrapy.Request(next_page, self.parse_follows)
    #关注用户
    def parse_followers(self,response):
        results = json.loads(response.text)
        # 关注用户的dada键的值筛选目标值
        if 'data' in results.keys():
            for result in results.get('data'):
                yield scrapy.Request(self.user_url.format(user=result.get('url_token'), include=self.user_query),callback=self.parse_user)
        #获取下一页的链接
        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            #回调
            yield scrapy.Request(next_page, self.parse_followers)


