from flask import Flask , render_template, url_for , request, flash
import fsite


app.config['SECRET_KEY'] = "efepfspefneifneflfndsffs"

list_menu = [{"name":"Главная" , "url" : "/"},
              {"name":"О нас", "url": "/about"},
              {"name" : "Обратная связь", "url": "/contact"}]

@app.route("/")
def index():
    return render_template("index.html", title = "Про Flask", menu = list_menu)

@app.route("/about")
def about():
    return render_template("about.html" , title = "О нас" , menu = list_menu)

@app.route("/contact", methods = ["POST", "GET"])
def contact():
    if request.method == 'POST':
        if len(request.form["message"]) > 5:
            flash('Cобщение отправлено')
        else:
            flash('Ошибка отправки')
    return render_template("contact.html" , title = "Обратная связь" , menu = list_menu)

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html', title = "Страница не найдена", menu = list_menu)

if __name__ == "__main__":
    app.run(debug = True)

print(__name__)