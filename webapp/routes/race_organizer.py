from app import app
import queries.shipment as ship
import queries.raceevent as race
from flask import render_template, request, flash, redirect

@app.route("/raceorganizer")
def race_organizer():
    if not request.args:
        print('no args')
        return render_template("raceorganizer.jinja",action= None, data=None)

    values = list(request.args.values())
    action = values.pop()
    print(action)
    if action == "View and Add Races":
        action_send = "races"
        data = race.raceevent_all()
    elif action == "View and Add Shipments":
        action_send = "shipments"
        data = ship.shipment_all()
    print(action)
    print(data)
    return render_template("raceorganizer.jinja", action=action_send, data=data)