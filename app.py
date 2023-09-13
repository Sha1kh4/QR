from flask import Flask, session, request,flash, render_template, redirect, url_for,flash
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

class login(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)


@app.route('/')
def main():
    return "hello"

@app.route("/login", methods=['GET', 'POST'])
def login_admin():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        print(username , password)
        result = login.query.filter_by(username=username).first()
        
        if result is None: 
            flash('Username not found. Please try again.')
        elif password != result.password:
            flash('Invalid Credentials. Please try again.')
        else:
            session['user'] = username
            return redirect(url_for("admin"))
    
    return render_template("login.html", title="Login")


    
@app.route("/admin", methods=['GET'])
def admin():
    return "hello"
    


@app.route("/a/<string:user_slug>", methods=['GET'])
def teach(user_slug):
    infos = info.query.filter_by(name=user_slug).first()
    exp = experience.query.filter_by(id=infos.no).first()
    print(exp.exp1name)
    return render_template("teach.html", db=infos,exp=exp)

