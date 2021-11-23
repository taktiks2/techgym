import scrapy


class TechgymBasicSpider(scrapy.Spider):
    name = 'techgym_basic'
    allowed_domains = ['techgym.jp']
    start_urls = ['http://techgym.jp/category/event/']

    def parse(self, response):
        articles: list = []
        div_post_list = response.css('div.vk_posts')[0]
        for div_post in div_post_list.css('div.vk_post'):
            post_title = div_post.css('a::text').get()
            post_title = post_title.strip()
            
            post_date = div_post.css('div.vk_post_date::text').get()
            post_date = post_date.strip()
            
            post_info = {
                'date': post_date,
                'title': post_title, 
            }
            
            articles.append(post_info)
        
        return articles
