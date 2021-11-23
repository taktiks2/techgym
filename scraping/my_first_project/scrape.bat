echo off
chcp 65001
del article_info.csv
cls
scrapy crawl techgym_basic -o article_info.csv
type article_info.csv

