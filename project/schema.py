from pydantic import EmailStr,BaseModel



class Usercreate(BaseModel):
    firstname:str
    lasttname:str
    email: EmailStr
    password:str





class userinlogin(BaseModel):
      email: EmailStr
      password:str
