import requests
import json

URL = "http://127.0.0.1:8000/api/api_article/"
py_dict = {'title': 'article13', 'author':'mammad', 'email':'mammad12@gmail.com'}

def post_data():
    # json_data = json.dumps(py_dict)
    # print(json_data)
    r = requests.post(url=URL, data=py_dict)
    data = r.json()
    print(data)

# post_data()
def get(id=None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    print(json_data)
    r = requests.get(url=URL, params=json_data)
    data = r.json()
    print(data)

get()