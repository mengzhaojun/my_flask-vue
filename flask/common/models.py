# coding=utf-8
import uuid
from common.exts import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'
    uid = db.Column(db.INT, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)


class Project(db.Model):
    __tablename__ = 'project'
    pid = db.Column(db.INT, primary_key=True, autoincrement=True)
    project_name = db.Column(db.String(50), nullable=False)
    project_region = db.Column(db.String(200), nullable=False)
    project_version = db.Column(db.String(50), nullable=False)
    project_create_time = db.Column(db.DateTime, default=datetime.now)


#
# class Module(db.Model):
#     __tablename__ = 'module'
#     mid = db.Column(db.INT, primary_key=True, autoincrement=True)
#     module_name = db.Column(db.String(50), nullable=False)
#     module_region = db.Column(db.String(200), nullable=False)
#     module_create_time = db.Column(db.DateTime, default=datetime.now)
#     author_id = db.Column(db.INT, db.ForeignKey('project.author_id'))
#     project_id = db.Column(db.INT, db.ForeignKey('project.pid'))
#
#     author = db.relationship('User', backref=db.backref('modules'))
#     project = db.relationship('User', backref=db.backref('modules'))
