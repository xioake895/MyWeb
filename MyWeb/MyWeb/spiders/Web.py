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
        for href in response.css('.zwmc').css('a::attr(href)').extract():
            url=href
            yield scrapy.Request(url,callback=self.parse_job)

    def parse_job(self,response):
        infoDict={}
        zwmc=response.css('h1').extract()[0][4:-5]#职位名称
        gsmc=re.search(r'[\u4e00-\u9fa5]+',response.css('h2').extract()[0]).group()#公司名称
        gzdd=re.search(r'[\u4e00-\u9fa5]+',response.css('h2').extract()[1]).group()#工作地点
        xzdy=re.search(r'薪资待遇.*[元/月\面议]',response.css('meta').extract()[3]).group()[4:]#薪资待遇
        infoDict.update({"职位名称":zwmc,"公司名称":gsmc,"工作地点":gzdd,"薪资待遇":xzdy})
        yield infoDict
        



