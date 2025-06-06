# -*- coding: utf-8 -*-
"""Predictive Analytics.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cvZsdtt4SUcBKDE-cNINsiczfs65OJCi

# **1. Import library**
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix
from imblearn.over_sampling import RandomOverSampler

"""# **2. Data Understanding**

## **2.1 Data Loading**

Tahap Data Loading bertujuan untuk memuat dataset yang akan digunakan agar lebih mudah dianalisis. Dataset saya simpan di Google Drive, sehingga perlu menghubungkan Google Drive ke Colab terlebih dahulu. Setelah itu dataset dibaca dengan menggunakan *library* pandas dan ditampilkan 5 baris pertama.
"""

# Connect google drive
from google.colab import drive
drive.mount('/content/drive')

# Membaca dataset
data = pd.read_csv("/content/drive/MyDrive/Dataset/Crop and fertilizer dataset.csv")
data.head()

"""## **2.2 Exploratory Data Analysis (EDA)**

### 2.2.1 Pengecekan Informasi Umum Data
"""

# Menghapus kolom tidak relevan
data = data.drop(columns=['District_Name', 'Link'])

"""Dikarenakan kolom 'District_Name' dan 'Link' tidak relevan untuk analisis dan tidak mempengaruhi model, maka dilakukan penghapusan kedua kolom tersebut."""

# Cek dimensi data
data.shape

# Cek info data
data.info()

# Mendefinisikan fitur numerik dan kategorikal
numerical_features = ['Nitrogen', 'Phosphorus', 'Potassium', 'pH', 'Rainfall', 'Temperature']
categorical_features = ['Soil_color', 'Crop', 'Fertilizer']

# Cek nilai unik pada fitur kategorikal
print("Fertilizer unik: ", data['Fertilizer'].unique())
print("Crop unik: ", data['Crop'].unique())
print("Soil color unik: ", data['Soil_color'].unique())

"""Dilakukan pengecekan nilai unik pada masing-masing fitur kategorik untuk mempermudah analisis"""

# Cek statistik deskriptif data
data.describe()

"""Dataset tersebut menunjukkan kondisi agrikultur yang cukup beragam.

### 2.2.2 Pengecekan Missing Value dan Duplikat
"""

# Cek nilai null
data.isnull().sum()

# Cek nilai NaN
data.isna().sum()

# Cek data duplikat
print("Jumlah data duplikat: ", data.duplicated().sum())

"""Data sudah bersih, tidak ada missing value maupun duplikat

### 2.2.3 Pengecekan Outlier
"""

# Boxplot awal untuk melihat outlier
plt.figure(figsize=(12, 8))
sns.boxplot(data=data[numerical_features])
plt.title("Boxplot untuk Semua Variabel")
plt.xticks(rotation=45)
plt.show()

"""Pada visualisasi tersebut outlier tidak terlihat jelas dikarenakan rentang data yang tidak sama antar variabel, sehingga perlu dilakukan normalisasi terlebih dahulu"""

# Normalisasi fitur numerik dengan MinMaxScaler
scaler = MinMaxScaler()
data2 = scaler.fit_transform(data[numerical_features])
data2 = pd.DataFrame(data2, columns=numerical_features)

# Gabungkan kembali hasil normalisasi dengan fitur kategorikal
data3 = pd.concat([data2, data[categorical_features].reset_index(drop=True)], axis=1)
data3.head()

# Boxplot setelah normalisasi
plt.figure(figsize=(12, 8))
sns.boxplot(data=data3)
plt.title("Boxplot untuk Semua Variabel (Normalized)")
plt.xticks(rotation=45)
plt.show()

"""Skala data sudah seragam, sekarang outlier terlihat jelas pada beberapa variabel sehingga perlu ditangani dengan teknik tertentu

### 2.2.4 Analisis Univariate
"""

num_features = len(categorical_features)

fig, axes = plt.subplots(1, num_features, figsize=(8 * num_features, 5), sharey=True)

if num_features == 1:
    axes = [axes]

for i, feature in enumerate(categorical_features):
    count = data3[feature].value_counts()
    percent = 100 * data3[feature].value_counts(normalize=True)
    df = pd.DataFrame({'jumlah sampel': count, 'persentase': percent.round(1)})

    print(f"Analisis Univariate untuk Fitur: {feature}")
    print(df)

    count.plot(kind='bar', ax=axes[i], color='skyblue')
    axes[i].set_title(f"Distribusi {feature}")
    axes[i].set_ylabel("Jumlah Sampel")
    axes[i].tick_params(axis='x', rotation=45)

plt.tight_layout()

plt.show()

"""Distribusi data yang ada sangat beragam dan terdapat perbedaan yang signifikan terhadap kelas mayoritas dan minoritas sehingga perlu dilakukan oversampling

### 2.2.5 Pengecekan Correlation Matrix
"""

# Cek data yang sudah bersih
data3.head()

# Correlation matrix fitur numerik
plt.figure(figsize=(10, 8))
correlation_matrix = data3[numerical_features].corr().round(2)
sns.heatmap(data=correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, fmt=".2f", annot_kws={"size": 10})
plt.title("Correlation Matrix Fitur Numerik", size=20, pad=20)
plt.xlabel("Fitur Numerik", fontsize=14)
plt.ylabel("Fitur Numerik", fontsize=14)
plt.tight_layout()

"""# **3. Data Preparation**

## **3.1 Penanganan Outlier**
"""

# Penanganan outlier menggunakan teknik capping
data4 = data2.copy()
for col in numerical_features:
    Q1 = data4[col].quantile(0.25)
    Q3 = data4[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR
    data4[col] = data4[col].apply(lambda x: lower_limit if x < lower_limit else upper_limit if x > upper_limit else x)

# Boxplot hasil penanganan outlier
plt.figure(figsize=(12, 8))
sns.boxplot(data=data4)
plt.title("Boxplot untuk Semua Variabel (Handled Outlier)")
plt.xticks(rotation=45)
plt.show()

"""Setelah diterapkan teknik capping, pada boxplot terlihat tidak ada lagi outlier pada setiap variabel

## **3.2 Encoding**

Encoding dilakukan agar data dapat diproses oleh model machine learning, sehingga perlu mengubah fitur kategorik menjadi fitur numerik terlebih dahulu

### 3.2.1 Label Encoding
"""

# Gabungkan data clean dengan kolom kategorik
data5 = pd.concat([data4, data[categorical_features].reset_index(drop=True)], axis=1)
data5.head()

# Pisahkan fitur (X) dan target label (y)
X = data5.iloc[:, :-1]  # Cleaned data
y = data5[['Fertilizer']]  # Target output

# Buat encoder untuk setiap kolom
le_soil = LabelEncoder()
le_crop = LabelEncoder()
le_fert = LabelEncoder()

# Fit dan encode kolom
le_soil.fit(data5['Soil_color'])
data5['Soil_color'] = le_soil.transform(data5['Soil_color'])

le_crop.fit(data['Crop'])
data5['Crop'] = le_crop.transform(data5['Crop'])

le_fert.fit(data['Fertilizer'])
y['Fertilizer'] = le_fert.transform(y['Fertilizer'])

"""### 3.2.2 One-Hot Encoding"""

# Mendefinisikan fitur numerik dan kategorikal
numerical_cols = ['Nitrogen', 'Phosphorus', 'Potassium', 'pH', 'Rainfall', 'Temperature']
categorical_cols = ['Soil_color', 'Crop']

# Data training
X = pd.get_dummies(X, columns=categorical_cols, drop_first=True)

# Simpan X.columns dan urutannya
X_columns = X.columns

X.head()

"""## **3.3 Splitting dan Oversampling**

### 3.3.1 Splitting Data
"""

# Split data dengan rasio 80:20
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

"""- 80% data untuk pelatihan (X_train, y_train)
- 20% data untuk pengujian (X_test, y_test)

### 3.3.2 Oversampling Data
"""

# Oversampling hanya untuk data training
X_train_resampled, y_train_resampled = RandomOverSampler(random_state=42).fit_resample(X_train, y_train)

# Buat salinan agar tidak merusak data asli
y_train_resampled_decoded = le_fert.inverse_transform(y_train_resampled)

# Ubah ke Series agar bisa pakai value_counts()
y_train_resampled_decoded = pd.Series(y_train_resampled_decoded, name='Fertilizer')

# Analisis univariate
count = y_train_resampled_decoded.value_counts()
percent = 100 * y_train_resampled_decoded.value_counts(normalize=True)
df = pd.DataFrame({'jumlah sampel': count, 'persentase': percent.round(1)})
print("Analisis Univariate untuk Fitur: Fertilizer")
print(df)

count.plot(kind='bar', title="Distribusi Fertilizer", color='skyblue', figsize=(8, 5))
plt.ylabel("Jumlah Sampel")
plt.show()

"""Setelah oversampling, data menjadi seragam dan tidak ada data yang lebih dominan.

# **4. Modeling**

## **4.1 Random Forest Base Model**
"""

# RF Base Model
rf_model_base = RandomForestClassifier(random_state=42)
rf_model_base.fit(X_train_resampled, y_train_resampled)

# Prediksi training
y_train_acc_base = rf_model_base.predict(X_train_resampled)
y_train_acc_base_decoded = le_fert.inverse_transform(y_train_acc_base)
y_train_true_decoded = le_fert.inverse_transform(y_train_resampled.values.ravel())

# Prediksi testing
y_pred_base = rf_model_base.predict(X_test)
y_pred_base_decoded = le_fert.inverse_transform(y_pred_base)
y_test_decoded = le_fert.inverse_transform(y_test.values.ravel())

"""## **4.2 Random Forest Hyperparameter Tunning**"""

# RF Hyperparameter Tunning
rf_model_tunned = RandomForestClassifier(
        max_depth=15,          # Batasi kedalaman pohon
        max_features='sqrt',   # Kurangi fitur yang digunakan di setiap split
        min_samples_split=5,   # Minimum sampel untuk membagi node
        random_state=42
    )

rf_model_tunned.fit(X_train_resampled, y_train_resampled)

# Prediksi training
y_train_acc_tunned = rf_model_tunned.predict(X_train_resampled)
y_train_acc_tunned_decoded = le_fert.inverse_transform(y_train_acc_tunned)
y_train_true_decoded = le_fert.inverse_transform(y_train_resampled.values.ravel())

# Prediksi testing
y_pred_tunned = rf_model_tunned.predict(X_test)
y_pred_tunned_decoded = le_fert.inverse_transform(y_pred_tunned)
y_test_decoded = le_fert.inverse_transform(y_test.values.ravel())

"""# **5. Model Evaluation**

## **5.1 Confusion Matrix**
"""

# Confusion Matrix untuk prediksi Fertilizer (Base Model)
cm_fertilizer = confusion_matrix(y_test_decoded, y_pred_base_decoded)

plt.figure(figsize=(6, 4))
sns.heatmap(cm_fertilizer, annot=True, fmt='d', cmap='Blues',
            xticklabels=np.unique(y_test_decoded),
            yticklabels=np.unique(y_test_decoded))
plt.xlabel('Predicted Fertilizer')
plt.ylabel('True Fertilizer')
plt.title('Confusion Matrix (Base Model)')
plt.show()

# Confusion Matrix untuk prediksi Fertilizer (Tunned)
cm_fertilizer = confusion_matrix(y_test_decoded, y_pred_tunned_decoded)

plt.figure(figsize=(6, 4))
sns.heatmap(cm_fertilizer, annot=True, fmt='d', cmap='Blues',
            xticklabels=np.unique(y_test_decoded),
            yticklabels=np.unique(y_test_decoded))
plt.xlabel('Predicted Fertilizer')
plt.ylabel('True Fertilizer')
plt.title('Confusion Matrix (Tunned)')
plt.show()

"""## **5.2 Matriks Evaluasi**"""

def evaluate_single_label(y_true, y_pred):
    return {
        'Accuracy': accuracy_score(y_true, y_pred),
        'Precision': precision_score(y_true, y_pred, average='weighted', zero_division=0),
        'Recall': recall_score(y_true, y_pred, average='weighted', zero_division=0),
        'F1-Score': f1_score(y_true, y_pred, average='weighted', zero_division=0)
    }

# Evaluasi training
train_results_rf_base = evaluate_single_label(y_train_true_decoded, y_train_acc_base_decoded)
train_results_rf_tunned = evaluate_single_label(y_train_true_decoded, y_train_acc_tunned_decoded)

# Evaluasi testing
results_rf_base = evaluate_single_label(y_test_decoded, y_pred_base_decoded)
results_rf_tunned = evaluate_single_label(y_test_decoded, y_pred_tunned_decoded)

# Buat DataFrame rekap evaluasi untuk satu target label saja
rows = []
for model_name, result_test, result_train in [
    ('Random Forest (Base)', results_rf_base, train_results_rf_base),
    ('Random Forest (Tuned)', results_rf_tunned, train_results_rf_tunned)
]:
    rows.append({
        'Model': model_name,
        'Train Accuracy': result_train['Accuracy'],
        'Test Accuracy': result_test['Accuracy'],
        'Precision': result_test['Precision'],
        'Recall': result_test['Recall'],
        'F1-Score': result_test['F1-Score']
    })

summary_df = pd.DataFrame(rows)
print(summary_df)