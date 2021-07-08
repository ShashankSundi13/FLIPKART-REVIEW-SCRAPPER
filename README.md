# FLIPKART-REVIEW-SCRAPPER
Customer review scrapper for Flipkart products

## Explanation of what code does 
### a)	The application internally opens the Flipkart page and searches for the product and parses the webpage in html format .

### b)	Once we have the entire HTML page, we try to get the product URL and then jump to the product page. 

### c)	On the product page, we find which HTML section contains the customer comments. We do it by inspecting elements on the page from the element-wise view of the HTML page. 

### d)	Once we have the list of all the comments, we extract the customer name ,the rating ,comment heading and the customer comment from the tags. 

### e)	After that, we’ll return the ‘results.html’ page as the response to the user containing all the reviews. 

### f)	If we run the app from our local system the the scraped reviews are stored as csv files on the reviews folder(Automatically created) 

### g)	If app is run from webpage , it shows only the reviews .
