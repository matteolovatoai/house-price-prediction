from pathlib import Path
import pandas as pd
import joblib

HOME_DIR = Path(__file__).parent
MODEL_PATH = HOME_DIR / "models" / "house_price_model.pkl"

def pulire_input(input):
    df = pd.DataFrame([input])
    
    trasformazione_binaria = {
    'yes': 1,
    'no': 0,
    }
    # hanno un ordinamento furnished > semi-furnished > unfurnished
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

if not MODEL_PATH.exists():
    raise FileNotFoundError(f"❌ File non trovato {MODEL_PATH}")
else:
    model = joblib.load(MODEL_PATH)
    print("-"*30)
    print("✅ Modello caricato")
    print("-"*30)
    print("\nInserisci i dati della casa che vuoi analizzare:\n")
    print("-"*30)
    user_input = {}
    # verificare che l'utente inserisca effettivamente un numero
    user_input['area'] = int(input("L'area della casa: "))
    user_input['bedrooms'] = int(input("Numero di camere da letto: "))
    user_input['bathrooms'] = int(input("Numero di bagni: "))
    user_input['stories'] = int(input("Quanti piani ha la casa? "))
    user_input['mainroad'] = "yes" if input("La proprietà affaccia sulla strada principale? (y/n): ") == "y" else "no"
    user_input['guestroom'] = "yes" if input("C'è la stanza degli ospiti? (y/n): ") == "y" else "no"
    user_input['basement'] = "yes" if input("C'è il seminterrato? (y/n): ") == "y" else "no"
    user_input['hotwaterheating'] = "yes" if input("Il riscaldamento è funzionante? (y/n): ") == "y" else "no"
    user_input['airconditioning'] = "yes" if input("È presente un impianto di climatizzazione? (y/n): ") == "y" else "no"
    user_input['parking'] = int(input("Quanti posti auto? "))
    user_input['prefarea'] = "yes" if input("Si trova in una zona prestigiosa? (y/n): ") == "y" else "no"
    print("furnished/semi-furnished/unfurnished: ")
    furnishingstatus = input("stato dell'arredamento (f/s/u): ")
    user_input['furnishingstatus'] = "furnished" if furnishingstatus == "f" else "semi-furnished" if furnishingstatus == "s" else "unfurnished"
    print("-"*30)
    print("Elaboro l'input")
    df_user_input = pulire_input(user_input)
    print("✅ Dati validi!")
    print("-"*30)
    print("\n⚙️ Calcolo in corso...")
    previsione = model.predict(df_user_input)[0]
    print("✅ Calcolo effettuato con successo!\n")
    print("-"*30)
    print(f"Previsione del prezzo: {previsione:.2f}")