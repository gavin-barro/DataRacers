"""Routes for viewing/editing the Container table."""

from app import app
import queries.container as db 
from flask import render_template, request, flash, redirect


@app.route("/container")
def container_all():
    data = db.container_all()
    return render_template("container_all.jinja", data=data)


@app.route("/container/<key>")
def container_edit(key):
    # If the form was not submitted
    if not request.args:
        if key == "new":
            values = []
        else:
            values = db.container_get(key) 
        return render_template("container_edit.jinja", key=key, values=values)
    values = list(request.args.values())
    action = values.pop() 
    try:
        if action == "Insert":
            db.container_ins(values)
            flash("Container inserted")
        elif action == "Update":
            db.container_upd(key, values)
            flash("Container updated")
        elif action == "Delete":
            db.container_del(key)
            flash("Container deleted")
    except Exception as e:
        flash(str(e))
        return render_template("container_edit.jinja", key=key, values=values)
    return redirect("/container")
