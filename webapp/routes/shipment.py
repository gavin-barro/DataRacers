"""Routes for viewing/editing the Shipment table."""

from app import app
import queries.shipment as db
from flask import render_template, request, flash, redirect


@app.route("/shipment")
def show_shipment_all():
    data = db.shipment_all()
    return render_template("shipment_all.jinja", data=data)


@app.route("/shipment/<key>")
def shipment_edit(key):

    # If the form was not submitted
    if not request.args:
        if key == "new":
            values = []
        else:
            values = db.shipment_get(key)
        return render_template("shipment_edit.jinja", key=key, values=values)

    # Perform the requested action
    values = list(request.args.values())
    action = values.pop()
    try:
        if action == "Insert":
            db.shipment_ins(values)
            flash("Person inserted")
        elif action == "Update":
            db.shipment_upd(key, values)
            flash("Person updated")
        elif action == "Delete":
            db.person_del(key)
            flash("Person deleted")
    except Exception as e:
        flash(str(e))
        return render_template("shipment_edit.jinja", key=key, values=values)
    return redirect("/person")