from flask import Flask, render_template,request,url_for,jsonify, redirect
from models import db,Student,Units
from flask_migrate import Migrate
from flask_restful import Api, reqparse, Resource



app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///db.db'

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)


@app.route('/', methods=['GET','POST'])
def index():
    students = Student.query.all()
    if request.method == 'GET':
        return render_template('index.html', students=students)
    if request.method == 'POST':
        new_student = Student(**request.form)
        db.session.add(new_student)
        db.session.commit()
        return render_template('index.html',students=students)


@app.route('/student/<int:id>', methods=['GET','POST'])
def student_by_id(id):
    student =Student.query.filter_by(id =id).first()
    if request.method == 'GET':
        unitsdone = Units.query.filter_by(student_id=id).all()
        return render_template("single.html", student=student,unitsdone=unitsdone)
    if request.method == 'POST':
        for key, value in request.form.items():
            setattr(student, key, value)
        db.session.commit()
        return render_template("single.html", student=student)

@app.route('/delete/<int:id>')
def delete_student(id):
        student =Student.query.filter_by(id =id).first()
        if student:
            db.session.delete(student)
            db.session.commit()
            return redirect( url_for('index'))

@app.route('/api', methods=['GET','POST'])
def apiindex():

    if request.method == 'GET':
        students = Student.query.all()
        students_dict= []
        for student in students:
            students_dict.append(student.to_dict())   
        return jsonify(students_dict)
    
    if request.method == 'POST':
        new_student = Student(**request.form)
        db.session.add(new_student)
        db.session.commit()
        
        return jsonify(new_student.to_dict())

@app.route('/api/<int:id>', methods=['GET','DELETE','PATCH'])
def api_by_id(id):

    if request.method == 'GET':
        student =Student.query.filter_by(id =id).first().to_dict()
        return jsonify(student)
    
    if request.method == 'PATCH':
        student =Student.query.filter_by(id =id).first()
        for key,value in request.form.items():
            setattr(student,key,value)
        db.session.commit()
        return jsonify(student.to_dict())
    
    if request.method == 'DELETE':
        student =Student.query.filter_by(id =id).first()
        db.session.delete(student)
        db.session.commit()
        return {"msg" :f"Student with id {id} has been deleted successfully"}


student_data = reqparse.RequestParser()
student_data.add_argument('firstname', type=str,help="firstname must be included", required=True)
student_data.add_argument('lastname', type=str,help="lastname must be included", required=True)
student_data.add_argument('gender', type=str,help="gender must be included", required=True)
student_data.add_argument('email', type=str,help="email must be included", required=True)
student_data.add_argument('feebalance', type=int,help="feebalance must be included", required=True)


student_update = reqparse.RequestParser()
student_update.add_argument('firstname', type=str,help="firstname must be included")
student_update.add_argument('lastname', type=str,help="lastname must be included")
student_update.add_argument('gender', type=str,help="gender must be included")
student_update.add_argument('email', type=str,help="email must be included")
student_update.add_argument('feebalance', type=int,help="feebalance must be included")


class Students(Resource):

    def get(self):
        students = Student.query.all()
        students_dict= []
        for student in students:
            student ={
                "id":student.id,
                "firstname":student.firstname,
                "lastname":student.lastname,
                "email":student.email,
               "gender":student.gender,
                "feebalance":student.feebalance
            }
            students_dict.append(student)   
        return jsonify(students_dict),200
    
    def post(self):
        student_details = student_data.parse_args()
        student = Student(**student_details)
        db.session.add(student)
        db.session.commit()
        return jsonify(student.to_dict()),201
        


class StudentsByID(Resource):

    def patch(self,id):
        student_details = student_update.parse_args()
        student =Student.query.filter_by(id = id).first()
        for key,value in student_details.items():
            if value is None:
                continue
            setattr(student,key,value)
        db.session.commit()
        return jsonify(student.to_dict())
    
    def delete(self,id):
        student =Student.query.filter_by(id =id).first()
        db.session.delete(student)
        db.session.commit()
        return {"detail" : f"student with id {id} has een deleted successfully"}



api.add_resource(Students,'/Capi')
api.add_resource(StudentsByID,'/Capi/<int:id>')


if __name__ == '__main__':
    app.run(debug=1)