from flask import Flask, render_template 
import requests 

app=Flask(__name__)

@app.route("/")
def index():
    url="https://newsapi.org/v2/top-headlines?country=in&apiKey=fb590af27774460a89461facd6313f2d"
    r=requests.get(url).json()

    cases={
        "articles": r["articles"]
    }

    return render_template("index.html", case=cases)



@app.route("/businessnews")
def businessnews():
    url="https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=fb590af27774460a89461facd6313f2d"
    r=requests.get(url).json()

    cases={
        "articles": r["articles"]
    }

    return render_template("businessnews.html", case=cases)

if __name__=="__main__":
    app.run(debug=True)