# FLIPKART-REVIEW-SCRAPPER
Customer review scrapper for Flipkart products

## Link to Heroku website :  
https://sundi-review-scraper.herokuapp.com/

## What is a webscrapper ?
Web scraping is a technique using which the webpages from the internet are fetched and parsed to understand and extract specific information similar to a human being. Web scrapping consists of two parts: 
•	Web Crawling -Accessing the webpages over the internet and pulling data from them. 
•	HTML parsing -Parsing the HTML content of the webpages obtained through web crawling and then extracting specific information from it. 

## Explanation of what code does :
a)	The application internally opens the Flipkart page and searches for the product and parses the webpage in html format .

b)	Once we have the entire HTML page, we try to get the product URL and then jump to the product page. 

c)	On the product page, we find which HTML section contains the customer comments. We do it by inspecting elements on the page from the element-wise view of the HTML page. 

d)	Once we have the list of all the comments, we extract the customer name ,the rating ,comment heading and the customer comment from the tags. 

e)	After that, we’ll return the ‘results.html’ page as the response to the user containing all the reviews. 

f)	If we run the app from our local system the the scraped reviews are stored as csv files on the reviews folder(Automatically created) 

g)	If app is run from webpage , it shows only the reviews .
