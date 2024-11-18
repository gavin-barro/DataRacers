"""Routes for race event views for race crew members"""

from app import app
import queries.views as db
from collections import Counter
from flask import render_template, request, flash, redirect


@app.route("/race_crew")
def race_crew():
    race_year = request.args.get("race_year")
    location = request.args.get("location")
    if race_year and location:
        data = db.racecrew_kitview(race_year, location)
        stats = Counter([row[1] for row in data])
    else:
        data = None
        stats = None
    return render_template("views/race_crew.jinja",
                           race_year=race_year, location=location, data=data, stats=stats)