from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Verdicto Backend 🚀"}
    from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define input format
class CaseInput(BaseModel):
    case_details: str

@app.get("/")
def read_root():
    return {"message": "Welcome to Verdicto Backend 🚀"}

@app.post("/predict")
def predict_case(data: CaseInput):
    # For now, just return a dummy prediction
    return {
        "case": data.case_details,
        "prediction": "Bail Granted ✅ (dummy result)"
    }