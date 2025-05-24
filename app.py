import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

st.set_page_config(page_title="Kalp Hastalığı Tahmini", layout="centered")
st.title("❤️ Kalp Hastalığı Tahmin Uygulaması")

# Girdi: Kullanıcı verileri 
age = st.slider("Yaş", 20, 100, 50)
sex = st.radio("Cinsiyet", ("Kadın", "Erkek"))
cp = st.selectbox("Göğüs Ağrısı Tipi", ["ASY", "NAP", "ATA", "TA"])
resting_bp = st.slider("İstirahat Kan Basıncı", 80, 200, 120)
cholesterol = st.slider("Kolesterol", 100, 600, 200)
fasting_bs = st.radio("Açlık Kan Şekeri > 120 mg/dl", ["Hayır", "Evet"])
resting_ecg = st.selectbox("EKG Sonucu", ["Normal", "ST", "LVH"])
max_hr = st.slider("Maksimum Kalp Atış Hızı", 60, 220, 150)
exercise_angina = st.radio("Egzersizle Göğüs Ağrısı", ["Evet", "Hayır"])
oldpeak = st.slider("ST Segmenti Değeri", 0.0, 6.0, 1.0)
st_slope = st.selectbox("ST Eğimi", ["Up", "Flat", "Down"])

# Veriyi dönüştür için bu kodu yazıyoruz
data = {
    'Age': age,
    'RestingBP': resting_bp,
    'Cholesterol': cholesterol,
    'FastingBS': 1 if fasting_bs == "Evet" else 0,
    'MaxHR': max_hr,
    'Oldpeak': oldpeak,
    'Sex_M': 1 if sex == "Erkek" else 0,
    'ChestPainType_ATA': int(cp == "ATA"),
    'ChestPainType_NAP': int(cp == "NAP"),
    'ChestPainType_ASY': int(cp == "ASY"),
    'ChestPainType_TA': int(cp == "TA"),
    'RestingECG_Normal': int(resting_ecg == "Normal"),
    'RestingECG_ST': int(resting_ecg == "ST"),
    'RestingECG_LVH': int(resting_ecg == "LVH"),
    'ExerciseAngina_Y': int(exercise_angina == "Evet"),
    'ST_Slope_Up': int(st_slope == "Up"),
    'ST_Slope_Flat': int(st_slope == "Flat"),
    'ST_Slope_Down': int(st_slope == "Down"),
}


# Model ve scaler oluştur
model = RandomForestClassifier(max_depth=5, n_estimators=50)
scaler = StandardScaler()

# Model eğitimi (CSV dosyasından)
df = pd.read_csv("heart.csv")
df = pd.get_dummies(df, drop_first=True)
X = df.drop("HeartDisease", axis=1)
y = df["HeartDisease"]
X_scaled = scaler.fit_transform(X)
model.fit(X_scaled, y)

# Kullanıcıdan alınan veriyi DataFrame'e çevir
X_input = pd.DataFrame([data])
X_input = X_input[X.columns]

# Tahmin
X_input_scaled = scaler.transform(X_input)
prediction = model.predict(X_input_scaled)

if st.button("Tahmin Et"):
    if prediction[0] == 1:
        st.error("⚠️ Kalp hastalığı riski mevcut!")
    else:
        st.success("✅ Kalp hastalığı riski görünmüyor.")
