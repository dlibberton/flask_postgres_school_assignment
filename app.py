from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://dal:root@localhost:5432/school"



db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    subject = db.Column(db.Integer)
    
class Subjects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(50))
    
class Teachers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    subject = db.Column(db.Integer)
    
    
    
@app.route('/api/v1/student/', methods=['GET'])
def get_students():
    try:
        students = Student.query.all()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        return (f"Unexpected {err=}, {type(err)=}")
    
    student_list = [
        {'id': student.id, 'first_name': student.first_name, 'last_name': student.last_name, 'age': student.age, 'subject': student.subject}
        for student in students]
    response = jsonify(student_list)
    return response

app.run(debug=True)
