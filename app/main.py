from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas import user_input
from app.db_models import loan_prediction
from app.predict import predict_loan_approval


app = FastAPI(
    title="Prediction of Loan using API",
    version="1.0",
    description="By using inputs predicts whether loan is approved or not"
)

# 🌍 Enable frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🎨 Templates folder
templates = Jinja2Templates(directory="templates")


# 🏠 Home Route → Loads index.html
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


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
