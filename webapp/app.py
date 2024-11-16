"""Web app for F1DB Workshop Management."""

from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "dev"  # required for flash()


@app.route("/")
def index():
    return render_template("index.jinja")

@app.route("/test")
def test():
    return render_template("test.jinja")

# Import all routes from other modules
import routes