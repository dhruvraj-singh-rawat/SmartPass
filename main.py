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

class User(db.Model):

   
    pin = db.Column(db.String(10))
    rollno = db.Column(db.String(10))        
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    typeCard = db.Column(db.String(5))
    rfidno  = db.Column(db.String(50))

    id = db.Column(db.Integer, primary_key = True)
    
    

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'         : self.name,
           'email'           : self.email,
           'rfidno'          : self.rfidno,
           'pin'              : self.pin,
           'rollno'           : self.rollno,
           'typeCard'         : self.typeCard
       }

class TravelHistory(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(250))
    trips_added = db.Column(db.String(250))
    trip_taken = db.Column(db.String(250))

    holder_id = db.relationship('User', backref='TravelHistory', lazy='dynamic')

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
          
           'email'           : self.email,
           'trips_added'         : self.trips_added,
           'trip_taken'              : self.trip_taken,
       }



class TravelStatement(db.Model):

    id = db.Column(db.Integer, primary_key = True)    
    balance_trip = db.Column(db.String(8))    
    email = db.Column(db.String(250))

    holder_id = db.relationship('User', backref='TravelStatement', lazy='dynamic')

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {          
           
           'balance_trip'         : self.balance_trip,
           'email'         : self.email,

       }


admin.add_view(ModelView(User,db.session))
admin.add_view(ModelView(TravelHistory,db.session))
admin.add_view(ModelView(TravelStatement,db.session))

if __name__ == '__main__':
    app.run(debug=True)