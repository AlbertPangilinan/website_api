import csv

projects = []

with open('projects.csv', newline='') as file:
    reader = csv.DictReader(file)
    i = 0
    for row in reader:
        row["id"] = i
        row["text"] = row["text"].split('|')
        row["tags"] = row["tags"].split('|')
        projects.append(row)
        i += 1


def get_all_projects():
    return projects


def get_project_by_id(project_id):
    return list(filter(lambda project: project['id'] == project_id, projects))[0]


def get_projects_by_tag(tag):
    print(tag.casefold())
    return list(filter(lambda project: tag.casefold() in [tag.casefold() for tag in project['tags']], projects))
