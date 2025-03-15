from useradd import Adduser
from schema import Usercreate,userinlogin
from secutiy.codingdata import encrypt
from secutiy.jwt import jwtclass
from fastapi import HTTPException
from user import Userr
from database import get_db


class usermanagement(Adduser):
    def __init__(self, session):
        super().__init__(session)
        
    def sign_up_user(self,Usercreate:Usercreate):
        if(self.chk_user_email(Usercreate.email)):
          raise HTTPException(status_code=400, detail="Email already in use")
        Usercreate.password=encrypt.hash_passwords(Usercreate.password)
        print("im here")
        return   self.create_user(Usercreate)
        print("im here again")

    
    def log_in(self,user:userinlogin):
        if(self.chk_user_email(user.email)):
          encryptedpass=self.session.query(Userr).filter_by(email=user.email).first().password
          encryptedpass=self.get_user_by_email(user.email).password
          if(encrypt.testing_password(user.password,encryptedpass)):
             return jwtclass.jwt_gen(user_id=self.get_user_id(user))
          else:
              raise HTTPException(status_code=400, detail="please check yout inputs") 
        raise HTTPException(status_code=400, detail="account not found")   


           