# Crawler Application Using Scrapy, MongoDB and Flask

#Installations
Installed Scrapy, pymongo and flask with the help of pip

To create application I have following steps
#1. Initial set up for the scrapy application

```python
scrapy startproject Crawler
scrapy genspider bbc "bbc.com"
```

#2. Wrote a spider to crawl a singe page and store data into local mongoDB. 
Configured following parameters into settings.py

```python
ITEM_PIPELINES = {'Crawler.pipelines.CrawlerPipeline':300, }
MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "BBCNewsArticles"
MONGODB_COLLECTION = "Article"
```
#3. Crawling multiple URLs
Add rules to get the crawled urls
```python
rules = (Rule(LinkExtractor(allow=r'/news/[A-Za-z0-9]'), callback='parse_item', follow=True),)
```

Use CrawlSpider class instead of the Spider class which was used to scrap only single page.

#4. REST based API with flask
An API module has been created to just query the stored articles. Since I am creating it locally I am using functions as in stanalone local appliation. This can be easily used as REST based APIs will small changes!
Start the Flask application on port 5000 from command line. Use commands as follows - 
```python
cd "D:\Projects\Crawler\Crawler\CrawlerRestAPIWithFlask"
python app.py
```
Application if started without error will display following message -
![Home](https://github.com/dattatrayshinde/Crawler/blob/master/Screenshots/home.png)

Function to get all Articles
http://localhost:5000/Articles

![All Articles](https://github.com/dattatrayshinde/Crawler/blob/master/Screenshots/GET%20ALL%20ARTICLES.png)

Function to get srearch result for the specific query
http://localhost:5000/Articles/trump

![Search Result for 'trump'](https://github.com/dattatrayshinde/Crawler/blob/master/Screenshots/Trump%20Search.png)

Here we are going to search trump in all our scraped articles from mongoDB
Result is as follows -Four articles contains the searched text. Here we are searching for 'trump'.

To make REST API more secure and mature we have to provide following modeules also.
-Authentication Modeule

-Token creation module

-Error Handling Module like 404 not found

#5. Pointing mongodb from compose
Just we need to use mongo URI as follows -
```python
mongodb://<user>:<password>@aws-us-east-1-portal.5.dblayer.com:16777,aws-us-east-1-portal.4.dblayer.com:16777/BBCNewsArticles?ssl=true
```

#Known Issues
1.I have written code specific to BBC news articles here which can be changed by just giving n no of domains and start urls 
in bbc.py file. 

2.Need to update xpath selectors from bbc.py to find the xpath dynamically which will be valid for any article.
Currently data is populating for most of the articles.

3.Rest API code given here has few modules to query the data from mongodb which can enhenced by providing modules such as authentication, tokenization, etc with request type such as PUT, DELETE.
