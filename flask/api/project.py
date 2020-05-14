from common.models import Project, User
from flask import Blueprint, request
from common.exts import db

project = Blueprint('project', __name__)

@project.route('/projectList', methods=['GET', 'POST'])
def projectList():
    # data = Project.query().all()
    print('-----')
    data = db.session.query(Project).all()
    all_data = []
    print(data)
    for row in data:
        res_data = {}
        res_data['name'] = row.project_name
        res_data['region'] = row.project_region
        res_data['version'] = row.project_version
        res_data['datetime'] = row.project_create_time
        all_data.append(res_data)
    res = {
        'static': 1,
        'message': 'success',
        'data': all_data
    }
    return res


@project.route('/addProject', methods=['GET', 'POST'])
def addProject():
    project_name = request.form.get('name')
    region = request.form.get('region')
    version = request.form.get('version')
    # user_id = 1
    # print(project_name, region, version)
    add_data = Project(project_name=project_name, project_region=region, project_version=version)
    db.session.add(add_data)
    db.session.commit()
    data = {
        'static': '1',
        'message': 'success'
    }
    return data


@project.route('deleteProject', methods=['GET', 'POST'])
def deleteProject(id):
    return id
