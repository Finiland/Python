from flask import Flask, session, redirect, url_for, request, render_template, flash
import flask
from markupsafe import escape
from flask import send_from_directory
import os
import datetime


app = Flask(__name__)

app.secret_key = b'\xbeVn\x06g\xc1\xbc\xde,\xa5\x85I\xa9\xdd\x96P\x89\xfc\xf6y\xf6\x13D\xbc\xbepC'
app.permanent_session_lifetime = datetime.timedelta(days=5)
#kanko = session.get('log_in')

@app.route("/")
def home():
    if "user" in session:
        return navigointi()
    else:
        return render_template("login.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        pwd = request.form["pw"]
        session["user"] = user
        if pwd == "Gigantti" and user == "Kaleva":            
            #flash("Kirjauduit sisään onnistuneesti!")
            return navigointi()
    elif "user" in session:
        #flash("Olet jo kirjautunut!")
        #return redirect(url_for("user"))
        return navigointi()
    else:
        return render_template("login.html")
    

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user=user)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash("Kirjauduit ulos!", "info")

        session.pop("user", None)    
        return render_template("login.html")

@app.route("/about")
def myymalat():
    if "user" in session:
        user = session["user"]
        return render_template("myymalat.html")
    else:
        return render_template('login.html')
@app.route("/support")
def support():
    if "user" in session:
        user = session["user"]
        return render_template("support.html")
    else:
        return render_template('login.html')
@app.route("/navigointi")
def navigointi():
    if "user" in session:
        user = session["user"]
        return render_template("navigointi.html")
    else:
        return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)
