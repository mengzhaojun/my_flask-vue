# run.py

'''
    render_template 是渲染模板用的，这里我们用来返回 index.html
    flask_cors 用来解决跨域的问题
'''



from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS
from datetime import datetime
import config
from flask_sqlalchemy import SQLAlchemy

# 通过 static_folder 指定静态资源路径，以便 index.html 能正确访问 CSS 等静态资源
# template_folder 指定模板路径，以便 render_template 能正确渲染 index.html
app = Flask(
    __name__, static_url_path='/', static_folder="./../flask-dist", template_folder="./../flask-dist")

CORS(app)
app.config.from_object(config)
db = SQLAlchemy(app)

class Project(db.Model):
    __tablename__ = 'project'
    id = db.Column(db.INT, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    region = db.Column(db.String(200), nullable=False)
    version = db.Column(db.String(50), nullable=False)
    project_create_time = db.Column(db.DateTime, default=datetime.now)

db.create_all()

@app.route("/")
def home():
    '''
        当在浏览器访问网址时，通过 render_template 方法渲染 dist 文件夹中的 index.html。
        页面之间的跳转交给前端路由负责，后端不用再写大量的路由
    '''
    return render_template('index.html')

@app.route('/test', methods=['GET', 'POST'])
def test():
    '''
    这个API用来测试跨域
    '''
    return 'success'

@app.route('/project_list', methods=['GET', 'POST'])
def project_list():
    res = {}
    res_data_list = []
    all_data = db.session.query(Project).all()
    for row in all_data:
        res_data = {}
        res_data['datetime'] = row.project_create_time
        res_data['name'] = row.name
        res_data['region'] = row.region
        res_data['version'] = row.version
        res_data_list.append(res_data)
    res['data'] = res_data_list
    return res

@app.route('/add_project', methods=['GET', 'POST'])
def add_project():
    project_name = request.form.get('name')
    region = request.form.get('region')
    version = request.form.get('version')
    print(project_name, region, version)
    add_data = Project(name=project_name, region=region, version=version)
    db.session.add(add_data)
    db.session.commit()
    return 'success..'


if __name__ == '__main__':
    # 开启 debug模式，这样我们就不用每更改一次文件，就重新启动一次服务
    # 设置 host='0.0.0.0'，让操作系统监听所有公网 IP
    # 也就是把自己的电脑作为服务器，可以让别人访问
    app.run(debug=True)
