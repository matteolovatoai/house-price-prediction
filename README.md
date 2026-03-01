# 🏠 House Price Prediction Project

Questo progetto implementa una soluzione end-to-end di Machine Learning per la stima dei prezzi immobiliari. Partendo da un dataset reale, ho sviluppato una pipeline che include l'analisi esplorativa (EDA), il preprocessing dei dati e la creazione di un'interfaccia interattiva per l'utente finale.

## ✅ Stato del Progetto
**Completato**
![Status](https://img.shields.io/badge/status-completed-brightgreen)

## 🚀 Live Demo
Puoi testare l'applicazione direttamente nel browser qui:  
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://matteolovatoai-house-price-prediction.streamlit.app/)

## 📈 Risultati del Modello
Grazie a un'accurata fase di **Feature Engineering** e **Data Cleaning**, le performance del modello di regressione hanno registrato un incremento significativo:
- **Baseline R²:** 0.43
- **Final R²:** **0.70** (+62% di accuratezza)

> **Key Insight:** Il miglioramento è stato ottenuto gestendo 7 variabili categoriche tramite mappatura ordinale/binaria e filtrando gli outlier (proprietà con prezzo > 10M), dimostrando che la qualità del dato è cruciale quanto la scelta dell'algoritmo.

## 🛠️ Tech Stack & Requisiti
- **Linguaggio:** Python 3.12+ (Sviluppato su MacBook Apple Silicon)
- **Librerie Core:**
  - `Pandas` & `NumPy`: Manipolazione dati.
  - `Scikit-Learn`: Modellazione e metriche.
  - `Joblib`: Serializzazione del modello (`.pkl`).
  - `Streamlit`: Web App per l'inferenza interattiva.
  - `Pathlib`: Gestione robusta dei percorsi cross-platform.

## 📂 Struttura della Repository
```text
├── data/               # Dataset Housing.csv (gestito tramite .gitignore)
├── notebooks/          # Analisi esplorativa e training (.ipynb)
├── models/             # Modello serializzato (house_price_model.pkl)
├── main.py             # Script di inferenza via terminale
├── main_visual.py      # App interattiva (Streamlit)
├── requirements.txt    # Lista dipendenze pulita
├── .gitignore          # Esclusione file di sistema e dati pesanti
└── README.md           # Documentazione del progetto
```
## 📂 Dataset
Il progetto utilizza il dataset [Kaggle - Housing Prices](https://www.kaggle.com/datasets/yasserh/housing-prices-dataset).

**Istruzioni:** per usare i notebooks
1. Scarica il file `Housing.csv` dal link sopra.
2. Crea una cartella `data/` nella root del progetto.
3. Inserisci il file csv nella cartella `data/`.
4. `pip install -r requirements_notebooks.txt`

## 🛠️ Installazione
Assicurati di avere Python installato.  
Clona la repository e installa le dipendenze:

```bash
git clone https://github.com/matteolovato-AI/house-price-prediction.git
cd house-price-prediction
pip install -r requirements.txt
```

## 🚀 Guida Rapida
1. **Installazione**  
Clona la repository e configura l'ambiente:

```bash
git clone [https://github.com/matteolovato-AI/house-price-prediction.git](https://github.com/matteolovato-AI/house-price-prediction.git)
cd house-price-prediction
pip install -r requirements.txt
```

2. **Esecuzione Inferenza (Terminale)**  
Per testare il modello con un input simulato direttamente da riga di comando:

```bash
python main.py
```

3. **Web App Interattiva (Streamlit)**  
Per lanciare l'interfaccia grafica e inserire i parametri della casa manualmente:

```bash
streamlit run main_visual.py
```

## ⚙️ Dettagli Tecnici
**Preprocessing:** La pipeline di input gestisce automaticamente la conversione di 7 variabili categoriche (es. mainroad, airconditioning, furnishingstatus) in formato numerico prima di alimentare il modello.

**Portabilità:** I percorsi dei file sono gestiti con pathlib per garantire il funzionamento dello script su diversi sistemi operativi senza modifiche manuali.

**Data Persistence:** Il modello è salvato separatamente dal codice tramite joblib per permettere un caricamento rapido senza dover ri-addestrare l'algoritmo.

---

**Sviluppato da Matteo Lovato** | *Studente ITS - Specializzazione AI*
