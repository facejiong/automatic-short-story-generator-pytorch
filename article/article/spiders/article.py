# -*- coding: utf-8 -*-
import scrapy

class ArticleSpider(scrapy.Spider):
    name = "article"

    def start_requests(self):
        baseUrl = "http://m.91read.net/show/"
        sum = 20000
        counter = 1
        while counter <= sum:
            url = baseUrl + str(counter) + ".html"
            counter += 1
            yield scrapy.Request(url=url, callback=self.parse)
            

    def parse(self, response):
        title = response.css(".article-title::text").get()
        content = response.css(".article-content::text").get()
        yield {
            'title': title,
            'content': content,
        }