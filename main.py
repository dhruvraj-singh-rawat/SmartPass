from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker

#from database_setup import Base, UserTable, StatementHistory,StatementTable
from flask import session as login_session
import random
import string
import time

#import for flask admin
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin 
# from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
admin=Admin(app)

# Connect to Database and create database session
engine = create_engine('sqlite:///digitalpayment.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()