from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer

# DEBUG = True
# FLATPAGES_AUTO_RELOAD = DEBUG
# FLATPAGES_EXTENSION = ".md"

app = Flask(__name__)
app.config.from_pyfile('settings.py')
pages = FlatPages(app)
freezer = Freezer(app)
# app.config.from_object(__name__)
# pages = FlatPages(app)


@app.route("/")  # This is the main URL
def home():
    # The argument should be in templates folder
    return render_template("index.html", name="Home")


@app.route("/<page>")
def allpages(page):
    pages = ["about", "projects", "contact"]
    if page in pages:
        return render_template("%s.html" % page, name=page.title())
    else:
        return render_template("index.html", name="Home")


@app.errorhandler(404)
def pageNotFound(e):
    return render_template("404.html", name="404"), 404


if __name__ == '__main__':
    app.run(debug=True)  # debug=True is optional
