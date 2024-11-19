from app import app
from flask import render_template

@app.route("/contact")
def contact() -> str:
    return render_template("contact.jinja") 