import os
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler
import pickle

def train_model():
    """Train ML model to predict band gap from other material properties"""
    
    df = pd.read_csv("data/materials.csv")
    df = df.dropna()
    
    features = ["formation_energy", "density", "volume", "energy_above_hull"]
    target = "band_gap"
    
    X = df[features]
    y = df[target]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    y_pred = model.predict(X_test_scaled)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"Model Performance:")
    print(f"Mean Absolute Error: {mae:.4f} eV")
    print(f"R² Score: {r2:.4f}")
    
    os.makedirs("data", exist_ok=True)
    with open("data/model.pkl", "wb") as f:
        pickle.dump(model, f)
    with open("data/scaler.pkl", "wb") as f:
        pickle.dump(scaler, f)
    
    print("Model saved to data/model.pkl")
    return model, scaler, mae, r2

def predict_band_gap(formation_energy, density, volume, energy_above_hull):
    """Predict band gap for a new material"""
    
    with open("data/model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("data/scaler.pkl", "rb") as f:
        scaler = pickle.load(f)
    
    features = np.array([[formation_energy, density, volume, energy_above_hull]])
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)[0]
    
    return round(prediction, 4)

if __name__ == "__main__":
    train_model()
    