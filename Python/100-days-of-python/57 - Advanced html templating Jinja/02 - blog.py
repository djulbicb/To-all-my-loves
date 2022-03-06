# Api for JSON DATA
# https://www.npoint.io/
NPOINT_URL = "https://api.npoint.io/260635fdcb7ca0a44f00"

from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    blogs = requests.get(NPOINT_URL).json()
    print(blogs)
    return render_template("blog.html", blogs=blogs)

@app.route("/<int:num>")
def test(num:int):
    return str(num)


if __name__ == "__main__":
    app.run(debug=True)

