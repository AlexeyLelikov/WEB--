from flask import Flask , render_template, url_for

app = Flask(__name__)

list_menu = [{"name":"Главная" , "url" : "/"},
              {"name":"О нас", "url": "/about"},
              {"name" : "Обратная связь", "url": "/"}]

@app.route("/")
def index():
    return render_template("index.html", title = "Про Flask", menu = list_menu)

@app.route("/about")
def about():
    return render_template("about.html" , title = "О нас" , menu = list_menu)


if __name__ == "__main__":
    app.run(debug = True)