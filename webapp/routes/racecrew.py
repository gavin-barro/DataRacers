"""Routes for race event views for race crew members"""

from app import app
import queries.views as db
from collections import Counter
from flask import render_template, request, flash, redirect

locations_by_year = {
    '2024': ['Bahrain Grand Prix', 'Saudi Arabian Grand Prix', 'Australian Grand Prix', 'Japanese Grand Prix', 'Chinese Grand Prix', 'Miami Grand Prix', 
             'Emilia Romagna Grand Prix', 'Monaco Grand Prix', 'Canadian Grand Prix', 'Spanish Grand Prix', 'Austrian Grand Prix', 'British Grand Prix', 
             'Hungarian Grand Prix', 'Belgian Grand Prix', 'Dutch Grand Prix', 'Italian Grand Prix', 'Azerbaijan Grand Prix', 'Singapore Grand Prix', 
             'United States Grand Prix', 'Mexico City Grand Prix', 'São Paulo Grand Prix', 'Las Vegas Grand Prix', 'Qatar Grand Prix', 'Abu Dhabi Grand Prix'],

    '2023': ['Bahrain Grand Prix', 'Saudi Arabian Grand Prix', 'Australian Grand Prix', 'Japanese Grand Prix', 'Miami Grand Prix', 
             'Monaco Grand Prix', 'Canadian Grand Prix', 'Spanish Grand Prix', 'Austrian Grand Prix', 'British Grand Prix', 
             'Hungarian Grand Prix', 'Belgian Grand Prix', 'Dutch Grand Prix', 'Italian Grand Prix', 'Azerbaijan Grand Prix', 'Singapore Grand Prix', 
             'United States Grand Prix', 'Mexico City Grand Prix', 'São Paulo Grand Prix', 'Las Vegas Grand Prix', 'Qatar Grand Prix', 'Abu Dhabi Grand Prix'],
}

@app.route("/race_crew", methods=["GET", "POST"])
def race_crew():
    race_year = request.form.get("race_year") or request.args.get("race_year")
    location = request.form.get("location") or request.args.get("location")

    locations = locations_by_year.get(race_year, []) if race_year else []

    if race_year and location:
        data = db.racecrew_kitview(race_year, location)
        stats = Counter([row[1] for row in data]) if data else None
    else:
        data = None
        stats = None

    return render_template(
        "views/race_crew.jinja",
        race_year=race_year,
        location=location,
        locations=locations,
        data=data,
        stats=stats
    )