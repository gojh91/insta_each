# -*- coding: utf-8 -*-
import scrapy
import requests
import json
import urllib.request
import datetime as dt
import pandas as pd
import csv
from instascrapy_each.items import InstascrapyEachItem

class InstagramSpider(scrapy.Spider):
    name = 'instagram_each'
    allowed_domains = ['instagram.com']
    start_urls = []
    csvname = "키즈존"

    #def start_requests(self):
    df = pd.read_csv('C:\\Users\\student\\Desktop\\insta_crawling\\인스타 끝난 자료\\' + csvname + '.csv')
    for each_url in df['each_url']:
        print("each_url : " + each_url)
        shortcode = each_url.split('"')[3]
        start_urls.append('https://www.instagram.com/p/' + shortcode + '/?__a=1')
        # start_urls.append(each_url)
           # yield scrapy.Request(url=each_url, callback=self.parse)

    def parse(self, response):
        print('response.url : ' + response.url)
        each_json_data = json.loads(response.body)
        
        print("each_json_data : " + str(each_json_data))
        item = InstascrapyEachItem()

        item['each_url'] = response.url
        
        # item['each_location'] = each_json_data['data']['shortcode_media']['location']['name']
        
        # item['address_json'] = each_json_data['data']['shortcode_media']['location']['address_json']

        item['each_location'] = each_json_data['graphql']['shortcode_media']['location']['name']
        
        item['address_json'] = each_json_data['graphql']['shortcode_media']['location']['address_json']

        yield item