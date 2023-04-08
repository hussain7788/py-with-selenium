from flask import Flask, render_template, request, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = 'hussain'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.sqlite3'

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)

    def __repr__(self) -> str:
        return self.name
    
@app.route('/', methods=['GET'])
def index():
    return f"This is index page"

@app.route('/students', methods=['GET'])
def get_all_students():
    res = Student.query.all()

    output = []
    for data in res:
        d1 = {}
        d1['id'] = data.id
        d1['name'] = data.name
        d1['age'] = data.age
        output.append(d1) 

    return jsonify({"data": output})

@app.route('/student/<int:pk>', methods=['GET'])
def get_student(pk):
    try:
        res = Student.query.get(pk)
    except:
        return jsonify({"message":"No Record Found"})
    else:
        output = {}
        output['id'] = res.id
        output['name'] = res.name
        output['age'] = res.age

        return jsonify({"data": output})


@app.route('/create', methods=['POST'])
def create_student():
    data = request.get_json()
    stu = Student(name= data['name'], age= data['age'])

    db.session.add(stu)
    db.session.commit()
    return jsonify({"message":"Student is Created"})

@app.route('/update/<int:pk>', methods=['PUT'])
def update_student(pk):
    data = request.get_json()
    try:
        res = Student.query.get(pk)
    except:
        return jsonify({"message":"No Record Found"})
    else:
        res.name = data['name']
        res.age = data['age']
        db.session.commit()
        return jsonify({"message": "Student Updated."})

@app.route('/delete/<int:pk>', methods=['DELETE'])
def delete_student(pk):
    try:
        res = Student.query.get(pk)
    except:
        return jsonify({"message":"No Record Found"})
    else:
        db.session.delete(res)
        db.session.commit()
        return jsonify({"message":"Student is Deleted."})

if __name__ == '__main__':
    app.run(debug=True)

