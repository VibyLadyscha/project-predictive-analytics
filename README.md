# Laporan Proyek Machine Learning - Viby Ladyscha Yalasena Winarno

## Domain Proyek

Sumber daya alam terdiri dari berbagai sektor penting, seperti kelautan, pertambangan, dan pertanian. Di antara sektor-sektor tersebut, pertanian memegang peranan penting dalam mendukung ketahanan pangan dan perekonomian nasional. Seiring berkembangnya teknologi, sektor ini turut mengalami transformasi melalui penerapan pertanian presisi, yaitu pendekatan yang mengandalkan data untuk mengoptimalkan penggunaan input sesuai kebutuhan spesifik tanaman. Tujuan dari pertanian presisi adalah meningkatkan efisiensi, mengurangi biaya produksi, serta menghasilkan panen yang lebih berkualitas. Implementasi pertanian presisi dapat dilakukan dari level sederhana hingga kompleks, bergantung pada tingkat akurasi yang diinginkan dan skala investasi teknologi yang digunakan [[1](https://repository.pertanian.go.id/handle/123456789/13673)].

Salah satu penerapan penting dari konsep ini adalah dalam menentukan jenis pupuk yang tepat, disesuaikan dengan karakteristik tanaman dan kondisi lingkungan. Pemilihan pupuk yang akurat berperan besar dalam meningkatkan produktivitas pertanian. Namun, kenyataannya banyak petani masih menghadapi kesulitan dalam menentukan pupuk yang optimal, karena proses identifikasi manual terhadap komposisi pupuk dan kondisi lahan memerlukan waktu dan pengetahuan teknis yang cukup tinggi [[2](https://ojs.udb.ac.id/index.php/Senatib/article/view/1922)]. Faktor-faktor seperti pH tanah, suhu, kelembaban, dan curah hujan menjadi penentu penting dalam pemilihan jenis pupuk [[3](https://journal.uniga.ac.id/index.php/JPPB/article/view/959)].  Oleh karena itu, dibutuhkan sebuah sistem rekomendasi pupuk berbasis *predictive analysis* yang mampu mengolah data lingkungan secara otomatis untuk memberikan rekomendasi pupuk yang optimal. Dengan menggunakan pendekatan tersebut, sistem ini dapat membantu petani dalam mengambil keputusan secara cepat dan akurat, meningkatkan efisiensi pemupukan, serta berkontribusi pada peningkatan produktivitas hasil pertanian.

## Business Understanding

Penggunaan pupuk yang tepat menjadi faktor kunci dalam meningkatkan produktivitas pertanian khususnya dalam konteks pertanian presisi. Namun, banyak petani masih mengalami kesulitan dalam menentukan jenis pupuk yang sesuai dengan kondisi lahan mereka secara cepat dan akurat. Oleh karena itu, dibutuhkan sistem berbasis data yang mampu memberikan rekomendasi jenis pupuk yang optimal secara otomatis. Proyek ini bertujuan untuk membangun sistem prediksi jenis pupuk menggunakan algoritma *machine learning* berbasis data lingkungan seperti pH tanah, suhu, kelembaban, dan curah hujan. Dengan pendekatan tersebut, diharapkan sistem ini dapat membantu petani dalam pengambilan keputusan yang lebih tepat, efisien, dan berbasis data.

### Problem Statements

Berdasarkan permasalahan yang diuraikan dalam latar belakang, proyek ini bertujuan menjawab beberapa pertanyaan berikut:
1. Bagaimana membangun model prediksi yang mampu memprediksi jenis pupuk yang tepat berdasarkan fitur seperti kondisi tanah, lingkungan, dan jenis tanaman?
   - Masalah ini timbul karena pemilihan pupuk yang selama ini dilakukan secara manual memerlukan waktu, tenaga, dan pengetahuan teknis yang tidak selalu dimiliki oleh petani.
2. Bagaimana meningkatkan akurasi model prediksi pupuk menggunakan teknik *machine learning* yang tepat?
   - Model prediksi memerlukan pengolahan data dan pengaturan parameter yang optimal agar dapat memberikan hasil yang akurat.
3. Bagaimana sistem ini dapat membantu petani dalam meningkatkan efisiensi pemupukan dan produktivitas pertanian?
   - Sistem yang mampu memberikan rekomendasi pupuk secara otomatis akan mempermudah pengambilan keputusan, mengurangi kesalahan penggunaan pupuk, dan meningkatkan hasil panen.

### Goals

Untuk menjawab permasalahan yang telah dirumuskan, tujuan dari proyek ini meliputi:
1. Mengembangkan model prediksi menggunakan algoritma *machine learning* untuk memprediksi jenis pupuk berdasarkan parameter seperti kondisi tanah, lingkungan, dan jenis tanaman.
2. Meningkatkan performa model prediksi melalui teknik *oversampling* dan *hyperparameter tuning*.
3. Menyediakan solusi berbasis data yang dapat digunakan oleh petani untuk meningkatkan efisiensi pemupukan dan hasil pertanian.

### Solution statements

Untuk mencapai tujuan yang telah ditetapkan, solusi yang diusulkan dalam proyek ini adalah sebagai berikut:
1. Membangun model prediksi dengan algoritma *Random Forest* karena algoritma ini memiliki kemampuan yang baik dalam menangani fitur numerik dan non-linear serta mengurangi risiko *overfitting*. Model ini digunakan sebagai *baseline* dalam memprediksi jenis pupuk berdasarkan parameter seperti kondisi tanah, lingkungan, dan jenis tanaman.
2. Melakukan *hyperparameter tuning* terhadap model *Random Forest* seperti mengatur jumlah *estimators*, *max depth*, dan *criterion* untuk mendapatkan akurasi yang lebih optimal dibandingkan dengan model *default*. Evaluasi akan dilakukan dengan menggunakan metrik seperti *accuracy*, *precision*, *recall*, dan *F1-score*.

## Data Understanding

Pada proyek ini saya menggunakan data sekunder yang diunduh dari situs dataset *online* Kaggle dengan judul “[Crop and Fertilizer Dataset for Western Maharashtra](https://www.kaggle.com/datasets/sanchitagholap/crop-and-fertilizer-dataset-for-westernmaharashtra/data?select=Crop+and+fertilizer+dataset.csv)”. Dataset disimpan dalam file dengan format .CSV yang kemudian akan digunakan dalam proses pengolahan data. Dataset ini berisi 4.513 baris dengan 11 variabel. 

### Variabel-variabel pada dataset

| **Nama Variabel**  | **Deskripsi**                                                                 |
|--------------------|------------------------------------------------------------------------------|
| **District Name**  | Nama dari distrik-distrik yang berada di wilayah Maharashtra Barat.          |
| **Soil color**     | Warna tanah yang terdapat di distrik tertentu.                               |
| **Nitrogen**       | Nilai kandungan nitrogen dalam tanah.                                        |
| **Potassium**      | Nilai kandungan kalium (potasium) dalam tanah.                              |
| **Phosphorus**     | Nilai kandungan fosfor dalam tanah.                                          |
| **pH**             | Tingkat keasaman atau kebasaan tanah (nilai pH).                             |
| **Rainfall**       | Tingkat curah hujan di wilayah tersebut.                                     |
| **Temperature**    | Tingkat suhu rata-rata di wilayah tersebut.                                  |
| **Crop**           | Nama berbagai jenis tanaman yang dibudidayakan.                              |
| **Fertilizer**     | Nama pupuk yang sesuai untuk tanaman tertentu.                               |
| **Link**           | Tautan video YouTube (cara merawat tanaman).                                 |

Dari seluruh variabel yang ada, saya hanya menggunakan 8 variabel yang berpengaruh dalam memprediksi pupuk, antara lain:
| **Soil color**  | **Nitrogen**   |
|-----------------|----------------|
| **Potassium**   | **Phosphorus** |
| **pH**          | **Rainfall**   |
| **Temperature** | **Crop**       |

Adapun variabel yang dihapus atau tidak digunakan dalam model prediksi karena tidak relevan untuk analisis dan tidak mempengaruhi model. Variabel tersebut antara lain:
| **District Name**  | **Link**   |
|--------------------|------------|

### EDA - Pengecekan Informasi Umum Data

- Setelah dilakukan *drop*/penghapusan variabel yang tidak relevan, dataset tersebut memiliki shape `(4513, 9)` yang menunjukkan jumlah baris dan variabel yang akan digunakan.
- Tipe data pada setiap variabel cukup beragam, yaitu `int64`, `float64`, dan `object`.
- Pengecekan statistik deskriptif juga dilakukan untuk melihat variasi data dengan hasil sebagai berikut.
  
  ![statistik deskriptif](https://raw.githubusercontent.com/VibyLadyscha/project-predictive-analytics/main/img/Screenshot%202025-05-26%20080032.png
)
  Berdasarkan hasil tersebut, dapat disimpulkan bahwa dataset tersebut menunjukkan kondisi agrikultur yang cukup beragam.
- Setelah dilakukan pengecekan, dataset ini juga sudah dalam kondisi bersih yaitu tidak memiliki *missing value* maupun data duplikat.

### EDA - Pengecekan Outlier
- Pengecekan outlier dilakukan pada data numerik dengan hasil sebagai berikut.
  
  ![outlier awal](https://raw.githubusercontent.com/VibyLadyscha/project-predictive-analytics/main/img/Outlier%20Awal.png)
  Pada visualisasi tersebut outlier tidak terlihat jelas dikarenakan rentang data yang tidak sama antar variabel, sehingga perlu dilakukan normalisasi terlebih dahulu
- Setelah dilakukan normalisasi, outlier semakin terlihat dengan jelas dan kemudian dilakukan teknik *capping* untuk menangani outlier tersebut.
  
  ![outlier setelah normalisasi](https://raw.githubusercontent.com/VibyLadyscha/project-predictive-analytics/main/img/Outlier%20Setelah%20Normalisasi.png)

### EDA - Analisis Univariate

![univariate analysis](https://raw.githubusercontent.com/VibyLadyscha/project-predictive-analytics/main/img/Univariate%20Analysis.png)

Setelah dilakukan visualisasi distribusi, terlihat bahwa frekuensi setiap variabel kategorik terutama variabel target tidak seimbang, sehingga diperlukan penanganan lebih lanjut untuk menghindari bias dalam memprediksi data yang distribusi kelasnya minoritas pada model.

### EDA - Correlation Matrix

![correlation matrix](https://raw.githubusercontent.com/VibyLadyscha/project-predictive-analytics/main/img/Matrix%20Correlation.png)

## Data Preparation

### Penanganan Outlier

Outlier yamg ada dilakukan penanganan dengan teknik *capping* yaitu menggantikan nilai outlier dengan nilai *lower_limit* dan *upper_limit*. Setelah diterapkan teknik *capping*, pada boxplot terlihat tidak ada lagi outlier pada setiap variabel. Hasil dari penanganan outlier adalah sebagai berikut.

![outlier cleaned](https://raw.githubusercontent.com/VibyLadyscha/project-predictive-analytics/main/img/Outlier%20Cleaned.png)

Konsep *capping*:
- Identifikasi outlier dengan metode *Interquartile Range*, yaitu dengan menghitung selisih antara Q3 dan Q1.
- Nilai ekstrem di luar batas bawah `(Q1 - 1.5 × IQR)` dan batas atas `(Q3 + 1.5 × IQR)` dianggap outlier, lalu dilakukan capping terhadap nilai-nilai tersebut.
  - Jika x lebih kecil dari batas bawah, ganti dengan *lower_limit*, jika lebih besar dari batas atas, ganti dengan *upper_limit*.
  - Jika tidak memenuhi keduanya, maka x tetap dipertahankan.

### Encoding

Agar dapat diproses oleh model *machine learning*, perlu dilakukan perubahan variabel kategorik menjadi variabel numerik terlebih dahulu sehingga model dapat mempelajarinya dengan efektif.

1. Label Encoding
   - Pada tahap ini, dilakukan transformasi terhadap variabel kategorikal `Soil_color,` `Crop`, dan `Fertilizer` menjadi representasi numerik menggunakan teknik *Label Encoding*. Teknik ini digunakan karena beberapa algoritma *machine learning*, salah satunya *Random Forest* dapat bekerja langsung dengan data numerik.
   - *Label encoding* diperlukan agar variabel kategorikal dapat diolah dengan baik oleh model. Selain itu, encoder ini disimpan untuk proses *inverse transform* di tahap interpretasi hasil.
2. One-Hot Encoding
   - Setelah dilakukan *label encoding*, variabel kategorikal seperti `Soil_color` dan `Crop` kemudian dikonversi menjadi bentuk *one-hot encoding*. Teknik ini digunakan untuk menghindari pemodelan urutan atau hierarki yang salah pada data kategorikal.
   - *One-hot encoding* hanya diterapkan pada variabel kategorikal yang digunakan sebagai input model, bukan pada target variabel atau data uji.
      ```python
      X = pd.get_dummies(X, columns=categorical_cols, drop_first=True)
      ```
   - Penggunaan `drop_first=True` bertujuan untuk menghindari multikolinearitas dengan menghapus satu kategori sebagai referensi.

### Splitting dan Oversampling

1. Splitting Data
   - Dataset dibagi menjadi 80% data untuk pelatihan *(X_train, y_train)* dan 20% untuk pengujian *(X_test, y_test)* menggunakan `train_test_split`.
      ```python
      X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
      ```
   - Parameter `random state` di-set dengan nilai 42 untuk memastikan konsistensi terhadap hasil pembagian data.
   - Splitting diperlukan untuk menguji kemampuan generalisasi model. Data training digunakan untuk membangun model, sementara data testing digunakan untuk mengukur performa model pada data yang belum pernah dilihat.
2. Oversampling Data
   - Teknik *Random Oversampling* diterapkan pada data pelatihan (*X_train* dan *y_train*) untuk mengatasi ketidakseimbangan kelas pada variabel target `Fertilizer`.
     ```python
      X_train_resampled, y_train_resampled = RandomOverSampler(random_state=42).fit_resample(X_train, y_train)
      ```
   - Ketidakseimbangan kelas dapat menyebabkan model bias terhadap kelas mayoritas, sehingga oversampling memperbanyak sampel kelas minoritas agar model memiliki representasi yang lebih seimbang dan meningkatkan performa prediksi.
   - Proses *oversampling* hanya dilakukan pada data pelatihan untuk mencegah kebocoran data (*data leakage*) ke dalam data pengujian, sehingga evaluasi model tetap valid.

## Modeling

Pada proyek ini, modeling dilakukan menggunakan algoritma *Random Forest*. *Random Forest* adalah algoritma *machine learning ensemble* yang menggabungkan beberapa *decision tree* untuk meningkatkan akurasi prediksi. Algoritma ini bekerja dengan membuat banyak *decision tree* secara acak dan kemudian menggunakan voting untuk memprediksi kategori atau nilai data baru. Selain menguji model *baseline*, saya juga melakukan *hyperparameter tuning* pada model tersebut untuk melihat apakah akurasi yang dihasilkan lebih baik atau tidak.

1. *Random Forest Baseline*
   - Model *baseline* dibangun menggunakan parameter *default* dari algoritma *RandomForestClassifier*, dengan penambahan `random_state` untuk menjamin reprodusibilitas hasil.
     ```python
      rf_model_base = MultiOutputClassifier(RandomForestClassifier(random_state=42))
      rf_model_base.fit(X_train_resampled, y_train_resampled)
      ```
   - Kelebihan *Random Forest*:
     - Mampu menangani fitur numerik dan kategorikal dengan baik.
     - Kuat terhadap *overfitting* karena menggunakan banyak pohon keputusan.
     - Memberikan estimasi pentingnya fitur.
   - Kekurangan *Random Forest*:
     - Waktu pelatihan lebih lama dibanding model yang lebih sederhana.
     - Sulit untuk diinterpretasi karena merupakan ensemble model.

2. *Random Forest Hyperparameter Tuning*
   - Proses *hyperparameter tuning* dengan mengatur beberapa parameter penting.
    ```python
       rf_model_tunned = MultiOutputClassifier(
       RandomForestClassifier(
           max_depth=15,
           max_features='sqrt',
           min_samples_split=5,
           random_state=42
          )
       )
       rf_model_tunned.fit(X_train_resampled, y_train_resampled)
    ```
   - Penjelasan parameter yang digunakan:
      - `max_depth=15` → untuk membatasi kedalaman pohon dan mengurangi risiko *overfitting*.
      - `max_features='sqrt'` → agar setiap pohon menggunakan subset fitur secara acak.
      - `min_samples_split=5` → untuk mengontrol jumlah minimum sampel yang dibutuhkan agar sebuah node dapat di-split.
   - Model tuned diharapkan memberikan performa yang lebih baik di data pengujian karena telah disesuaikan untuk menangani kompleksitas data secara lebih optimal dibandingkan model *default*. Evaluasi dilakukan menggunakan metrik *Accuracy*, *Precision*, *Recall*, dan *F1-score* terhadap data uji untuk melihat sejauh mana tuning memberikan dampak terhadap prediksi.

## Evaluation

Metrik evaluasi yang digunakan untuk mengevaluasi model setelah dilakukan pelatihan terdiri dari *Confusion Matrix*, *Accuracy8, *Precision*, *Recall*, *F1-score*.

### Confusion Matrix

*Confusion Matrix* adalah matriks persegi berukuran N x N, dengan N merupakan jumlah kelas keluaran (*output*). Tiap baris pada matriks merepresentasikan jumlah nilai yang diprediksi dan tiap kolom merepresentasikan jumlah nilai sebenarnya. *Confusion matrix* menunjukkan performa dari model, misalnya banyak prediksi yang benar atau banyak kesalahan yang dilakukan. Banyak nilai yang ditunjukkan terbagi menjadi empat tipe:
1. *True Positive* (TP): Model memprediksi hasil positif secara benar. Hasil prediksi dan hasil sebenarnya adalah positif.
2. *False Positive* (FP): Model salah memprediksi hasil positif. Hasil prediksi bernilai positif, sedangkan hasil sebenarnya adalah negatif. Biasa disebut dengan Type I error.
3. *True Negative* (TN): Model memprediksi hasil negatif secara benar. Hasil prediksi dan hasil sebenarnya adalah negatif.
4. *False Negative* (FN): Model salah memprediksi hasil negatif. Hasil prediksi bernilai negatif, sedangkan hasil sebenarnya adalah positif. Biasa disebut dengan Type II error.

#### Interpretasi Hasil

1. *Random Forest Baseline*
   
   ![confusion matrix baseline](https://raw.githubusercontent.com/VibyLadyscha/project-predictive-analytics/main/img/)

   - Berdasarkan *confusion matrix* tersebut, secara keseluruhan model dapat memprediksi seluruh kelas dengan baik, hanya ada beberapa kelas yang salah prediksi.
   - Sebaran kelas terbanyak terdapat pada jenis pupuk `Urea`, `DAP`, `MOP`, `SSP`, `19:19:19 NPK`, dan `Magnesium Sulphate` dengan detail sebagai berikut.
     - `Urea`: 249 benar, hanya beberapa salah diprediksi ke berbagai jenis NPK, "MOP", "SSP".
     - `DAP`: 131 benar, hanya beberapa salah diprediksi sebagai "SSP" dan "Urea".
     - `MOP`: 118 benar, hanya beberapa salah diprediksi sebagai "SSP", "Sulphur", dan "Urea".
     - `SSP`: 67 benar.
     - `Magnesium Sulphate`: 43 benar.
     - `19:19:19 NPK`: 89 benar.

2. *Random Forest Hyperparameter Tuning*
   
   ![confusion matrix tuning](https://raw.githubusercontent.com/VibyLadyscha/project-predictive-analytics/main/img/)

   - Berdasarkan *confusion matrix* tersebut, secara keseluruhan model dapat memprediksi seluruh kelas dengan baik, hanya ada beberapa kelas yang salah prediksi.
   - Sebaran kelas terbanyak terdapat pada jenis pupuk `Urea`, `DAP`, `MOP`, `SSP`, `19:19:19 NPK`, dan `Magnesium Sulphate` dengan detail sebagai berikut.
     - `Urea`: 150 benar, hanya beberapa salah diprediksi ke berbagai jenis NPK, "MOP", "SSP" dan "DAP".
     - `DAP`: 93 benar, hanya beberapa salah diprediksi sebagai "SSP" dan "Urea".
     - `MOP`: 109 benar, hanya beberapa salah diprediksi sebagai "SSP", "Sulphur", dan "Urea".
     - `SSP`: 62 benar.
     - `Magnesium Sulphate`: 40 benar.
     - `19:19:19 NPK`: 90 benar.
   - Setelah dilakukan *hyperparameter tuning* justru hasil akurasi semakin turun jika dibandingkan dengan model *baseline*.

### Accuracy

*Accuracy* atau akurasi adalah seberapa sering prediksi yang dihasilkan suatu model bernilai benar. Akurasi berasal dari perbandingan antara jumlah hasil prediksi yang benar dengan total prediksi. Akurasi dapat dihitung dengan rumus:

$$\text{Accuracy} = \frac{\text{TP} + \text{TN}}{\text{TP} + \text{TN} + \text{FP} + \text{FN}}\%$$

### F1-score

*F1-Score* adalah metrik evaluasi yang dihasilkan dari gabungan *precision* dan *recall*. *Precision* adalah bagian dari hasil positif yang diprediksi dengan benar. Metrik ini menunjukkan seberapa *confident* suatu model dalam memprediksi kelas positif sebagai positif. *Precision* dapat dihitung dengan rumus:

$$\text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}\%$$

Sedangkan, *recall* adalah metrik yang mengukur seberapa akurat suatu model memprediksi hasil positif. *Recall* dapat dihitung dengan rumus:

$$\text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}\%$$

*F1-Score* didapatkan dari rata-rata harmonis dari *precision* dan *recall*. Rata-rata harmonis ini tidak hanya memperhatikan nilai prediksi yang benar, tetapi juga memperhatikan nilai prediksi yang salah. Metrik *F1-Score* dapat dihitung dengan rumus:

$$\text{F1 Score} = \frac{2 \times \text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$

#### Interpretasi Hasil

| Model                  | Train Accuracy | Test Accuracy | Precision | Recall   | F1-Score |
|------------------------|----------------|---------------|-----------|----------|----------|
| Random Forest (Base)   | 0.999855       | 0.941307      | 0.941431  | 0.941307 | 0.939894 |
| Random Forest (Tuned)  | 0.979102       | 0.768549      | 0.817174  | 0.768549 | 0.762358 |

1. *Random Forest Baseline*
   - *Train Accuracy* yang sangat tinggi yaitu 0.999855, menunjukkan bahwa model hampir sempurna mempelajari data latih.
   - *Test Accuracy* juga tinggi yaitu 0.941307, menunjukkan performa yang sangat baik di data uji.
   - *Precision*, *Recall*, dan *F1-Score* juga seimbang dan tinggi, sekitar 0.937.
   - Akurasi training yang terlalu tinggi dibandingkan dengan akurasi testing bisa menjadi indikasi adanya *overfitting*, di mana model terlalu cocok dengan data latih namun berisiko kurang generalisasi ke data baru.

2. *Random Forest Hyperparameter Tuning*
   - Setelah dilakukan *tuning*, *Train Accuracy* turun menjadi 0.979102, menandakan bahwa model tidak terlalu overfit terhadap data pelatihan.
   - *Test Accuracy* juga menurun secara signifikan menjadi 0.768549, menunjukkan penurunan performa di data uji.
   - *Precision* dan *Recall* juga ikut menurun, meskipun masih cukup baik di angka 0.81 dan 0.77.
   - *F1-Score* menurun menjadi 0.762 yang menunjukkan adanya *trade-off* akibat tuning. Hal tersebut kemungkinan terjadi karena model menjadi lebih sederhana, parameter yang dipilih kurang optimal, atau tuning berlebihan dalam menghindari *overfitting* hingga menurunkan akurasi model.

## Summary

Proyek ini berhasil membangun sistem prediksi jenis pupuk berbasis algoritma *machine learning* dengan pendekatan *Random Forest* menggunakan data lingkungan seperti pH tanah, suhu, kelembaban, curah hujan, dan jenis tanaman. Berdasarkan hasil evaluasi, model *Random Forest Baseline* menunjukkan performa terbaik dengan akurasi tinggi pada data uji sebesar 94.13%, serta nilai *Precision*, *Recall*, dan *F1-score* yang seimbang di kisaran 94%, mengindikasikan model mampu memberikan rekomendasi pupuk secara tepat dan konsisten.

Ketika dilakukan *hyperparameter tuning* terhadap model, justru terjadi penurunan performa yang cukup signifikan, dengan akurasi uji menurun menjadi 76.85%. Hal ini menunjukkan bahwa model *baseline* sebenarnya sudah cukup optimal, dan penyesuaian parameter justru menurunkan kompleksitas model secara berlebihan sehingga mengurangi kemampuannya dalam menangkap pola pada data.

Hasil ini menjawab problem utama yang diangkat yaitu bagaimana membangun model prediksi yang akurat untuk membantu petani dalam memilih jenis pupuk yang sesuai dengan kondisi lahannya. Sistem yang dibangun mampu mengatasi keterbatasan dalam pengambilan keputusan secara manual yang selama ini membutuhkan waktu, tenaga, dan pengetahuan teknis yang tinggi. Selain itu, model yang dihasilkan terbukti efektif dalam memproses data lingkungan dan memberikan rekomendasi pupuk secara otomatis, sehingga mendukung efisiensi dalam proses pemupukan dan berpotensi meningkatkan produktivitas pertanian. Keterkaitan antara hasil proyek ini dengan tujuan yang ditetapkan juga sangat jelas yaitu model prediktif berhasil dibangun dan dioptimalkan, meskipun *tuning* belum memberikan hasil yang lebih baik, serta solusi berbasis data berhasil diwujudkan sebagai alat bantu pengambilan keputusan bagi petani.

Secara keseluruhan, proyek ini menunjukkan bahwa pendekatan *machine learning* sangat potensial untuk diterapkan dalam bidang pertanian presisi, khususnya untuk meningkatkan efektivitas pemupukan dan hasil pertanian melalui rekomendasi yang *data-driven*.

## References

[1] J. Pitono, "Pertanian presisi dalam budidaya lada the precision farming on pepper cultivation," Perspektif, vol. 18, no. 2, pp. 1279–1300, 2020.

[2] N. R. Imanuloh, R. Kuswulandari, T. Listiani, and D. Hartanti, "Sistem Pendukung Keputusan Pemilihan Pupuk Terbaik untuk Tanaman Padi di Desa Panggisari dengan Metode Fuzzy," in Prosiding Seminar Nasional Teknologi Informasi dan Bisnis (SENATIB), 2022.

[3] A. Rukmana, H. Susilawati, and Galang, "Pencatat pH Tanah Otomatis," Journal Universitas Garut, vol. 10, no. 1, pp. 25, 2019.
