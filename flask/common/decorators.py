# coding = utf-8
from functools import wraps
from flask import redirect, url_for, session


# 登录限制
def login_require(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('user_id'):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrapper
