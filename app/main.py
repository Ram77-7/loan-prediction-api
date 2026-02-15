from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.database import Base, engine

from app.dependencies import get_db
from app.schemas import user_input
from app.db_models import loan_prediction
from app.predict import predict_loan_approval


app = FastAPI(
    title="Prediction of Loan using API",
    version="1.0",
    description="By using inputs predicts whether loan is approved or not"
)

Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Diabetes Prediction API"}

# 🔮 Prediction Route
@app.post("/predict")
def prediction(data: user_input, db: Session = Depends(get_db)):
    try:
        # 🔮 ML Prediction
        result = predict_loan_approval(data)

        # 💾 Save to Database
        record = loan_prediction(
            Gender=data.Gender,
            Married=data.Married,
            Education=data.Education,
            Self_Employed=data.Self_Employed,
            ApplicantIncome=data.ApplicantIncome,
            Property_Area=data.Property_Area,
            Prediction=str(result)
        )

        db.add(record)
        db.commit()
        db.refresh(record)

        return {
            "loan_status": result,
            "record_id": record.id
        }

    except Exception as e:
        print("ERROR IN PREDICTION:", e)
        raise HTTPException(status_code=500, detail=str(e))
