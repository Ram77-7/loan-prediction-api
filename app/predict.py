from app.schemas import user_input
from app.models import (
    le_gender,
    le_married,
    le_education,
    le_self_employed,
    le_property_area,
    pca_transformer,
    Load_model
)
import numpy as np

def predict_loan_approval(data: user_input):
    try:
        Gender = le_gender.transform([data.Gender])[0]
        Married = le_married.transform([data.Married])[0]
        Education = le_education.transform([data.Education])[0]
        Self_Employed = le_self_employed.transform([data.Self_Employed])[0]
        Property_Area = le_property_area.transform([data.Property_Area])[0]

        X = np.array([[
            Gender,
            Married,
            Education,
            Self_Employed,
            data.ApplicantIncome,
            Property_Area
        ]], dtype=np.float32)

        # Only transform if PCA was used in training
        pca_features = pca_transformer.transform(X)
        prediction = Load_model.predict(pca_features)

        return {
    "status": "Approved" if prediction[0][0] >= 0.5 else "Not Approved",
    "probability": round(float(prediction[0][0]), 2)
}

    except Exception as e:
        print("PREDICTION ERROR:", e)
        return f"Error: {e}"
