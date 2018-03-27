# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs

class qidianPipline(object):

        def process_item(self,item,spider):
                # 根据书名来创建文件,
                self.file = codecs.open("小说/"+item['title'] + '.txt', 'a', encoding='utf-8')
                self.file.write(item["desc"] + "\n")
                print('正在下载！！！！！！！！！！'+item['title'])
                return item
        def spider_closed(self,spider):
                self.file.close()


