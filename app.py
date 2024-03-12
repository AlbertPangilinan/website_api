import csv_read
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return csv_read.get_all_projects()


@app.route("/projects")
def get_all_projects():
    return csv_read.get_all_projects()


@app.route("/project/<project_id>")
def get_project_by_id(project_id):
    return csv_read.get_project_by_id(int(project_id))
