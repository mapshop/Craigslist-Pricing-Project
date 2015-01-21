# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 15:02:19 2014

@author: Jay
"""

import scrapy
#import pandas as pd


#Item class with listed fields to scrape
class CraigslistItem(scrapy.Item):
    date = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
    area = scrapy.Field()
    beds = scrapy.Field()
    size = scrapy.Field()
    CraigID = scrapy.Field()
    numPic = scrapy.Field()
    coord = scrapy.Field()
    postDate = scrapy.Field()
    updateDate = scrapy.Field()
    content = scrapy.Field()
    baths = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    contentLen = scrapy.Field()

class MySpider(scrapy.Spider):
    name = "craig"
    allowed_domains = ["craigslist.org"]
    #Base url for Seattle apartment rentals. Change if necessary
    base_url = "http://seattle.craigslist.org/search/apa?"
    start_urls = ["http://seattle.craigslist.org/search/apa?"]
    #Initially grab all of the urls up to where craigslist allows
    #In this case, it's 2400 
    for i in range(1, 24):
        start_urls.append(base_url + "s=" + str(i) + "00&")
        
#    def __init__(self):
#        global df
#        test = CraigslistItem()
#        test = self.initialize(test)
#        df = pd.DataFrame(columns = list(test.keys()), index=xrange(0,2400))

    def parse(self, response):
        #find all postings
        postings = response.xpath(".//p")
        #loop through the postings
        for i in range(0, len(postings)-1):
            item = CraigslistItem()
            #grab craiglist apartment listing ID
            item["CraigID"] = postings[i].xpath("@data-pid").extract()
            temp = postings[i].xpath("span[@class='txt']")
            info = temp.xpath("span[@class='pl']")
            #title of posting
            item["title"] = info.xpath("a/text()").extract()
            #date of posting
            item["date"] = info.xpath("time/text()").extract()
            #pre-processing for getting the price in the right format
            price = ''.join(temp.xpath("span")[2].xpath("span[@class='price']").xpath("text()").extract())
            item["price"] = price.replace("$","")
            item["link"] = info.xpath("a/@href").extract()
            follow = "http://seattle.craigslist.org" +''.join(item["link"])
            #Parse request to follow the posting link into the actual post
            request = scrapy.Request(follow , callback=self.parse_item_page)
            request.meta['item'] = item
            #self.df.loc[i] = pd.Series(item)
            yield request

    #Parsing method to grab items from inside the individual postings
    def parse_item_page(self, response):
        item = response.meta["item"]
        maplocation = response.xpath("//div[contains(@id,'map')]")
        latitude = maplocation.xpath('@data-latitude').extract()
        longitude = maplocation.xpath('@data-longitude').extract()
        attr = response.xpath("//p[@class='attrgroup']")
        try:
            item["beds"] = attr.xpath("span/b/text()")[0].extract()
            bath = attr.xpath("span/b/text()")[1].extract()
            item["size"] = attr.xpath("span")[1].xpath("b/text()").extract()
            if(bath.isdigit()):
                item["baths"] = attr.xpath("span/b/text()")[1].extract()
            item["baths"] = bath
        except:
            pass
        item["contentLen"] = len(response.xpath("//section[@id='postingbody']").xpath("text()").extract())
        item["latitude"] = latitude
        item["longitude"] = longitude
        item["coord"] = ''.join(latitude) + ", " + ''.join(longitude)
        postinginfo = response.xpath("//p[@class = 'postinginfo']").xpath("time/@datetime")
        item["postDate"] = postinginfo[0].extract()
        item["updateDate"] = postinginfo[len(postinginfo)-1].extract()
        item["numPic"] = len(response.xpath("//div[@id='thumbs']").xpath("a"))
        return item
        
            