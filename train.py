import pandas as pd
import joblib
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


df = pd.read_csv("crop_yield_dataset.csv")


X = df.drop("Crop Yield (tons/ha)", axis=1)
y = df["Crop Yield (tons/ha)"]


categorical_cols = ['Crop']
numerical_cols = [
    'Temperature (C)', 'Rainfall (mm)', 'Humidity (%)',
    'Sunlight (hours)', 'Soil pH',
    'Soil Nitrogen (%)', 'Soil Phosphorus (ppm)',
    'Soil Potassium (ppm)', 'Altitude (m)', 'Wind Speed (m/s)'
]


encoder = OneHotEncoder(drop="first", sparse_output=False)
encoded_cat = encoder.fit_transform(X[categorical_cols])

encoded_df = pd.DataFrame(
    encoded_cat,
    columns=encoder.get_feature_names_out(categorical_cols)
)

X_final = pd.concat(
    [X[numerical_cols].reset_index(drop=True),
     encoded_df.reset_index(drop=True)],
    axis=1
)


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_final)


model = LinearRegression()
model.fit(X_scaled, y)


joblib.dump(model, "model.pkl")
joblib.dump(scaler, "scaler.pkl")
joblib.dump(encoder, "encoder.pkl")

print("Training complete. Files saved.")
print("Mean yield:", y.mean())