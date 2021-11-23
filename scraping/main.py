import requests
from bs4 import BeautifulSoup


URL: str = 'https://techgym.jp/?cat=2'


def main():
    response: str = requests.get(URL)
    response.encoding = response.apparent_encoding
    bs: BeautifulSoup = BeautifulSoup(response.text, 'html.parser')
    
    div_post_list: list = bs.select('div.vk_posts')
    for div_post in div_post_list[0].select('div.vk_post'):
        post_date_tag = div_post.select('div.vk_post_date')[0]
        post_date = post_date_tag.text.strip()
        
        post_title_tag = div_post.select('h5.vk_post_title')[0]
        post_title = post_title_tag.text.strip()
        
        print(f'{post_date},{post_title}')
    
if __name__ == '__main__':
    main()