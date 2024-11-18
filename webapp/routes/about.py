from app import app
from flask import render_template, request, flash, redirect

@app.route("/about")
def about_slide():
    return render_template("about.jinja")