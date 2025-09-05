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
    from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression

app = FastAPI()

# ---- Step 1: Define input schema ----
class CaseInput(BaseModel):
    age: int
    crime_severity: int   # e.g., 1=low, 2=medium, 3=high
    past_offenses: int

# ---- Step 2: Train a simple model (demo data) ----
# Sample training data
data = {
    "age": [22, 45, 30, 40, 18, 60],
    "crime_severity": [1, 3, 2, 3, 1, 2],
    "past_offenses": [0, 2, 1, 3, 0, 1],
    "verdict": [0, 1, 0, 1, 0, 1]   # 0 = Bail, 1 = Conviction
}
df = pd.DataFrame(data)

X = df[["age", "crime_severity", "past_offenses"]]
y = df["verdict"]

model = LogisticRegression()
model.fit(X, y)

# ---- Step 3: Routes ----
@app.get("/")
def read_root():
    return {"message": "Verdicto Backend Running"}

@app.post("/predict")
def predict_case(input_data: CaseInput):
    input_df = pd.DataFrame([input_data.dict()])
    prediction = model.predict(input_df)[0]

    result = "Conviction" if prediction == 1 else "Bail"
    return {"prediction": result}
    from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# ---- Input schema ----
class CaseInput(BaseModel):
    age: int
    crime_severity: int
    past_offenses: int

# ---- Load pre-trained model ----
model = joblib.load("model.pkl")

# ---- Routes ----
@app.get("/")
def read_root():
    return {"message": "Verdicto Backend Running"}

@app.post("/predict")
def predict_case(input_data: CaseInput):
    input_df = pd.DataFrame([input_data.dict()])
    prediction = model.predict(input_df)[0]

    result = "Conviction" if prediction == 1 else "Bail"
    return {"prediction": result}
