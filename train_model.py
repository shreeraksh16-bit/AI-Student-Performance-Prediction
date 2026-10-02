import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
data = pd.read_csv("dataset/student-mat.csv", sep=";")

# Select input features
X = data[["studytime", "failures", "absences", "G1", "G2"]]

# Select target
y = data["G3"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create the model
model = RandomForestRegressor(
    n_estimators=100, random_state=42
)

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Model training completed!")
print("Mean Absolute Error:", round(mae, 2))
print("R2 Score:", round(r2, 2))
# Save the trained model
joblib.dump(model, "student_model.pkl")

print("Model saved successfully!")