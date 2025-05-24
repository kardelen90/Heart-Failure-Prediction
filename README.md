# Kalp Hastalığı Tahmini

Bu proje, Makine Öğrenmesi Bootcamp kapsamında gerçekleştirdiğim bir çalışmadır. Amacım, çeşitli sağlık verilerine bakarak bir bireyin kalp hastalığı riski taşıyıp taşımadığını tahmin eden bir model geliştirmekti.

## Kullandığım Veri Seti

- Veri adı: heart.csv
- Satır sayısı: 918
- Sütunlar: yaş, cinsiyet, göğüs ağrısı tipi, kolesterol, EKG, maksimum nabız gibi sağlıkla ilgili bilgiler
- Hedef değişken: `HeartDisease` (0: sağlıklı, 1: hastalık var)

##  Neler Yaptım?

1. Veriyi inceledim, eksik değer kontrolü ve sınıf dağılımı yaptım
2. Sayısal değişkenler arasında korelasyonlara baktım
3. Kategorik değişkenleri `get_dummies` ile sayısala çevirdim
4. `StandardScaler` ile veriyi ölçeklendirdim
5. Veriyi eğitim ve test olarak ayırdım (%80/%20)
6. Logistic Regression ve Random Forest ile modeller kurdum
7. Modelleri karşılaştırıp en iyi sonucu Random Forest verdi
8. GridSearchCV ile en iyi parametreleri buldum

##  Web Uygulaması (Streamlit)

Streamlit kullanarak kullanıcıdan yaş, kolesterol, EKG gibi bilgileri alıp tahmin yapan basit bir arayüz geliştirdim. Modelin eğitildiği özelliklerle aynı yapıda olacak şekilde verileri dönüştürüp sonuçları ekrana yazdırdım.

Uygulamayı başlatmak için:
```bash
streamlit run app.py
