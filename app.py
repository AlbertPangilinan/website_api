import csv_read

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return csv_read.get_all_projects()

@app.route("/projects")
def projects():
    return csv_read.get_all_projects()