from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from flask_admin import Admin 
from flask_admin.contrib.sqla import ModelView
import json
import datetime
import time 
import smtplib

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
    day = db.Column(db.String(50))
    time = db.Column(db.String(50))

class statement(db.Model):

    id = db.Column(db.Integer, primary_key = True)    
    balance_trip = db.Column(db.String(8))    
    rfidno  = db.Column(db.String(50))
    name = db.Column(db.String(250), nullable=False)



admin.add_view(ModelView(user,db.session))
admin.add_view(ModelView(history,db.session))
admin.add_view(ModelView(statement,db.session))

#Mailing Server Implementation

def mailer_server(reciever_email,datee,timee,leftee):

	# Python code to illustrate Sending mail from 
	# your Gmail account 
	import smtplib
	 
	# creates SMTP session
	s = smtplib.SMTP('smtp.gmail.com', 587)

	# start TLS for security
	s.starttls()
	 
	# Authentication
	s.login("feedbacklnmiit@gmail.com", "helloworld12345")
	 
	# message to be sent
	SUBJECT="Alert: BusPass Used"
	message_body = "Your Bus was used on "+str(datee)+" at "+str(timee)+" ! Remaining Trip Left "+str(leftee)

	message = 'Subject: {}\n\n{}'.format(SUBJECT, message_body)
	# sending the mail
	s.sendmail("digitalcampuslnmiit@gmail.com", reciever_email, message)
	 
	# terminating the session
	s.quit()




# API IMPLEMENTATION 

@app.route("/api_responce", methods = ['GET', 'POST'])
def api_responce():

    if request.method=='POST':

        rfidno=request.args.get('rfid_no')

    
        user_balance = db.session.query(statement).filter_by(rfidno=rfidno).one()
        user_info=db.session.query(user).filter_by(rfidno=rfidno).one()

        balance_available=int(user_balance.balance_trip)
        

        if balance_available>0:
            balance_available=balance_available-1
            user_balance.balance_trip=balance_available
            db.session.commit()

            day=datetime.datetime.now().strftime("%d/%m/%y")
            timee=time.strftime("%H:%M:%S")

            trip_update=history(name=user_balance.name,rfidno=rfidno,day=day,time=timee)
            db.session.add(trip_update)
            db.session.commit()

            mailer_server(user_info.email,day,timee,balance_available)

            output={
                'status':1,

            }
            return json.dumps(output)
        else:
            output={
                'status':0,
            }
            return json.dumps(output)



    elif request.method=='GET':

        response=make_response(json.dumps('GET is working',200))
        response.headers['Content-Type']='application/json'
        return response

if __name__ == '__main__':

    app.debug = True
    app.run(host='192.168.43.174', port=5000)	
    app.run(debug=True)