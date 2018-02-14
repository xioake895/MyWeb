# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class MyWebPipeline(object):
    def process_item(self, item, spider):
        return item
        
class MyWebInfoPipeline(object):
    def open_spider(self,spider):
        self.f=open('MyWebInfo.txt','w',encoding='utf-8')

    def close_spider(self,spider):
        self.f.close()

    def process_item(self,item,spider):
        try:
            line=str(dict(item))+'\n'
            self.f.write(line)
        except:
            pass
        return item

