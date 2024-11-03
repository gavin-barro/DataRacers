"""Routes for viewing/editing the Race Events table."""

from app import app
import queries.raceevent as db
from flask import render_template, request, flash, redirect


@app.route("/raceevent")
def workshop_all():
    data = db.raceevent_all()
    return render_template("race_event_all.jinja", data=data)


@app.route("/raceevent/<key>")
def raceevent_edit(key):

    # If the form was not submitted
    if not request.args:
        if key == "new":
            values = []
        else:
            values = db.raceevent_get(key)
        return render_template("raceevent_edit.jinja", key=key, values=values)

    # Perform the requested action
    values = list(request.args.values())
    action = values.pop()
    try:
        if action == "Insert":
            db.raceevent_ins(values)
            flash("Race Event inserted")
        elif action == "Update":
            db.raceevent_upd(key, values)
            flash("Race Event updated")
        elif action == "Delete":
            db.raceevent_del(key)
            flash("Race Event deleted")
    except Exception as e:
        flash(str(e))
        return render_template("raceevent_edit.jinja", key=key, values=values)
    return redirect("/raceevent")