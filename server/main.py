from operator import itemgetter


from flask import Flask, render_template,request,url_for,jsonify, redirect,flash
from models import db,Student,Units,User
from flask_migrate import Migrate
from flask_restful import Api, reqparse, Resource
from flask_cors import CORS, cross_origin
from flask_login  import LoginManager, logout_user,login_user, current_user,login_required



app =Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///db.db'
app.config['SECRET_KEY']=b'\xb4\xbe\x0b\xd1x\x88\xdc\xaa\xe83\xa1\nZ\xbc]\xf0\x13\x83J\xd5@\xe0\xca'

app.config['CORS_HEADERS'] = 'Content-Type'
login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view='login'

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=int(user_id)).first()

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method=='POST':
        email = request.form['email']
        password = request.form['password']
        user =User.query.filter_by(email=email).first()
        if user.password == password:
            login_user(user)
        return redirect(url_for('index'))
        # return current_user.username

    else:
        return render_template('login.html')
    
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['POST','GET'])
def register():
    if request.method=='POST':
        
        # print(username,password,cnpassword)
        if request.form['cnpassword'] != request.form['password']:
            flash('Paswords do not match')
            return render_template('register.html')
        else:
           
            new_user= User()
            for key,value in request.form.items():
                if key == 'cnfpasword':
                    continue
                setattr(new_user,key,value)
            db.session.add(new_user)
            db.session.commit()
            print(request.form)
            return redirect(url_for('login'))



            print(request.form)
       
    else:
        return render_template('register.html')


@app.route('/', methods=['GET','POST'])
@login_required
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
        student = Student(**request.form)
        db.session.add(student)
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
@login_required
def apiindex():

    if request.method == 'GET':
        students = Student.query.all()
        students_dict= []
        for student in students:
            students_dict.append(student.to_dict(rules=('-course','-course')))   
        return jsonify(students_dict)
    
    if request.method == 'POST':
        # obj= request.form.items()
        print(request.json)
        new_student = Student(**request.json)
        db.session.add(new_student)
        db.session.commit()
        
        return jsonify(new_student.to_dict(rules=('-course','-course')))

@app.route('/api/<int:id>', methods=['GET','DELETE','PATCH'])
def api_by_id(id):

    if request.method == 'GET':
        student =Student.query.filter_by(id =id).first().to_dict(rules=('-course','-course'))
        
        return jsonify(student)
    
    if request.method == 'PATCH':
        student =Student.query.filter_by(id =id).first()
        for key,value in request.form.items():
            setattr(student,key,value)
        db.session.commit()
        return jsonify(student.to_dict(rules=('-course','-course')))
    
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
        return jsonify(student.to_dict(rules=('-course','-course'))),201
        


class StudentsByID(Resource):

    def get(self, id):
        student =Student.query.filter_by(id = id).first()
        return jsonify(student.to_dict(rules=('-course','-course')),200)

    def patch(self,id):
        student_details = student_update.parse_args()
        print(student_details)
        student =Student.query.filter_by(id = id).first()
        for key,value in student_details.items():
            if value is None:
                continue
            setattr(student,key,value)
        db.session.commit()
        return jsonify(student.to_dict(rules=('-course','-course')),201)
    
    def delete(self,id):
        student =Student.query.filter_by(id =id).first()
        db.session.delete(student)
        db.session.commit()
        return {"detail" : f"student with id {id} has een deleted successfully"}



api.add_resource(Students,'/Capi')
api.add_resource(StudentsByID,'/Capi/<int:id>')


if __name__ == '__main__':
    app.run(debug=1)