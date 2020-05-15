# coding=utf-8
import uuid
from common.exts import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'
    uuid = db.Column(db.String(50), primary_key=True, nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)


class Project(db.Model):
    __tablename__ = 'project'
    uuid = db.Column(db.String(50), primary_key=True, nullable=False)
    # pid = db.Column(db.INT, primary_key=True, autoincrement=True)
    project_name = db.Column(db.String(50), nullable=False)
    project_region = db.Column(db.String(200), nullable=False)
    project_version = db.Column(db.String(50), nullable=False)
    project_create_time = db.Column(db.DateTime, default=datetime.now)


#
class Module(db.Model):
    __tablename__ = 'module'
    uuid = db.Column(db.String(50), primary_key=True, nullable=False)
    module_name = db.Column(db.String(50), nullable=False)
    module_region = db.Column(db.String(200), nullable=False)
    module_create_time = db.Column(db.DateTime, default=datetime.now)
    project_id = db.Column(db.String(50), db.ForeignKey('project.uuid'))

    project = db.relationship('Project', backref=db.backref('modules'))


class Case(db.Model):
    __tablename__ = 'case'
    uuid = db.Column(db.String(50), primary_key=True, nullable=False)
    case_id = db.Column(db.INT, autoincrement=True, nullable=False)
    case_name = db.Column(db.String(100), nullable=False)
    case_url = db.Column(db.String(100), nullable=False)
    case_type = db.Column(db.String(100), nullable=False)
    case_data = db.Column(db.Text, nullable=False)
    case_create_time = db.Column(db.DateTime, default=datetime.now)

    project_id = db.Column(db.String(50), db.ForeignKey('project.uuid'))
    module_id = db.Column(db.String(50), db.ForeignKey('module.uuid'))
