# Usa un'immagine Python leggera
FROM python:3.11-slim

# Imposta la directory di lavoro nel container
WORKDIR /app

# Installa le dipendenze di sistema necessarie (opzionale ma consigliato)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copia il file dei requisiti
COPY requirements.txt .

# Installa le librerie Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia il resto del codice e il modello
COPY . .

# Espone la porta usata da Streamlit (default 8501)
EXPOSE 8501

# Comando per avviare l'app
ENTRYPOINT ["streamlit", "run", "main_visual.py", "--server.port=8501", "--server.address=0.0.0.0"]