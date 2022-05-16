from flask import Flask, redirect, render_template,request
import requests, re

app = Flask(__name__)

def url():
    URL="https://emojihub.herokuapp.com/api/random"
    html=requests.get(url=URL)
    data=html.json()
    return data



@app.route('/', methods=['GET','POST'])
def index():
    htmlcode=""
    if request.method == "GET":
        htmlcode=generate()
    return render_template('random.html',htmlcode=htmlcode)



@app.route('/random', methods=['GET','POST'])
def generate():
    data=url()
    value=data["htmlCode"]
    return (value[0])



@app.route("/search/", methods=['GET',"POST"])
def search():
    if request.method == 'POST':
        value=find(request.form["search"])
        return render_template('search.html',data=value)
    else:
        value=find("")
        return render_template("search.html",data=value)

def find(search_word):
    URL="https://emojihub.herokuapp.com/api/all"
    html=requests.get(url=URL)
    data=html.json()
    value=[]
    for element in data:
        if(re.search(search_word,element["name"])):
            value.append([element["name"],element["htmlCode"][0]])
    return value


@app.route('/results/', methods=['GET','POST'])
def results():
    value=find(request.form["search"])
    return render_template("search.html",data=value)


if __name__ =="__main__":
    app.run(debug=True)