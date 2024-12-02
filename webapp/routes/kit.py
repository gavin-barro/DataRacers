"""Routes for viewing/editing the Shipment table."""
from app import app
import queries.kit as db
from flask import render_template, request, flash, redirect

@app.route("/kit")
def show_kit_all():
    data = db.kit_all()
    return render_template("kit_all.jinja", data=data)


@app.route("/kit/<key>")
def kit_edit(key):
    print("key", key)
    # If the form was not submitted
    if not request.args:
        if key == "new":
            values = []
        else:
            values = db.kit_get(key)
        return render_template("kit_edit.jinja", key=key, values=values)

    # Perform the requested action
    values = list(request.args.values())
    action = values.pop()
    try:
        if action == "Insert":
            db.kit_ins(values)
            flash("Kit inserted")
        elif action == "Update":
            db.kit_upd(key, values)
            flash("Kit updated")
        elif action == "Delete":
            db.kit_del(key)
            flash("Kit deleted")
    except Exception as e:
        flash(str(e))
        return render_template("kit_edit.jinja", key=key, values=values)
    return redirect("/kit")