from common.models import Project, User
from flask import Blueprint, request
from common.exts import db
from common.common import create_uuid

project = Blueprint('project', __name__)

@project.route('/projectList', methods=['GET', 'POST'])
def projectList():
    data = db.session.query(Project).all()
    all_data = []
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
    # return 'success'

@project.route('/addProject', methods=['GET', 'POST'])
def addProject():
    uuid = create_uuid()
    name = request.form.get('name')
    region = request.form.get('region')
    version = request.form.get('version')
    add_data = Project(uuid=uuid, project_name=name, project_region=region, project_version=version)
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


@project.route('/projectlist', methods=['GET', 'POST'])
def projectlist():
    project = db.session.query(Project).all()
    data =[]
    for p in project:
        res = {}
        res['value'] = p.uuid
        res['label'] = p.project_name
        data.append(res)
    res_data = {
        'static': 1,
        'message': 'success',
        'data': data
    }
    return res_data
