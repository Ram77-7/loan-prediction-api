from pydantic import BaseModel

class user_input(BaseModel):
    Gender:str
    Married:str
    Education:str
    Self_Employed:str
    ApplicantIncome:int
    Property_Area:str

    