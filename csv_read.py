import csv

projects = []

with open('projects.csv', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        projects.append(row)

def get_projects():
    return projects
