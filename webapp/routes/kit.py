"""Routes for viewing/editing the Shipment table."""
from app import app
import queries.kit as db
from flask import render_template, request, flash, redirect

@app.route("/kit")
def show_kit_all():
    data = db.shipment_all()
    return render_template("kit_all.jinja", data=data)