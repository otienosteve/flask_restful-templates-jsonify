from main import app
from models import Student, Units,db


sample_students= [{
  "id": 1,
  "firstname": "Roarke",
  "lastname": "Nance",
  "email": "rnance0@google.nl",
  "gender": "Male",
  "feebalance": 36797
}, {
  "id": 2,
  "firstname": "Chelsey",
  "lastname": "Gerssam",
  "email": "cgerssam1@dyndns.org",
  "gender": "Female",
  "feebalance": 10498
}, {
  "id": 3,
  "firstname": "Yule",
  "lastname": "Smallacombe",
  "email": "ysmallacombe2@issuu.com",
  "gender": "Male",
  "feebalance": 9896
}, {
  "id": 4,
  "firstname": "Prince",
  "lastname": "Standon",
  "email": "pstandon3@blogs.com",
  "gender": "Male",
  "feebalance": 28005
}, {
  "id": 5,
  "firstname": "Ned",
  "lastname": "Spirit",
  "email": "nspirit4@smugmug.com",
  "gender": "Male",
  "feebalance": 40142
}, {
  "id": 6,
  "firstname": "Kristal",
  "lastname": "Cody",
  "email": "kcody5@irs.gov",
  "gender": "Female",
  "feebalance": 39728
}, {
  "id": 7,
  "firstname": "Renie",
  "lastname": "Lambrecht",
  "email": "rlambrecht6@tmall.com",
  "gender": "Female",
  "feebalance": 19573
}, {
  "id": 8,
  "firstname": "Flory",
  "lastname": "Edwards",
  "email": "fedwards7@china.com.cn",
  "gender": "Female",
  "feebalance": 12312
}, {
  "id": 9,
  "firstname": "Eugenius",
  "lastname": "Threader",
  "email": "ethreader8@privacy.gov.au",
  "gender": "Male",
  "feebalance": 35562
}, {
  "id": 10,
  "firstname": "Cleopatra",
  "lastname": "Klosser",
  "email": "cklosser9@newsvine.com",
  "gender": "Female",
  "feebalance": 42907
}, {
  "id": 11,
  "firstname": "Leighton",
  "lastname": "Luety",
  "email": "lluetya@odnoklassniki.ru",
  "gender": "Male",
  "feebalance": 7007
}, {
  "id": 12,
  "firstname": "Nanete",
  "lastname": "Elsey",
  "email": "nelseyb@hatena.ne.jp",
  "gender": "Female",
  "feebalance": 21122
}, {
  "id": 13,
  "firstname": "Tiffany",
  "lastname": "Denkin",
  "email": "tdenkinc@ed.gov",
  "gender": "Female",
  "feebalance": 12791
}, {
  "id": 14,
  "firstname": "Tracey",
  "lastname": "Tomasz",
  "email": "ttomaszd@ebay.com",
  "gender": "Male",
  "feebalance": 27291
}, {
  "id": 15,
  "firstname": "Martina",
  "lastname": "Prandini",
  "email": "mprandinie@multiply.com",
  "gender": "Female",
  "feebalance": 27192
}, {
  "id": 16,
  "firstname": "Tammara",
  "lastname": "Eate",
  "email": "teatef@sohu.com",
  "gender": "Female",
  "feebalance": 8342
}, {
  "id": 17,
  "firstname": "Guntar",
  "lastname": "Leech",
  "email": "gleechg@scribd.com",
  "gender": "Male",
  "feebalance": 23193
}, {
  "id": 18,
  "firstname": "Roi",
  "lastname": "Thaxton",
  "email": "rthaxtonh@themeforest.net",
  "gender": "Male",
  "feebalance": 16338
}, {
  "id": 19,
  "firstname": "Ashil",
  "lastname": "Wrathmall",
  "email": "awrathmalli@a8.net",
  "gender": "Female",
  "feebalance": 43543
}, {
  "id": 20,
  "firstname": "Fidelio",
  "lastname": "Whitebread",
  "email": "fwhitebreadj@hexun.com",
  "gender": "Male",
  "feebalance": 15511
}]
units =[{
  "id": 1,
  "name": "justo aliquam"
}, {
  "id": 2,
  "name": "porttitor id"
}, {
  "id": 3,
  "name": "feugiat"
}, {
  "id": 4,
  "name": "tempus"
}, {
  "id": 5,
  "name": "in leo maecenas"
}, {
  "id": 6,
  "name": "fusce"
}, {
  "id": 7,
  "name": "viverra dapibus"
}, {
  "id": 8,
  "name": "amet justo morbi"
}, {
  "id": 9,
  "name": "aliquet maecenas leo"
}, {
  "id": 10,
  "name": "mauris non"
}, {
  "id": 11,
  "name": "in felis"
}, {
  "id": 12,
  "name": "semper porta volutpat"
}, {
  "id": 13,
  "name": "et tempus"
}, {
  "id": 14,
  "name": "turpis nec"
}, {
  "id": 15,
  "name": "in"
}, {
  "id": 16,
  "name": "amet"
}, {
  "id": 17,
  "name": "sodales"
}, {
  "id": 18,
  "name": "in"
}, {
  "id": 19,
  "name": "et ultrices posuere"
}, {
  "id": 20,
  "name": "mi nulla ac"
}]

from random import randint
with app.app_context():
    # students =[]
    # for student in sample_students:
    #     student = Student(**student)
    #     students.append(student)
    # db.session.add_all(students)
    # db.session.commit()

    # attr, inst=
    students = Student.query.all()
    allunits=[]
    for unit in units:
        unt =Units(**unit)
        unt.student= students[randint(1,19)]
        allunits.append(unt)
    db.session.add_all(allunits)
    db.session.commit()





