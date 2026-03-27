# ⚗️ REMI — Renewable Energy Materials Intelligence

An AI-powered materials science platform for analyzing and predicting properties of renewable energy materials including solar cells and batteries.

## 🔬 What it does

**Materials Dashboard**
Explore and visualize properties of 117 real materials from the Materials Project database. Interactive charts comparing solar and battery materials across band gap, formation energy, density and more.

**Property Predictor**
Input material properties and get an instant ML prediction of the band gap. Instantly know if a material is suitable for solar cells or batteries.

## 🛠️ Built with
- Python
- Materials Project API — real quantum mechanical materials data
- Scikit-learn — Random Forest ML model (R² = 0.815)
- Plotly — interactive scientific visualizations
- Streamlit — multi-page web application
- Anthropic Claude API

## 🚀 How to run locally
1. Clone the repository
2. Create conda environment: `conda create -n remi python=3.11 -y`
3. Activate: `conda activate remi`
4. Install dependencies: `pip install -r requirements.txt`
5. Add your API keys to `.env` file
6. Fetch materials data: `python utils.py`
7. Train the model: `python predictor.py`
8. Launch the app: `streamlit run home.py`

## 📊 Model Performance
- Algorithm: Random Forest Regressor
- Target: Band gap prediction (eV)
- R² Score: 0.815
- Mean Absolute Error: 0.598 eV

## Built by
Shingi Machaka — MS Business Analytics & AI, American University (Kogod School of Business)
