import streamlit as st
from predictor import predict_band_gap, train_model
import os

def show_predictor():
    st.title("Material Property Predictor")
    st.caption("Predict the band gap of a new material using machine learning")

    if not os.path.exists("data/model.pkl"):
        st.warning("Model not trained yet. Training now...")
        with st.spinner("Training model..."):
            model, scaler, mae, r2 = train_model()
        st.success(f"Model trained! R² Score: {r2:.4f}, MAE: {mae:.4f} eV")

    st.divider()

    st.subheader("Enter material properties")
    st.caption("Adjust the sliders to match your material's known properties")

    col1, col2 = st.columns(2)

    with col1:
        formation_energy = st.slider(
            "Formation energy (eV/atom)",
            min_value=-5.0, max_value=0.0,
            value=-2.0, step=0.01,
            help="Energy released when the material forms from its elements"
        )
        density = st.slider(
            "Density (g/cm³)",
            min_value=0.5, max_value=15.0,
            value=3.0, step=0.1,
            help="Mass per unit volume of the material"
        )

    with col2:
        volume = st.slider(
            "Volume (ų)",
            min_value=10.0, max_value=2000.0,
            value=300.0, step=1.0,
            help="Unit cell volume of the material"
        )
        energy_above_hull = st.slider(
            "Energy above hull (eV/atom)",
            min_value=0.0, max_value=1.0,
            value=0.05, step=0.001,
            help="Thermodynamic stability — lower is more stable"
        )

    st.divider()

    if st.button("Predict Band Gap", type="primary", use_container_width=True):
        with st.spinner("Running prediction..."):
            prediction = predict_band_gap(
                formation_energy, density, volume, energy_above_hull
            )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Predicted Band Gap", f"{prediction} eV")

        with col2:
            if prediction < 0.1:
                suitability = "Metal/Conductor"
                color = "inverse"
            elif prediction < 1.5:
                suitability = "Narrow gap — battery"
                color = "normal"
            elif prediction <= 3.0:
                suitability = "Ideal for solar cells"
                color = "normal"
            else:
                suitability = "Wide gap — insulator"
                color = "inverse"
            st.metric("Material Type", suitability)

        with col3:
            ideal_solar = 1.0 <= prediction <= 1.8
            st.metric("Solar Cell Suitable", "Yes" if ideal_solar else "No")

        st.divider()

        st.subheader("What does this mean?")
        if prediction < 0.1:
            st.info("This material behaves like a metal. Electrons flow freely — not suitable for solar cells but useful as electrodes in batteries.")
        elif prediction < 1.5:
            st.info("Narrow band gap material. Good candidate for battery electrodes or infrared solar cells.")
        elif prediction <= 1.8:
            st.success("This material has an ideal band gap for solar cell applications. The optimal range for single-junction solar cells is 1.0-1.8 eV, matching the solar spectrum well.")
        elif prediction <= 3.0:
            st.warning("Wide band gap material. Could work in tandem solar cells or UV applications but not ideal as a single-junction solar cell.")
        else:
            st.error("Very wide band gap — this material is an insulator. Not suitable for solar or battery applications.")
            