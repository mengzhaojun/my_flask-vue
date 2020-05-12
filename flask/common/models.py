# coding=utf-8

from common.exts import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)



class Project(db.Model):
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    project_name = db.Column(db.String(50), nullable=False)
    project_client = db.Column(db.String(50), nullable=False)
    project_version = db.Column(db.String(50), nullable=False)
    project_create_time = db.Column(db.DateTime, default=datetime.now)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    author = db.relationship('User', backref=db.backref('projects'))


class Module(db.Model):
    __tablename__ = 'module'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    module_name = db.Column(db.String(50), nullable=False)
    module_create_time = db.Column(db.DateTime, default=datetime.now)
    # author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    user_name = db.Column(db.String(50), nullable=False)

    # author = db.relationship('User', backref=db.backref('projects'))
    project = db.relationship('Project', backref=db.backref('modules'))



class Case(db.Model):
    __tablename__ = 'case'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    case_name = db.Column(db.String(50), nullable=False)
    case_url = db.Column(db.String(100), nullable=False)
    case_req_type = db.Column(db.String(50), nullable=False)
    case_req_data = db.Column(db.Text, nullable=False)
    case_data_type = db.Column(db.String(20), nullable=False)
    project_name = db.Column(db.String(50), nullable=False)
    author_name = db.Column(db.String(50), nullable=False)
    # authors_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # projects_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    module_id = db.Column(db.Integer, db.ForeignKey('module.id'))
    user_name = db.Column(db.String(50),nullable=False)

    # authors = db.relationship('User', backref=db.backref('projects'))
    # projects = db.relationship('Project', backref=db.backref('modules'))
    module = db.relationship('Module', backref=db.backref('cases'))