from  database import Base
from sqlalchemy import Column, Integer ,String



class Userr(Base):
    __tablename__="User"
    id=Column(Integer,primary_key=True)
    firstname =Column(String(50))
    lasttname =Column(String(50))
    email =Column(String(50))
    password =Column(String(200))
