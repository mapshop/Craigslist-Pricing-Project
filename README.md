Craigslist-Pricing-Project
==========================

1. Enter directory that you want to store the scraper and then in CMD enter: 

      scrapy startproject tutorial

2. Change base url to specific craigslist apartment link e.g. http://sfbay.craigslist.org/search/apa for San Francisco

3. To run the scraper type in the directory: 

    scrapy crawl craig -o items.csv -t csv

For more in-depth to customize, here's the blog post:

https://racketracer.wordpress.com/2015/01/29/practical-scraping-using-scrapy/

Replace the pipelines.py file with an empty file if you don't want to store the data in a postgresql database. 


##More notes

Installs (if not already installed)

* pip install scrapy
* pip install sqlalchemy

Postgres

* Database needs to be created and the server running before you start the spider
* Not sure if postgis is necessary, but I used it.

Start urls

* Timed out at 500 requests before I added the expanded list of start urls.

Maps

* Doesn't seem to retrieve listings that don't have maps in them

True/False

* I turned all the nullify booleans to True in the spider to stop the null errors I was getting. 

Titles

* Got very few records with titles, not sure why.











