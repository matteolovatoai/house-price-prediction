import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# Configurazione pagina
st.set_page_config(page_title="House Price Predictor", layout="centered")

# Percorsi con pathlib
HOME_DIR = Path(__file__).parent
MODEL_PATH = HOME_DIR / "models" / "house_price_model.pkl"

@st.cache_resource
def load_model():
    if not MODEL_PATH.exists():
        st.error(f"❌ Modello non trovato in {MODEL_PATH}")
        return None
    return joblib.load(MODEL_PATH)

def pulire_input(data_dict):
    df = pd.DataFrame([data_dict])
    
    # Mapping logico
    trasformazione_binaria = {'yes': 1, 'no': 0}
    trasformazione_fornitura = {
        'unfurnished': 0,
        'semi-furnished': 1,
        'furnished': 2,
    }

    colonne_yes_no = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea']

    for col in colonne_yes_no:
        df[col] = df[col].map(trasformazione_binaria)
    df['furnishingstatus'] = df['furnishingstatus'].map(trasformazione_fornitura)
    return df

# UI Streamlit
st.title("Housing price prediction 🏠")
st.write("Inserisci i dettagli dell'immobile per ottenere una stima del prezzo.")

model = load_model()

if model:
    # Organizzazione in colonne
    col1, col2 = st.columns(2)

    with col1:
        area = st.number_input("Area (mq)", min_value=1650, max_value=16000, value=5000)
        bedrooms = st.number_input("Camere da letto", 1, 6, 3)
        bathrooms = st.number_input("Bagni", 1, 4, 1)
        stories = st.number_input("Piani", 1, 4, 1)
        parking = st.number_input("Posti auto", 0, 3, 0)

    with col2:
        mainroad = st.checkbox("Strada principale")
        guestroom = st.checkbox("Stanza ospiti")
        basement = st.checkbox("Seminterrato")
        hotwater = st.checkbox("Riscaldamento acqua")
        aircon = st.checkbox("Aria condizionata")
        prefarea = st.checkbox("Zona prestigiosa")
        furnishing = st.selectbox("Arredamento", options=['unfurnished', 'semi-furnished', 'furnished'])

    # Conversione input per il modello
    user_input = {
        'area': area, 'bedrooms': bedrooms, 'bathrooms': bathrooms, 'stories': stories,
        'mainroad': 'yes' if mainroad else 'no',
        'guestroom': 'yes' if guestroom else 'no',
        'basement': 'yes' if basement else 'no',
        'hotwaterheating': 'yes' if hotwater else 'no',
        'airconditioning': 'yes' if aircon else 'no',
        'parking': parking,
        'prefarea': 'yes' if prefarea else 'no',
        'furnishingstatus': furnishing
    }

    if st.button("Calcola Prezzo 🚀", use_container_width=True):
        df_prepared = pulire_input(user_input)
        prediction = model.predict(df_prepared)[0]
        
        st.success(f"### Prezzo Stimato: {prediction:,.2f}")