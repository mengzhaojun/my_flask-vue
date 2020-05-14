# coding=utf-8

"""Django's command-line utility for administrative tasks."""
from flask_script import Manager
from flask_migrate import MigrateCommand, Migrate
from run import app
from common.exts import db
from common.models import User, Project


# 让python支持命令行工作
manager = Manager(app)

# 使用migrate绑定app和db
migrate = Migrate(app, db)

# 添加迁移脚本的命令到manager中
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
