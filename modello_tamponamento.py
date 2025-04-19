# modello_tamponamento.py
# Modello predittivo simulato per il rischio di tamponamento

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import joblib

# === 1. Simulazione dati ===
np.random.seed(42)
n_samples = 1000

# Variabili simulate
# distanza [m], velocità relativa [km/h], frenata_dietro [0=no, 1=sì]
distanza = np.random.uniform(2, 20, n_samples)
vel_rel = np.random.uniform(0, 40, n_samples)
frenata_dietro = np.random.choice([0, 1], n_samples, p=[0.7, 0.3])

# Regola per rischio (etichetta): 1 = rischio tamponamento
rischio = ((distanza < 5) & (vel_rel > 20) & (frenata_dietro == 0)).astype(int)

# Costruzione DataFrame
data = pd.DataFrame({
    'distanza': distanza,
    'vel_rel': vel_rel,
    'frenata_dietro': frenata_dietro,
    'rischio_tamponamento': rischio
})

# === 2. Split train/test ===
X = data[['distanza', 'vel_rel', 'frenata_dietro']]
y = data['rischio_tamponamento']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# === 3. Modello Random Forest ===
model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
model.fit(X_train, y_train)

# === 4. Valutazione ===
y_pred = model.predict(X_test)
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("\nMatrice di Confusione:")
print(confusion_matrix(y_test, y_pred))

# === 5. Salvataggio del modello ===
joblib.dump(model, "modello_tamponamento.pkl")
print("\n✅ Modello salvato come 'modello_tamponamento.pkl'")
