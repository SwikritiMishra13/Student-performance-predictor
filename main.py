import pandas as pd
from sklearn.linear_model import LinearRegression

print("Welcome to Student Performance Predictor")
print("This tool estimates marks using study data\n")

# Load dataset
df = pd.read_csv("data.csv")

# Features and target
X = df[["hours_study", "attendance"]]
y = df["marks"]

# Train model
model = LinearRegression()
model.fit(X, y)

print("=== Student Performance Predictor ===")

# Take input
hours = float(input("Enter study hours: "))
attendance = float(input("Enter attendance (%): "))

# Predict
prediction = model.predict([[hours, attendance]])

print(f"Predicted Marks: {prediction[0]:.2f}")
if prediction[0] >= 40:
    print("Status: Pass")
else:
    print("Status: Fail")