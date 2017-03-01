# IR-HomeFinder

How to run:__
clone repo__
Install scrapy: 'pip install scrapy'__
Working python version: 3.6.0__
navigate to ZCrawl directory__
Change your baseURL and change code for "next page" accordingly to whatever website you are crawling__
run: 'scrapy runspider spiders/ZCrawler.py -o <outputFile>.json -t json --logfile=log.txt'__