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




engine = create_engine('sqlite:///DigitalPass.db')
 

Base.metadata.create_all(engine)
