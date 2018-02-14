# -*- coding: utf-8 -*-
import scrapy
import re

class WebSpider(scrapy.Spider):
    name = 'Web'
    #allowed_domains = ['zhilian.com']
    kw="python"
    jl="大连"
    start_urls = ['http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%s&kw=%s'%(jl,kw)]
    
    def parse(self, response):
        '''
        infoDict={}
        count=0
        for table in response.css('table'):
            count+=1
            #self.log(table.extract())
            #try:
            jobname=table.css('.zwmc').xpath('string(div/a)').extract()#职位名称
            company=table.css('.gsmc').xpath('string(a)').extract()#公司名称
            price=table.css('.zwyx').extract()[0][17:-5]#月薪
            address=table.css('.gzdd').extract()[0][17:-5]#工作地点
            infoDict.update({"序号%s"%count:count,"职位名称%s"%count:jobname,"公司名称%s"%count:company,"月薪%s"%count:price,"工作地点%s"%count:address})
            #except:
                #continue
        yield infoDict
        '''
        for href in response.css('.zwmc').css('a::attr(href)').extract():
            url=href
            yield scrapy.Request(url,callback=self.parse_job)

    def parse_job(self,response):
        infoDict={}
        zwmc=response.css('h1').extract()[0][4:-5]#职位名称
        h2=response.css('h2').extract()[0]#
        gsmc=re.search(r'[\u4e00-\u9fa5]+',h2).group()#公司名称
        '''gzdd=h2[1][4:-5]
        self.log(gzdd)
        
        xinzi=response.css('ul').extract()[0]
        price=re.findall(r'<strong>.*?<',xinzi)
        self.log(price)'''
        
        infoDict.update({"职位名称":zwmc,"公司名称":gsmc})
        #self.log(h2)
        yield infoDict
        



