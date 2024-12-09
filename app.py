from flask import Flask, render_template
import env
import requests
import main

app = Flask(__name__)
app.template_folder = "./"


@app.route("/")
def run():

    CALENDAR = main.CALENDAR

    return render_template("index.html")
