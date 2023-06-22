from flask import Flask, render_template,request,url_for,jsonify, redirect
from models import db,Student,Units
from flask_migrate import Migrate


app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///db.db'

migrate = Migrate(app, db)

db.init_app(app)


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



if __name__ == '__main__':
    app.run(debug=1)