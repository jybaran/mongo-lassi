#!/usr/bin/python
import mongo
from flask import Flask, render_template, request, redirect, session, flash, url_for

# the second kitten image link is broken :(

app = Flask(__name__)

def requireLogin(page):
    if 'user' not in session:
        flash("You need to be logged in to see that!")
        return redirect("login")
    else:
        return render_template("%s.html"%page)

@app.route("/home")
@app.route("/")
def home():
    if 'user' in session:
        return redirect("animals")
    return render_template("home.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if 'user' in session:
        flash("Already logged in!", "error")
        return redirect("animals")
    
    # Logging in
    if request.method == "POST":
        user = request.form["user"]
        password = request.form["password"]
        error = mongo.loginErrors(user, password)
        if error:
            flash(error, "error")
            return render_template("login.html")
        else:
            session['user'] = user
            return redirect("animals")
    else:
        return render_template("login.html")

@app.route("/register", methods=["GET","POST"])
def register():
    if 'user' in session:
        flash("Already logged in!", "error")
        return redirect("animals")

    # Registering
    if request.method == "POST":
        user = request.form["user"]
        password = request.form["password"]
        error = mongo.registerErrors(user,password)
        if error:
            flash(error, "error")
            return render_template("register.html")
        else:
            mongo.addAccount(user,password)
            flash("Successfully registered")
            return redirect("login")
    else:
        return render_template("register.html")

@app.route("/logout", methods=["GET","POST"])
def logout():
    if request.method == "POST":
        session.pop("user",None)
        return redirect("/")
    else:
        return render_template("logout.html")

@app.route("/animals")
def animals():
    return requireLogin("animals")

@app.route("/otter")
def otter():
    return requireLogin("otter")

@app.route("/kitten", methods=["GET","POST"])
def kitten():
    return requireLogin("kitten")


#======================END-DEFINITIONS======================


#should not be on github
app.secret_key = '\x90\x9c\xe3C<\x12]^v0p\xde\xc7\xb2\xa1\xea\x90e\x10\xfe\xf1\xd0\xa7g'

if __name__ == "__main__":
    app.debug=True
    app.run(host="0.0.0.0")
