from app import app
from flask import render_template, request, flash, redirect

@app.route("/about")
def about_slide():
    picture_path = 'f1_logo.jpg'
    return render_template("about.jinja", image = picture_path)