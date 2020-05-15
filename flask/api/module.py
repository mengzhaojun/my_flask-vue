import json
from common.models import Project,Module
from flask import Blueprint, request
from common.exts import db
from common.common import MyEncoder
from common.common import create_uuid

module = Blueprint('module', __name__)

@module.route('/moduleList', methods=['GET', 'POST'])
# @module.route('/moduleList/<projectName>', methods=['GET', 'POST'])
def moduleList():
    all_data = []
    projectName = request.args.get('p_name')
    # print('p_name: ', projectName)
    if projectName:
        project = Project.query.filter(Project.project_name == projectName).first()
        data = project.modules
        for row in data:
            # print(row.project.project_name)
            res_data = {}
            res_data['name'] = row.module_name
            res_data['region'] = row.module_region
            res_data['datetime'] = row.module_create_time
            res_data['project_name'] = str(row.project.project_name)
            all_data.append(res_data)
        # print(all_data)
    else:
        data = db.session.query(Module).all()
        for row in data:
            # print(row.project.project_name)
            res_data = {}
            res_data['name'] = row.module_name
            res_data['region'] = row.module_region
            res_data['datetime'] = row.module_create_time
            res_data['project_name'] = str(row.project.project_name)
            all_data.append(res_data)
    res = {
        'static': 1,
        'message': 'success',
        'data': all_data
    }
    return res

