# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class TencentPipeline(object):
    def __init__(self):
        self.file = open('tengxun.json', 'w', encoding='utf-8')


    def process_item(self, item, spider):
        print('/////////////////////////')
        str = json.dumps(dict(item),ensure_ascii=False)
        str = str + '\n'
        self.file.write(str)
        #json.dump(dict(item), open('tengxun.json', 'a', encoding='utf-8'), ensure_ascii=False)
        return item

    def close_spider(self,spider):
        self.file.close()



