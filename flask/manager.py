# coding=utf-8
from flask_script import Manager
from flask_migrate import MigrateCommand, Migrate
# from api_01 import app
from flask import app
from common.exts import db
from common.models import User, Project, Module, Case

manager = Manager(app)

# 使用Migrate绑定app和db
migrate = Migrate(app, db)

#添加迁移脚本的命令到manager中
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
