from sqlalchemy import Column,Integer,String,DateTime,Float
from datetime import datetime
from app.database import Base
from sqlalchemy.dialects.postgresql import JSON



class loan_prediction(Base):
    __tablename__ = 'loan_applications'
    Gender = Column(String)
    Married=Column(String)
    Education =Column(String)
    Self_Employed = Column(String)
    ApplicantIncome = Column(Integer)
    Property_Area = Column(String)
    Prediction = Column(JSON)
    Created_at = Column(DateTime,default=datetime.utcnow)
    id = Column(Integer,primary_key=True,index=True)
