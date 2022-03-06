# Jinja is build into Flask
# Used for html templating
# <h1<{{5 * 6}}</h1> = 60    # ovo je template
# <h1>5 + 6</h1>             # ovo nije template

# Passing values from app to html

from flask import Flask, render_template
import random
import datetime as dt

app = Flask(__name__)

@app.route("/")
def index() :
    current_year = dt.datetime.now().year
    number = random.randint(1,10)
    return render_template("index.html", year=current_year, num=number)

import requests
@app.route("/guess/<string:name>")
def guess(name:str):
    _name = name

    response = requests.get(f"https://api.agify.io/?name={name}").json()
    _age = response['age']

    respose = requests.get(f"https://api.genderize.io?name={name}").json()
    _gender = respose['gender']
    return render_template("guesse.html", name=_name, age=_age, gender=_gender)

if __name__ == "__main__":
    # app.run()
    app.run(debug=True)