#!/usr/bin/python
from flask import Flask, render_template, request, redirect, url_for
#import database

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("login.html")


if __name__ == "__main__":
    #app.debug=True
    #database.create()
    app.run()
