# IR-HomeFinder

How to run:<br />
clone repo<br />
Install scrapy: 'pip install scrapy'<br />
Working python version: 3.6.0<br />
navigate to ZCrawl directory<br />
Change your baseURL and change code for "next page" accordingly to whatever website you are crawling<br />
run: 'scrapy runspider spiders/ZCrawler.py -o <outputFile>.json -t json --logfile=log.txt'<br />
