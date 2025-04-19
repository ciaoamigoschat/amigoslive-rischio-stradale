# modello_incidenti.py
# Questo script rappresenta solo una parte dell'algoritmo completo utilizzato per anticipare il comportamento di altri guidatori,
# simulare scenari di rischio stradale e classificare il livello di pericolosità in base alla fascia oraria e alle variabili comportamentali.
# Modello predittivo per la classificazione del rischio di incidenti stradali
# Autore: Pippo Messina – HelpSoftware

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, roc_auc_score
import joblib
import os

# === 1. Caricamento del dataset ===
DATASET_PATH = "dati_simulati.csv"

if not os.path.exists(DATASET_PATH):
    raise FileNotFoundError(f"⚠️ File '{DATASET_PATH}' non trovato. Assicurati che il dataset esista nella directory.")

print("📥 Caricamento del dataset...")
df = pd.read_csv(DATASET_PATH)

# === 2. Visualizzazione iniziale ===
print("\n📄 Primi 5 record del dataset:")
print(df.head())

# === 3. Definizione delle feature e del target ===
features = [
    "ora", "giorno_settimana", "frenate_brusche",
    "cambi_corsia", "violazioni_stop", "traffico",
    "distrazione", "alterazione"
]
target = "incidente"

# === 4. Funzione per addestrare e salvare un modello per ogni fascia oraria ===
def train_and_save_model(data, fascia, model_type="random_forest"):
    print(f"\n🚗 Addestramento modello per fascia oraria: {fascia.upper()}")
    X = data[features]
    y = data[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    if model_type == "random_forest":
        model = RandomForestClassifier(n_estimators=100, max_depth=6, random_state=42)
    elif model_type == "gradient_boosting":
        model = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=5, random_state=42)
    else:
        raise ValueError("Tipo di modello non supportato")

    # Addestramento
    model.fit(X_train, y_train)

    # Valutazione
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    print("✅ Accuracy:", accuracy_score(y_test, y_pred))
    print("✅ ROC AUC:", roc_auc_score(y_test, y_prob))
    print("\n📊 Classification Report:")
    print(classification_report(y_test, y_pred))
    print("\n🧮 Matrice di Confusione:")
    print(confusion_matrix(y_test, y_pred))

    # Salvataggio del modello
    model_name = f"modello_incidenti_{fascia}.pkl"
    joblib.dump(model, model_name)
    print(f"💾 Modello salvato come '{model_name}'")

# === 5. Esecuzione per ciascuna fascia oraria ===
fasce_orarie = ["mattina", "pre-sera", "sabato_sera"]
modelli_creati = 0

for fascia in fasce_orarie:
    sottoinsieme = df[df["fascia_oraria"] == fascia]
    if not sottoinsieme.empty:
        train_and_save_model(sottoinsieme, fascia, model_type="random_forest")
        modelli_creati += 1
    else:
        print(f"⚠️ Nessun dato disponibile per la fascia oraria: {fascia}")

print("\n✅ Addestramento completato per tutte le fasce orarie.")
print("📂 I modelli sono stati salvati nei rispettivi file '.pkl'.")
print("🔍 Utilizzali in fase predittiva per stimare il rischio in tempo reale o su nuovi dati campionati.")
