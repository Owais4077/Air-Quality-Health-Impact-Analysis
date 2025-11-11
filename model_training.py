import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib
from data_preprocessing import load_data, clean_data, format_dates

def train_model(df, features, target):
    """Trains a RandomForestRegressor model and evaluates it."""
    X = df[features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Model Mean Squared Error: {mse}")
    print(f"Model R^2 Score: {r2}")

    return model

def save_model(model, path):
    """Saves the trained model to a file."""
    joblib.dump(model, path)
    print(f"Model saved to {path}")

if __name__ == '__main__':
    # Load and preprocess data
    aq_path = '../data/air_quality_data.csv'
    aq_data, _ = load_data(aq_path, '../data/health_data.csv') # health data not needed for AQI prediction
    aq_data = clean_data(aq_data)
    aq_data = format_dates(aq_data)

    # Feature engineering (e.g., using date components)
    aq_data['Year'] = aq_data['Date'].dt.year
    aq_data['Month'] = aq_data['Date'].dt.month
    aq_data['Day'] = aq_data['Date'].dt.day

    # Define features and target
    features = ['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3', 'Year', 'Month', 'Day']
    target = 'AQI'

    # Train and save the model
    trained_model = train_model(aq_data, features, target)
    model_path = '../models/aqi_model.joblib'
    save_model(trained_model, model_path)
