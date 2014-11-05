#!/usr/bin/python
import mongo
from flask import Flask, render_template, request, redirect, \
    url_for, session, flash


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        user = request.form["user"]
        password = request.form["password"]
        dict = {'user':user,'password':password}
        #error = None if no errors
        error = mongo.loginErrors(dict)

        if error:
            flash(error, "error")
        else:
            session['user'] = user
            flash("Sucessfully logged in")
            return redirect(url_for("animals"))
    return render_template("login.html")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        user = request.form["user"]
        password = request.form["password"]
        dict = {'user':user, 'password':password}
        #error = None if no errors
        error = mongo.registerErrors(dict)

        if error:
            flash(error, "error")
        else:
            mongo.addAccount(dict)
            flash("Successfully registered")
            return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/logout", methods=["GET","POST"])
def logout():
    if request.method == "GET":
        return render_template("logout.html")
    else:
        session.pop("user",None)
        return redirect(url_for("home"))

@app.route("/animals")
def animals():
    if session['user'] == None:
        flash("You need to be logged in to see that!")
        return redirect(url_for("login"))
    return render_template("animals.html")

@app.route("/otter")
def otter():
    if session['user'] == None:
        flash("You need to be logged in to see that!")
        return redirect(url_for("login"))
    return render_template("otter.html")

@app.route("/kitten")
def kitten():
    if session['user'] == None:
        flash("You need to be logged in to see that!")
        return redirect(url_for("login"))
    return render_template("kitten.html")


#======================END-DEFINITIONS======================


app.secret_key = '\x90\x9c\xe3C<\x12]^v0p\xde\xc7\xb2\xa1\xea\x90e\x10\xfe\xf1\xd0\xa7g'

if __name__ == "__main__":
    app.debug=True
    app.run()
