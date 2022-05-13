from flask import Flask, redirect, render_template,request
import requests, re

app = Flask(__name__)
count=0

@app.route('/')

def index():
    htmlcode=""
    if request.method == "GET":
        htmlcode=generate()
    return render_template('random.html',htmlcode=htmlcode)


def generate():
    URL="https://emojihub.herokuapp.com/api/random"
    html=requests.get(url=URL)
    data=html.json()
    value=data["htmlCode"]
    return (value[0])

@app.route("/search/", methods=['GET',"POST"])
def search():
    if request.method == 'POST':
        URL="https://emojihub.herokuapp.com/api/all"
        html=requests.get(url=URL)
        data=html.json()
        value=[]
        search_word=request.form["search"]
        for element in data:
            if(re.search(search_word,element["name"])):
                value.append(element["htmlCode"][0])
        return render_template('search.html',data=value)
    else:
        return render_template("search.html")



if __name__ =="__main__":
    app.run(debug=True)