# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import redis

class redisPopeline(object):
    def __init__(self):
            self.r = redis.Redis(host='localhost',port=6379,db=0)
    def process_item(self,item,spider):
        pass

class PapaPipeline(redisPopeline):
    def process_item(self, item, spider):
        print('kaishi')
        self.r.hmset(item['id'],{'name':item['name'],'headline':item['headline']})
        print('成功')
        return item

