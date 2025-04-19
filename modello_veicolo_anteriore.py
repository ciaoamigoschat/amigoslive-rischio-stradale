# modello_veicolo_anteriore.py
# Simulazione di previsione comportamento veicolo anteriore usando LSTM

import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical

# === 1. Simulazione dataset ===
np.random.seed(42)
n_samples = 500

# Simulazione dati temporali
sequenze = []
etichette = []
azioni = ['mantenimento', 'frenata', 'cambio_corsia']

for _ in range(n_samples):
    # 20 frame da 0.5s ciascuno = 10s di osservazione
    distanza = np.clip(np.random.normal(15, 5, 20), 2, 30)  # in metri
    velocita_rel = np.clip(np.random.normal(-10, 4, 20), -30, 5)  # in km/h
    traiettoria = np.random.choice([0, 1, 2], 20)  # costante, instabile, deviazione
    sequenza = np.stack([distanza, velocita_rel, traiettoria], axis=1)
    sequenze.append(sequenza)
    etichette.append(np.random.choice(nazioni, p=[0.6, 0.25, 0.15]))

X = np.array(sequenze)
y = np.array(etichette)

# === 2. Encoding etichette ===
le = LabelEncoder()
y_encoded = le.fit_transform(y)
y_categorical = to_categorical(y_encoded)

# === 3. Normalizzazione input ===
scaler = MinMaxScaler()
X_reshaped = X.reshape(-1, 3)
X_scaled = scaler.fit_transform(X_reshaped).reshape(n_samples, 20, 3)

# === 4. Train/test split ===
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_categorical, test_size=0.2, random_state=42)

# === 5. Costruzione modello LSTM ===
model = Sequential()
model.add(LSTM(64, input_shape=(20, 3)))
model.add(Dense(32, activation='relu'))
model.add(Dense(3, activation='softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# === 6. Addestramento ===
model.fit(X_train, y_train, epochs=20, batch_size=16, validation_data=(X_test, y_test))

# === 7. Valutazione ===
loss, accuracy = model.evaluate(X_test, y_test)
print(f"\n✅ Accuratezza su test set: {accuracy:.2f}")

# === 8. Salvataggio modello ===
model.save("modello_comportamento_anteriore.h5")
print("📁 Modello salvato come 'modello_comportamento_anteriore.h5'")
