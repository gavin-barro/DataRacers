from app import app
import queries.kit as kit
import queries.raceevent as race
from flask import render_template, request, flash, redirect

@app.route("/team_manager")
def team_manager():
    if not request.args:
        print('no args')
        return render_template("team_manager.jinja",action= None, data=None)
    values = list(request.args.values())
    action = values.pop()
    if action == "View and Add Kits":
        return render_template("team_manager.jinja", action="kits")
    elif action == "View a teams kit and contents":
        return render_template("team_manager.jinja", action="tk")
