import streamlit as st
from dashboard import show_dashboard
from predictor_page import show_predictor

st.set_page_config(
    page_title="REMI",
    page_icon="⚗️",
    layout="wide"
)

st.sidebar.title("⚗️ REMI")
st.sidebar.caption("Renewable Energy Materials Intelligence")
st.sidebar.divider()

page = st.sidebar.radio(
    "Navigate",
    ["Home", "Materials Dashboard", "Property Predictor"],
    label_visibility="collapsed"
)

st.sidebar.divider()
st.sidebar.caption("Built by Shingi Machaka")
st.sidebar.caption("MS Business Analytics & AI")
st.sidebar.caption("American University")

if page == "Home":
    st.title("⚗️ REMI")
    st.subheader("Renewable Energy Materials Intelligence Platform")
    st.caption("AI-powered materials analysis for solar cells and batteries")
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Materials Dashboard")
        st.write("Explore and visualize properties of 117 real materials from the Materials Project database. Compare solar and battery materials across band gap, formation energy, density and more.")
        if st.button("Open Dashboard", use_container_width=True):
            st.session_state.page = "Materials Dashboard"
            st.rerun()
    
    with col2:
        st.markdown("### Property Predictor")
        st.write("Input material properties and get an instant AI prediction of the band gap. Find out if your material is suitable for solar cells or batteries.")
        if st.button("Open Predictor", use_container_width=True):
            st.session_state.page = "Property Predictor"
            st.rerun()
    
    st.divider()
    
    st.markdown("### What is REMI?")
    st.write("""
    REMI combines real materials science data with machine learning to help 
    researchers, industry professionals and policymakers understand renewable energy materials.
    
    Built on data from the Materials Project — a database of over 150,000 materials 
    computed using quantum mechanical calculations — REMI makes materials 
    intelligence accessible to everyone.
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Materials in Database", "117")
    with col2:
        st.metric("ML Model R² Score", "0.815")
    with col3:
        st.metric("Properties Analyzed", "6")

elif page == "Materials Dashboard":
    show_dashboard()

elif page == "Property Predictor":
    show_predictor()
