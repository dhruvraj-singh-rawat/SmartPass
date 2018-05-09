from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()

class UserTable(Base):
    __tablename__ = 'user_table'
   
    pin = Column(String(10))
    rollno = Column(String(10))        
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    typeCard = Column(String(5))
    rfidno  = Column(String(50))

    id = Column(Integer, primary_key = True)
    
    statementhistory=relationship('TravelHistory',backref='account_holder',lazy='dynamic')
    statementtable=relationship('TravelStatement',backref='account_holder',lazy='dynamic')

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

class TravelHistory(Base):
    __tablename__ = 'Travel History'

    id = Column(Integer, primary_key = True)
    email = Column(String(250))
    trips_added = Column(String(250))
    trip_taken = Column(String(250))

    holder_id = Column(Integer,ForeignKey('user_table.id'))

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
          
           'email'           : self.email,
           'trips_added'         : self.trips_added,
           'trip_taken'              : self.trip_taken,
       }

class TravelStatement(Base):
    __tablename__ = 'Travel Statement'


    
    id = Column(Integer, primary_key = True)    
    balance_trip = Column(String(8))    
    email = Column(String(250))

    holder_id = Column(Integer,ForeignKey('user_table.id'))
    


    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {          
           
           'balance_trip'         : self.balance_trip,
           'email'         : self.email,

       }



engine = create_engine('sqlite:///DigitalPass.db')
 

Base.metadata.create_all(engine)
