from flask import Flask, session, redirect, url_for, request, render_template, flash
import flask
from markupsafe import escape
from flask import send_from_directory
import os
import datetime


app = Flask(__name__)

app.secret_key = b'\xbeVn\x06g\xc1\xbc\xde,\xa5\x85I\xa9\xdd\x96P\x89\xfc\xf6y\xf6\x13D\xbc\xbepC'
app.permanent_session_lifetime = datetime.timedelta(days=5)

@app.route("/")
def home():
    return render_template("mainpage.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        flash("You are logged in succesfully!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already logged in!")
            return redirect(url_for("user"))
        return render_template("login2.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user=user)
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash("You have been logged out!", "info")
    session.pop("user", None)    
    return redirect(url_for("login"))

@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin!"))

if __name__ == "__main__":
    app.run(debug=True)