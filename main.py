from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from flask_admin import Admin 
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///digitalpass.db'
app.config['SECRET_KEY']='mysecret'
db = SQLAlchemy(app)

admin = Admin(app)

class user(db.Model):

   
    pin = db.Column(db.String(10))
    rollno = db.Column(db.String(10))        
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    typeCard = db.Column(db.String(5))
    rfidno  = db.Column(db.String(50))

    id = db.Column(db.Integer, primary_key = True)


class history(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(250), nullable=False)    
    rfidno  = db.Column(db.String(50))
    date = db.Column(db.DateTime)

class statement(db.Model):

    id = db.Column(db.Integer, primary_key = True)    
    balance_trip = db.Column(db.String(8))    
    rfidno  = db.Column(db.String(50))
    name = db.Column(db.String(250), nullable=False)



admin.add_view(ModelView(user,db.session))
admin.add_view(ModelView(history,db.session))
admin.add_view(ModelView(statement,db.session))

if __name__ == '__main__':
    app.run(debug=True)