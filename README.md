# Crawler Application Using Scrapy, MongoDB and Flask

#Installations
Installed Scrapy, pymongo and flask with the help of pip

To create application I have following steps
#1. Initial set up for the scrapy application


scrapy startproject Crawler

scrapy genspider bbc "bbc.com"
 
#2. Wrote a spider to crawl a singe page and store data into local mongoDB. 
Configured following parameters into settings.py
ITEM_PIPELINES = {'Crawler.pipelines.CrawlerPipeline':300, }
MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "BBCNewsArticles"
MONGODB_COLLECTION = "Article"

#3. Crawling multiple URLs
Add rules to get the crawled urls

rules = (Rule(LinkExtractor(allow=r'/news/[A-Za-z0-9]'), callback='parse_item', follow=True),)
Use CrawlSpider class instead of the Spider class which was used to scrap only single page.

#4. REST based API with flask
An API module has been created to just query the stored articles
Functionlait for the following modules will provide in future

-Authentication Modeule
-Error Handling Module like 404 not found
-Token creation module

#5. Pointing mongodb from compose
Just we need to use mongo URI as follows -

mongodb://<user>:<password>@aws-us-east-1-portal.5.dblayer.com:16777,aws-us-east-1-portal.4.dblayer.com:16777/BBCNewsArticles?ssl=true

#Known Issues
1.I have written code specific to BBC news articles here which can be changed by just giving n no of domains and start urls 
in bbc.py file. 

2.Need to update xpath selectors from bbc.py to find the xpath dynamically which will be valid for any article.
Currently data is populating for most of the articles.

3.Rest API code given here has few modules to query the data from mongodb which can enhenced by providing modules such as authentication, tokenization, etc with request type such as PUT, DELETE.
