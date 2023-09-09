from flask import Flask, session, request, g, render_template, redirect, url_for,flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "1234"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://'+os.getenv("DB_USERNAME")+':'+os.getenv("DB_PASSWORD")+'@'+os.getenv("DB_HOST")+':3306'+'/'+os.getenv("DB_NAME")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class info(db.Model):
    no = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.String(255))
    Name = db.Column(db.String(255))
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
    exp = db.Column(db.Integer(2))
    exp1name = db.Column(db.String(255))
    exp1place = db.Column(db.String(255))
    exp1time = db.Column(db.String(255))
    exp1info = db.Column(db.Text)
