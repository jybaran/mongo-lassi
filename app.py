#!/usr/bin/python
from flask import Flask, render_template, request, redirect, url_for
import mongo

app = Flask(__name__)

@app.route("/")
def main():
    return redirect(url_for("login"))

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        user = request.form["user"]
        password = request.form["password"]
        dict = {'user':user,'password':password}
        if mongo.isValidLogin(dict):
            # send user to home page
            ####
            return "WE MADE IT"
        else:
            # do something when login info is not valid
            ####
            return "Login failed"
            #return render_template("login.html")

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        user = request.form["user"]
        password = request.form["password"]
        dict = {'user':user, 'password':password}
        if mongo.isValidRegister(dict):
            mongo.addAccount(dict)
            # let user know he succesfully registered
            ####
            return redirect(url_for("login"))
        else:
            # do something when register info is not valid
            ####
            return "Username taken"
            #return render_template("register.html")


if __name__ == "__main__":
    app.debug=True
    app.run()
