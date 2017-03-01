# IR-HomeFinder

How to run:

clone repo
Install scrapy: 'pip install scrapy'
Working python version: 3.6.0
navigate to ZCrawl directory
Change your baseURL and change code for "next page" accordingly to whatever website you are crawling
run: 'scrapy runspider spiders/ZCrawler.py -o <outputFile>.json -t json --logfile=log.txt'