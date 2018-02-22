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
        '''
        try:
            line=str(dict(item))+'\n'
            self.f.write(line)
            info=dict(item)
            zwmc=info['职位名称']
            gsmc=info['公司名称']
            gzdd=info['工作地点']
            xzdy=info['薪资待遇']
            line.append([zwmc,gsmc,gzdd,xzdy])

            self.f.write(str(line)+'\n')
        except:
            pass
        '''
        info=dict(item)
        zwmc=info['职位名称']
        gsmc=info['公司名称']
        gzdd=info['工作地点']
        xzdy=info['薪资待遇']
        #tl="{0:^10}\t{1:{4}^10}\t{2:{4}^10}\t{3:{4}^10}"
        len1=45-len(zwmc.encode("GBK"))+len(zwmc)
        len2=35-len(gsmc.encode("GBK"))+len(gsmc)
        len3=25-len(gzdd.encode("GBK"))+len(gzdd)
        len4=22-len(xzdy.encode("GBK"))+len(xzdy)
        tl="{0:{8}<{4}}{1:{8}<{5}}{2:{8}<{6}}{3:{8}<{7}}"
        i=tl.format(zwmc,gsmc,gzdd,xzdy,len1,len2,len3,len4,'*')
        #line.append([zwmc,gsmc,gzdd,xzdy])
        self.f.write(i+'\n')
        return item

