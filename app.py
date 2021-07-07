import os
from csv import DictWriter
from urllib.request import urlopen as uReq
import requests
from bs4 import BeautifulSoup as bs
from flask import Flask, render_template, request
from flask_cors import cross_origin

app = Flask(__name__)

@app.route('/',methods=['GET'])
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/review',methods=['POST','GET'])
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            searchString = request.form['content'].replace(" ","")
            flipkart_url = "https://www.flipkart.com/search?q=" + searchString
            uClient = uReq(flipkart_url)
            flipkartPage = uClient.read()
            uClient.close()
            flipkart_html = bs(flipkartPage, "html.parser")
            bigboxes = flipkart_html.findAll("div", {"class": "_1AtVbE col-12-12"})
            del bigboxes[0:3]
            box = bigboxes[0]
            productLink = "https://www.flipkart.com" + box.div.div.div.a['href']
            prodRes = requests.get(productLink)
            prodRes.encoding='utf-8'
            prod_html = bs(prodRes.text, "html.parser")
            commentboxes = prod_html.find_all('div', {'class': "_16PBlm"})

            target_folder = os.path.join('./reviews')

            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            filename = searchString + ".csv"
            f = open(os.path.join(target_folder, filename), 'w')
            headers = "Product,Name,Rating,CommentHead,Comment"
            f.write(headers)

            reviews = []
            for commentbox in commentboxes:
                try:

                    name = commentbox.div.div.find_all('p', {'class': '_2sc7ZR _2V5EHH'})[0].text
                    name.encode(encoding='utf-8')

                except:
                    name = 'No Name'

                try:

                    rating = commentbox.div.div.div.div.text
                    rating.encode(encoding='utf-8')


                except:
                    rating = 'No Rating'

                try:

                    commentHead = commentbox.div.div.div.p.text
                    commentHead.encode(encoding='utf-8')

                except:
                    commentHead = 'No Comment Heading'
                try:
                    comtag = commentbox.div.div.find_all('div', {'class': ''})
                    custComment = comtag[0].div.text
                    custComment.encode(encoding='utf-8')
                except :
                    custComment="No Comment"

                mydict = {"Product": searchString, "Name": name, "Rating": rating, "CommentHead": commentHead,
                          "Comment": custComment}
                reviews.append(mydict)

                with open(os.path.join(target_folder, filename), 'a',encoding='utf-8') as f:
                    dictwriter_object = DictWriter(f, fieldnames=list(headers.split(",")))
                    dictwriter_object.writerow(mydict)
                    f.close()

            return render_template('results.html', reviews=reviews[0:(len(reviews)-1)])
        except Exception as e:
            print(e)
            return print(e)

    else:
        return  render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)