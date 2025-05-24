# Heart-Failure-Prediction

Bu proje, sağlık verilerine dayanarak kalp hastalığı riskini tahmin etmek amacıyla geliştirilmiştir. Kullanıcıdan alınan bilgilerle makine öğrenmesi modeli, kalp hastalığı olasılığını % olarak tahmin eder.

## 📊 Kullanılan Veri Seti
- Kaynak: Kaggle
- Kayıt sayısı: 918
- Özellik sayısı: 12 (yaş, cinsiyet, kolesterol, EKG sonuçları vb.)

## 🔍 Kullanılan Yöntemler
- Exploratory Data Analysis (EDA)
- Veri Ön İşleme
- One-Hot Encoding
- Modelleme: 
  - Logistic Regression
  - Random Forest (final model)
- Model Değerlendirme:
  - Accuracy
  - ROC AUC
  - Confusion Matrix

## 🧠 En Başarılı Model
- 🎯 Random Forest (max_depth=5, n_estimators=50)
- Accuracy: %87
- ROC AUC: 0.86

## 🖥️ Web Arayüz (Streamlit)
Streamlit ile oluşturulan kullanıcı arayüzünde kullanıcılar:
- Yaş, cinsiyet, kolesterol vb. bilgileri girerek
- Anlık kalp hastalığı riski tahmini alabilir

### Başlatmak için:
```bash
streamlit run app.py
