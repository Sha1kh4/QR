from flask import Flask, session, request, g, render_template, redirect, url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
import mysql.connector as sql

import os

app = Flask(__name__)
app.secret_key = "1234"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://'+os.getenv("DB_USERNAME")+':'+os.getenv("DB_PASSWORD")+'@'+os.getenv("DB_HOST")+':3306'+'/'+os.getenv("DB_NAME")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class info(db.Model):
    no = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.String(255))
    name = db.Column(db.String(255))
    position = db.Column(db.String(255))
    contact = db.Column(db.String(255))
    resume = db.Column(db.String(255))
    skill1 = db.Column(db.String(255))
    skill2 = db.Column(db.String(255))
    skill3 = db.Column(db.String(255))
    skill4 = db.Column(db.String(255))
    skill5 = db.Column(db.String(255))
    about = db.Column(db.Text)
    linkedin = db.Column(db.String(255))
    fb = db.Column(db.String(255))
    insta = db.Column(db.String(255))
    twt = db.Column(db.String(255))
    exp = db.Column(db.Integer)


class experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exp1name = db.Column(db.String(255)) 
    exp1place  = db.Column(db.String(255))
    exp1time = db.Column(db.String(255))
    exp1info = db.Column(db.String(255))
    exp2name = db.Column(db.String(255))
    exp2place = db.Column(db.String(255))
    exp2time = db.Column(db.String(255))
    exp2info = db.Column(db.String(255))
    exp3name = db.Column(db.String(255))
    exp3place = db.Column(db.String(255))
    exp3time = db.Column(db.String(255))
    exp3info = db.Column(db.String(255))
    exp4name = db.Column(db.String(255))
    exp4place = db.Column(db.String(255))
    exp4time = db.Column(db.String(255))
    exp4info = db.Column(db.String(255))
    no = db.Column(db.Integer, db.ForeignKey("info.no"))

@app.route('/')
def main():
    return "hello"


@app.route('/teach')
def teach():

    infos = info.query.filter_by(no=1).first()
    exp = experience.query.filter_by(id=1).first()
    print(exp.exp1name)
    return render_template("teach.html", db=infos,exp=exp)



# @app.route('/edit',methods=['GET', 'POST'])
# def edit():
#         if(request.method=='POST'):
#             name  = request.form.get('name')
#             position = request.form.get('position')
#             contact = request.form.get('contact')
#             resume = request.form.get('resume')
#             skill1 = request.form.get('skill1')
#             skill2 = request.form.get('skill2')
#             skill3 = request.form.get('skill3')
#             skill4 = request.form.get('skill4')
#             skill5 = request.form.get('skill5')
#             # info = request.form.get('info')
#             linkedin = request.form.get('linkedin')
#             insta = request.form.get('insta')
#             twt = request.form.get('twt')
#             exp = request.form.get('exp')
            

#             entry=info(name=name,position=position,contact=contact,resume=resume,skill1=skill1,skill2=skill2,skill3=skill3,skill4=skill4,skill5=skill5,linkedin=linkedin,insta=insta,twt=twt,exp=exp)
#             db.session.add(entry)
#             db.session.commit()

#         return render_template('form.html')
