# coding=utf-8
import uuid
import json

def create_uuid(type=1):
    if type == 0:
        s_uuid = str(uuid.uuid4())
    elif type == 1:
        s_uuid = str(uuid.uuid4())
        l_uuid = s_uuid.split('-')
        s_uuid = ''.join(l_uuid)
    return s_uuid

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        return json.JSONEncoder.default(self, obj)
