import joblib
import pandas as pd


model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
encoder = joblib.load("encoder.pkl")

LOW_YIELD_THRESH = 15.2
HIGH_YIELD_THRESH = 28.6


categorical_cols = ['Crop']

numerical_cols = [
    'Temperature (C)',
    'Rainfall (mm)',
    'Humidity (%)',
    'Sunlight (hours)',
    'Soil pH',
    'Soil Nitrogen (%)',
    'Soil Phosphorus (ppm)',
    'Soil Potassium (ppm)',
    'Altitude (m)',
    'Wind Speed (m/s)'
]

def get_yield_category(value):
    if value < LOW_YIELD_THRESH:
        return "Low Yield"
    elif value < HIGH_YIELD_THRESH:
        return "Medium Yield"
    else:
        return "High Yield"

def predict_yield(input_dict):
    """
    input_dict example:
    {
        'Crop': 'Wheat',
        'Temperature (C)': 25,
        ...
    }
    """


    df = pd.DataFrame([input_dict])

    
    encoded = encoder.transform(df[categorical_cols])
    encoded_df = pd.DataFrame(
        encoded,
        columns=encoder.get_feature_names_out(categorical_cols)
    )


    final_input = pd.concat(
        [df[numerical_cols].reset_index(drop=True),
         encoded_df.reset_index(drop=True)],
        axis=1
    )


    scaled_input = scaler.transform(final_input)


    prediction = model.predict(scaled_input)[0]
    category = get_yield_category(prediction)

    return prediction, category

    