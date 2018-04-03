# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field

class PapaItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #允许消息
    allow_message = Field()
    #回答数
    answer_count = Field()
    #文章数
    articles_count = Field()
    #头像url
    avatar_url = Field()
    #头像url 模板
    avatar_url_template = Field()
    #徽章
    badge = Field()
    #工作
    employments = Field()
    #粉丝数量
    follower_count = Field()
    #性别
    gender = Field()
    #标题
    headline = Field()
    #ID
    id = Field()
    #广告
    is_advertiser = Field()
    #关注
    is_followed = Field()
    #被关注
    is_following = Field()
    #名字
    name = Field()
    #类型
    type = Field()
    #url
    url = Field()
    #url令牌
    url_token = Field()
    #用户类型
    user_type = Field()
