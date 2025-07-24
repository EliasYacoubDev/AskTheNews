import scrapy

class BBCSpider(scrapy.Spider):
    name = 'bbc_headlines'
    start_urls = ['https://feeds.bbci.co.uk/news/rss.xml']

    def parse(self, response):
        for item in response.css('item'):
            yield{
                'title': item.css('title::text').get(),
                'link': item.css('link::text').get(),
                'pubDate': item.css('pubDate::text').get()
            }