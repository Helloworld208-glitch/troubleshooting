from base import Fatherclass
from schema import Usercreate,userinlogin
from user import Userr
from secutiy.jwt import  jwtclass
import pydantic

class Adduser(Fatherclass):
  def create_user(self,Usercreate: Usercreate):
      new_user = Userr(**Usercreate.dict(exclude_none=True))
      self.session.add(new_user)
      self.session.commit()
      self.session.refresh(new_user)
      print("finally")
      return jwtclass.jwt_gen(new_user.id)
  


  def get_user_by_email(self,email:str):
    user = self.session.query(Userr).filter_by(email=email).first()
    return user
  

  def chk_user_email(self,email:str):
    user = self.session.query(Userr).filter_by(email=email).first()
    return bool(user)
  def get_user_by_id(self,id:int):
    return self.session.query(Userr).filter_by(id=id).first()
  def get_user_id(self,user:userinlogin):
    return self.session.query(Userr).filter_by(email=user.email).first().id