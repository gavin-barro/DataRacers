from app import app
import queries.kit as kit
import queries.raceevent as race
from flask import render_template, request, flash, redirect

@app.route("/team_manager")
def race_organizer():
    if not request.args:
        print('no args')
        return render_template("team_manager.jinja",action= None, data=None)
    '''
    values = list(request.args.values())
    action = values.pop()
    print(action)
    if action == "View and Add Races":
        action_send = "races"
        data = race.raceevent_all()
    elif action == "View and Add Shipments":
        action_send = "shipments"
        data = ship.shipment_all()
        # Title casing the data
        data  = [
            tuple(item.title() if isinstance(item, str) else item for item in row)
            for row in data
        ]
    print(action)
    print(data)
    return render_template("raceorganizer.jinja", action=action_send, data=data)
    '''