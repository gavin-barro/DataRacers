"""Routes for database views."""

from app import app
import queries.views as db
from collections import Counter
from flask import render_template, request, flash, redirect


@app.route("/critical_dates")
def critical_dates():
    race_year = request.args.get("race_year")
    if race_year:
        data = db.critical_dates(race_year)
        stats = Counter([row[1] for row in data])
    else:
        data = None
        stats = None
    return render_template("views/critical_dates.jinja",
                           race_year=race_year, data=data, stats=stats)

@app.route("/race_team_shipment")
def race_team_shipment():
    # TODO implement function stub
    data = db.race_team_shipment()
    return render_template("views/race_team_shipment.jinja", data=data)

@app.route("/select_team_kits")
def get_team_kits():
    data = db.get_team_kits()
    return render_template("views/team_kits.jinja")