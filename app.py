import os
import sqlite3

from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask import *
# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = sqlite3.connect("registration.db",check_same_thread=False)
cursor = db.cursor()
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # TODO: Add the user's entry into the database
        name = request.form.get("name")
        email = request.form.get("email")
        number = request.form.get("number")
        comment = request.form['comment']
        cursor.execute("INSERT into sports(name,email,age,comment) VALUES(?,?,?,?)", (name,email,number,comment))
        db.commit()

        return render_template("index.html")

    else:

        # TODO: Display the entries in the database on index.html
        return render_template("index.html")

