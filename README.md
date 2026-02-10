# 🏠 House Price Prediction Project

Benvenuto in questo progetto di Machine Learning.
L'obiettivo è sviluppare un modello predittivo per stimare i prezzi immobiliari partendo da un dataset reale, applicando tecniche di Data Analysis (EDA) e algoritmi di Regressione.

## 🚧 Stato del Progetto
**Work in Progress.**  
![Python](https://img.shields.io/badge/python-3.14-blue)
![Status](https://img.shields.io/badge/status-Work_in_progress-yellow)  
Migliorando gli input con streamlit

## 🎯 Obiettivi
- [x] Setup ambiente virtuale e dipendenze
- [x] Acquisizione dataset (Housing Prices)
- [x] Analisi Esplorativa dei Dati (Notebooks)
- [x] Pulizia dati e Feature Engineering
- [x] Training del modello (Linear Regression)
- [x] Valutazione metriche (MSE, R2 Score)

## 🛠️ Tech Stack
- **Python 3.14**
- **Pandas:** Manipolazione dati
- **Matplotlib:** Visualizzazione dati
- **Scikit-Learn:** Modellazione AI
- **Jupyter:** Prototipazione rapida
- **Streamlit:** App interattiva

## 📂 Struttura della Repository
```text
├── data/               # Dataset (ignorato da git per dimensione)
├── notebooks/          # Analisi esplorativa (.ipynb)
├── models/             # File del modello (.pkl)
├── main.py             # Script principale
├── main_visual.py      # App interattiva
├── .gitignore          # File esclusi dal versionamento
├── requirements.txt    # Lista dipendenze
└── README.md           # Documentazione
```
## 📂 Dataset
Il progetto utilizza il dataset [Kaggle - Housing Prices](https://www.kaggle.com/datasets/yasserh/housing-prices-dataset).

**Istruzioni:** per usare i notebooks
1. Scarica il file `Housing.csv` dal link sopra.
2. Crea una cartella `data/` nella root del progetto.
3. Inserisci il file csv nella cartella `data/`.
4. `pip install -r requirements_notebooks.txt`

## 🛠️ Installazione
Assicurati di avere Python installato. Clona la repository e installa le dipendenze:

```bash
git clone https://github.com/matteolovato-AI/house-price-prediction.git
cd house-price-prediction
pip install -r requirements.txt
```

## 🚀 Run
Per lo script con input da terminale
```bash
python main.py 
```
Per usare l'applicazione interattiva
```bash
streamlit run main_visual.py
```
