import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def show_dashboard():
    st.title("Materials Dashboard")
    st.caption("Visual analysis of renewable energy materials properties")
    
    try:
        df = pd.read_csv("data/materials.csv")
    except FileNotFoundError:
        st.error("No materials data found. Please run utils.py first.")
        return
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Materials", len(df))
    with col2:
        st.metric("Solar Materials", len(df[df["category"]=="Solar"]))
    with col3:
        st.metric("Battery Materials", len(df[df["category"]=="Battery"]))
    with col4:
        st.metric("Avg Band Gap", f"{df['band_gap'].mean():.2f} eV")
    
    st.divider()
    
    st.subheader("Band gap distribution by category")
    fig1 = px.histogram(
        df, x="band_gap", color="category",
        nbins=30, barmode="overlay",
        color_discrete_map={"Solar": "#00C49F", "Battery": "#FF8042"},
        labels={"band_gap": "Band Gap (eV)", "count": "Number of Materials"}
    )
    fig1.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig1, use_container_width=True)
    
    st.subheader("Formation energy vs band gap")
    fig2 = px.scatter(
        df, x="formation_energy", y="band_gap",
        color="category", hover_data=["formula", "density"],
        color_discrete_map={"Solar": "#00C49F", "Battery": "#FF8042"},
        labels={
            "formation_energy": "Formation Energy (eV/atom)",
            "band_gap": "Band Gap (eV)"
        }
    )
    fig2.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig2, use_container_width=True)
    
    st.subheader("Top 10 materials by band gap")
    top10 = df.nlargest(10, "band_gap")[["formula", "band_gap", "density", "category"]]
    fig3 = px.bar(
        top10, x="formula", y="band_gap", color="category",
        color_discrete_map={"Solar": "#00C49F", "Battery": "#FF8042"},
        labels={"band_gap": "Band Gap (eV)", "formula": "Material"}
    )
    fig3.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig3, use_container_width=True)
    
    st.subheader("Full materials database")
    st.dataframe(df, use_container_width=True)
    