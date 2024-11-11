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
    # team_name = request.args.get("team_name")
    
    # data = db.race_team_shipment(team_name)
    # return render_template("views/race_team_shipment.jinja", data=data, team_name=team_name)

    team_name = request.args.get("team_name")
    print(f"Selected Team: {team_name}")
    if team_name:
        data = db.race_team_shipment(team_name)
        stats = Counter([row[4] for row in data])
    else:
        data = None
        stats = None
    return render_template("views/race_team_shipment.jinja", data=data, team_name=team_name, stats=stats)
