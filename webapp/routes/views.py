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

@app.route("/race_team_shipment_status")
def race_team_shipment_status() -> str:
    status = request.args.get("status") 
    print(f"Query string: {request.args}")
    print(f"Selected Status: {status}")
    
    if status:
        data = db.race_team_shipment_status(status) 
        stats = Counter([row[3] for row in data]) 
    else:
        data = None
        stats = None
    
    return render_template("views/race_team_shipment_status.jinja", data=data, status=status, stats=stats)


@app.route('/select_team_kits')
def get_team_kits():
    team_id = request.args.get("team_id")
    stats = {}
    if team_id:
        data = db.get_team_kits(team_id)
        stats = Counter([row[2] for row in data])
    else:
        data = None
        stats = None
        
    return render_template("views/team_kits.jinja",data=data, stats=stats, team_id = team_id)


@app.route('/overweight_kits')
def get_overweight_kits():
    weight = request.args.get("weight")
    print(f"weight {weight}")
    
    if weight:
        data = db.get_overweight_kits(12)
        print(data)
    else:
        data = None
 
    return render_template("views/overweight_kits.jinja",data=data)
