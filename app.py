#!/usr/bin/python
from flask import Flask, render_template, request, redirect, url_for, session
import mongo

app = Flask(__name__)

#note: session stuff is setup but not being used right now
# use it to let user know whether or not they are logged in (top right corner)

@app.route("/")
def main():
    return render_template("home.html")

    #if 'user' in session:
    #    return "home page for users already logged in"
    #else:
    #    return redirect(url_for("login"))

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
            session['user'] = user
            #return redirect(url_for("logout"))
            return render_template("logout.html")
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

@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("login"))


#======================END-DEFINITIONS======================


app.secret_key = '\x90\x9c\xe3C<\x12]^v0p\xde\xc7\xb2\xa1\xea\x90e\x10\xfe\xf1\xd0\xa7g'

if __name__ == "__main__":
    app.debug=True
    app.run()
