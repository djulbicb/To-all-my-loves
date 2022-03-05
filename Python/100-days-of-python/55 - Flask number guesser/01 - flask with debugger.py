from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1 style="text-align:center;">Hello world</h1>' \
           '<iframe src="https://giphy.com/embed/MDJ9IbxxvDUQM" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/cat-kisses-hugs-MDJ9IbxxvDUQM">via GIPHY</a></p>'

@app.route("/echo")
def bye():
    return "Echo"

# variable sections <variable_name>
@app.route("/username/<name>")
def name(name):
    return f"Hello {name + 10}"

if __name__ == "__main__":
    # app.run()
    app.run(debug=True)

# Enable debugger to hot reload files on file save, and enables debug mode of application
# U konzoli ce se pojaviti debug pin

# Mogu automatski da se konvertuju u neki tip. def je string
# <konverter:variable_name>
# int, float, path, uuid
# path username/<path:var> ce od username/angela/1 uzeti /angela/1

