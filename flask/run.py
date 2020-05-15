import config
import uuid
from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from common.models import User
from api.project import project
from api.module import module
from common.common import create_uuid

# 通过 static_folder 指定静态资源路径，以便 index.html 能正确访问 CSS 等静态资源
# template_folder 指定模板路径，以便 render_template 能正确渲染 index.html
app = Flask(
    __name__,
    static_url_path='/',
    static_folder="./../flask-dist",
    template_folder="./../flask-dist",
    )

app.register_blueprint(project, url_prefix="/")
app.register_blueprint(module, url_prefix="/")


CORS(app)
app.config.from_object(config)
db = SQLAlchemy(app)
db.init_app(app)



@app.route("/")
def home():
    '''
        当在浏览器访问网址时，通过 render_template 方法渲染 dist 文件夹中的 index.html。
        页面之间的跳转交给前端路由负责，后端不用再写大量的路由
    '''
    return render_template('index.html')

@app.route('/test', methods=['GET', 'POST'])
def test():
    uuid = create_uuid()
    user_data = User(uuid=uuid, username='mengzhaojun', password='123456')
    db.session.add(user_data)
    db.session.commit()
    return uuid


if __name__ == '__main__':
    # 开启 debug模式，这样我们就不用每更改一次文件，就重新启动一次服务
    # 设置 host='0.0.0.0'，让操作系统监听所有公网 IP
    # 也就是把自己的电脑作为服务器，可以让别人访问
    app.run(debug=True)
