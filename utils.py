import os
from dotenv import load_dotenv
from mp_api.client import MPRester
import pandas as pd

load_dotenv()

def get_materials_data():
    """Fetch solar and battery materials from Materials Project API"""
    
    api_key = os.getenv("MP_API_KEY")
    
    materials_list = []
    
    with MPRester(api_key) as mpr:
        print("Fetching solar cell materials...")
        solar_docs = mpr.materials.summary.search(
            elements=["Si", "Ge", "Ga"],
            fields=[
                "material_id",
                "formula_pretty",
                "band_gap",
                "energy_above_hull",
                "formation_energy_per_atom",
                "density",
                "volume"
            ],
            num_chunks=1,
            chunk_size=100
        )
        
        for doc in solar_docs:
            materials_list.append({
                "material_id": doc.material_id,
                "formula": doc.formula_pretty,
                "band_gap": doc.band_gap,
                "energy_above_hull": doc.energy_above_hull,
                "formation_energy": doc.formation_energy_per_atom,
                "density": doc.density,
                "volume": doc.volume,
                "category": "Solar"
            })
        
        print("Fetching battery materials...")
        battery_docs = mpr.materials.summary.search(
            elements=["Li", "Na"],
            fields=[
                "material_id",
                "formula_pretty",
                "band_gap",
                "energy_above_hull",
                "formation_energy_per_atom",
                "density",
                "volume"
            ],
            num_chunks=1,
            chunk_size=100
        )
        
        for doc in battery_docs:
            materials_list.append({
                "material_id": doc.material_id,
                "formula": doc.formula_pretty,
                "band_gap": doc.band_gap,
                "energy_above_hull": doc.energy_above_hull,
                "formation_energy": doc.formation_energy_per_atom,
                "density": doc.density,
                "volume": doc.volume,
                "category": "Battery"
            })
    
    df = pd.DataFrame(materials_list)
    df = df.dropna()
    
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/materials.csv", index=False)
    print(f"Saved {len(df)} materials to data/materials.csv")
    
    return df

if __name__ == "__main__":
    df = get_materials_data()
    print(df.head())
    print(f"Total materials: {len(df)}")
    