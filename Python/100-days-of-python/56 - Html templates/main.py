# https://html5up.net/
# document.body.contentEditable=True

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<int:test>")
def test(test=""):
    return str(test)

if __name__ == "__main__":
    # app.run()
    app.run(debug=True)