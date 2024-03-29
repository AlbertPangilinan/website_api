import csv_read
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000/", "http://localhost:3000"])

@app.route("/")
def home():
    return csv_read.get_all_projects()


@app.route("/projects")
def get_all_projects():
    return csv_read.get_all_projects()


@app.route("/project/<project_id>")
def get_project_by_id(project_id):
    return csv_read.get_project_by_id(int(project_id))


@app.route("/projects/<tag>")
def get_projects_by_tag(tag):
    return csv_read.get_projects_by_tag(tag)
