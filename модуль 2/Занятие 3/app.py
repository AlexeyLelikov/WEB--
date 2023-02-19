from flask import Flask , render_template

app = Flask(__name__)

list_menu = [ "/about" , "/person" , "/home"]

@app.route("/")
def index():
    return render_template("index.html", title = "Про Flask", menu = list_menu)

@app.route("/about")
def about():
    return render_template("about.html" , title = "О нас")


if __name__ == "__main__":
    app.run(debug = True)