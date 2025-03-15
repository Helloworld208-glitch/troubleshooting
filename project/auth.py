from fastapi import APIRouter,Depends
from schema import Usercreate, userinlogin


from database import get_db

from usermanagement import * 
authentification = APIRouter()



@authentification.post("/login")
def auth(userinlogin: userinlogin, session=Depends(get_db)):
        return usermanagement(session).log_in(userinlogin)



@authentification.post("/signup")
def signup(Usercreate: Usercreate, session = Depends(get_db) ):
        return usermanagement(session).sign_up_user(Usercreate)