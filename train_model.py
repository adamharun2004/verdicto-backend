import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

# Sample training data
data = {
    "age": [22, 45, 30, 40, 18, 60],
    "crime_severity": [1, 3, 2, 3, 1, 2],
    "past_offenses": [0, 2, 1, 3, 0, 1],
    "verdict": [0, 1, 0, 1, 0, 1]   # 0 = Bail, 1 = Conviction
}
df = pd.DataFrame(data)

# Features and labels
X = df[["age", "crime_severity", "past_offenses"]]
y = df["verdict"]

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")
print("✅ Model trained and saved as model.pkl")