import pandas as pd
import numpy as np
import re

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout

# -----------------------------
# LOAD DATA
# -----------------------------
print("Loading dataset...")
df = pd.read_csv("india-news-headlines.csv")

# Reduce size (IMPORTANT for laptop)
df = df.sample(30000, random_state=42)

# -----------------------------
# CREATE LABELS (FAKE LOGIC)
# -----------------------------
def create_label(text):
    text = text.lower()
    if any(word in text for word in ["kill", "attack", "scam", "fraud"]):
        return 1
    return 0

df['label'] = df['headline_text'].astype(str).apply(create_label)

# -----------------------------
# CLEAN TEXT
# -----------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z ]', '', text)
    return text

df['headline_text'] = df['headline_text'].apply(clean_text)

# -----------------------------
# SPLIT DATA
# -----------------------------
X = df['headline_text']
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# TOKENIZATION
# -----------------------------
vocab_size = 8000
max_len = 80

tokenizer = Tokenizer(num_words=vocab_size, oov_token="<OOV>")
tokenizer.fit_on_texts(X_train)

X_train_seq = tokenizer.texts_to_sequences(X_train)
X_test_seq = tokenizer.texts_to_sequences(X_test)

X_train_pad = pad_sequences(X_train_seq, maxlen=max_len)
X_test_pad = pad_sequences(X_test_seq, maxlen=max_len)

# -----------------------------
# MODEL
# -----------------------------
print("Building model...")

model = Sequential([
    Embedding(vocab_size, 64, input_length=max_len),
    LSTM(64),
    Dropout(0.4),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(
    loss='binary_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

model.summary()

# -----------------------------
# TRAIN
# -----------------------------
print("Training...")
model.fit(
    X_train_pad, y_train,
    epochs=3,
    batch_size=32,
    validation_data=(X_test_pad, y_test),
    verbose=1
)

# -----------------------------
# EVALUATE
# -----------------------------
print("Evaluating...")
preds = (model.predict(X_test_pad) > 0.5).astype(int)

print(classification_report(y_test, preds))

# -----------------------------
# PREDICT FUNCTION
# -----------------------------
def predict_news(text):
    text = clean_text(text)
    seq = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(seq, maxlen=max_len)

    pred = model.predict(padded)[0][0]
    return "Fake" if pred > 0.5 else "Real"

# -----------------------------
# TEST
# -----------------------------
while True:
    user_input = input("\nEnter news headline (or 'exit'): ")
    if user_input.lower() == "exit":
        break

    print("Prediction:", predict_news(user_input))