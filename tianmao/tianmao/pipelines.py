# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql
import codecs

class MysqlPipeline(object):
        def __init__(self):
                self.conn = pymysql.connect('192.168.56.101','root','123456','python',charset='utf8')
                self.cursor = self.conn.cursor()
                print('数据库插入将要开始')
        def process_item(self,item,spider):
                pass
        def close_spider(self,spider):
                self.cursor.close()
                self.conn.close()

class TianmaoPipeline(MysqlPipeline):
        # def __init__(self):
        #     self.file = open('tianmao.json', 'w', encoding='utf-8')
        def process_item(self,item,spider):
                print('开始')
                sql = "insert into tianmao(mingzi,xianka) VALUES(%s,%s) "
                data = (item['name'],item['xianka'])
                try:
                        self.cursor.execute(sql,data)
                        self.conn.commit()
                except Exception as e:
                        print("插入失败",e)
                        self.conn.rollback()
                return item






