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
  
  ![statistik deskriptif](https://github.com/VibyLadyscha/project-predictive-analytics/blob/main/img/Screenshot%202025-05-26%20080032.png)
  Berdasarkan hasil tersebut, dapat disimpulkan bahwa dataset tersebut menunjukkan kondisi agrikultur yang cukup beragam.
- Setelah dilakukan pengecekan, dataset ini juga sudah dalam kondisi bersih yaitu tidak memiliki *missing value* maupun data duplikat.

### EDA - Pengecekan Outlier
- Pengecekan outlier dilakukan pada data numerik dengan hasil sebagai berikut.
  
  ![outlier awal](https://github.com/VibyLadyscha/project-predictive-analytics/blob/main/img/Outlier%20Awal.png)
  Pada visualisasi tersebut outlier tidak terlihat jelas dikarenakan rentang data yang tidak sama antar variabel, sehingga perlu dilakukan normalisasi terlebih dahulu
- Setelah dilakukan normalisasi, outlier semakin terlihat dengan jelas dan kemudian dilakukan teknik *Interquartile Range* untuk menangani outlier tersebut.
  
  ![outlier setelah normalisasi](https://github.com/VibyLadyscha/project-predictive-analytics/blob/main/img/Outlier%20Setelah%20Normalisasi.png)
  
- Setelah diterapkan teknik *Interquartile Range*, pada boxplot terlihat tidak ada lagi outlier pada setiap variabel. Hasil dari penanganan outlier adalah sebagai berikut.
  ![outlier cleaned](https://github.com/VibyLadyscha/project-predictive-analytics/blob/main/img/Outlier%20Cleaned.png)

  Konsep *Interquartile Range (IQR)*:
  - Identifikasi outlier dengan metode *Interquartile Range*, yaitu dengan menghitung selisih antara Q3 dan Q1.
  - Nilai ekstrem di luar batas bawah `(Q1 - 1.5×IQR)` dan batas atas `(Q3 + 1.5×IQR)` dianggap outlier, lalu dilakukan capping atau penghapusan terhadap nilai-nilai tersebut.
     - Jika x lebih kecil dari batas bawah, ganti dengan *lower_limit*, jika lebih besar dari batas atas, ganti dengan *upper_limit*.
     - Jika tidak memenuhi keduanya, maka x tetap dipertahankan.

### EDA - Analisis Univariate

![univariate analysis](https://github.com/VibyLadyscha/project-predictive-analytics/blob/main/img/Univariate%20Analysis.png)

Setelah dilakukan visualisasi distribusi, terlihat bahwa frekuensi setiap variabel kategorik terutama variabel target tidak seimbang, sehingga diperlukan penanganan lebih lanjut untuk menghindari bias dalam memprediksi data yang distribusi kelasnya minoritas pada model.

### EDA - Correlation Matrix

![correlation matrix](https://github.com/VibyLadyscha/project-predictive-analytics/blob/main/img/Matrix%20Correlation.png)

## Data Preparation

### Encoding

Agar dapat diproses oleh model *machine learning*, perlu dilakukan perubahan variabel kategorik menjadi variabel numerik terlebih dahulu.

1. Label Encoding
   Penjelasan
2. One-Hot Encoding
   Penjelasan

### Splitting dan Oversampling

1. Splitting Data
   Penjelasan
2. Oversampling Data
   Penjelasan

Pada bagian ini Anda menerapkan dan menyebutkan teknik data preparation yang dilakukan. Teknik yang digunakan pada notebook dan laporan harus berurutan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan proses data preparation yang dilakukan
- Menjelaskan alasan mengapa diperlukan tahapan data preparation tersebut.

## Modeling

Pada proyek ini, modeling dilakukan menggunakan algoritma *Random Forest*. Selain menguji model *baseline*, saya juga melakukan *hyperparameter tuning* pada model tersebut untuk melihat apakah akurasi yang dihasilkan lebih baik atau tidak.

1. *Random Forest Baseline*
   Penjelasan
2. *Random Forest Hyperparameter Tuning*
   Penjelasan

Tahapan ini membahas mengenai model machine learning yang digunakan untuk menyelesaikan permasalahan. Anda perlu menjelaskan tahapan dan parameter yang digunakan pada proses pemodelan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan kelebihan dan kekurangan dari setiap algoritma yang digunakan.
- Jika menggunakan satu algoritma pada solution statement, lakukan proses improvement terhadap model dengan hyperparameter tuning. **Jelaskan proses improvement yang dilakukan**.
- Jika menggunakan dua atau lebih algoritma pada solution statement, maka pilih model terbaik sebagai solusi. **Jelaskan mengapa memilih model tersebut sebagai model terbaik**.

## Evaluation
Pada bagian ini anda perlu menyebutkan metrik evaluasi yang digunakan. Lalu anda perlu menjelaskan hasil proyek berdasarkan metrik evaluasi yang digunakan.

Sebagai contoh, Anda memiih kasus prediksi dan menggunakan metrik **akurasi, precision, recall, dan F1 score**. Jelaskan mengenai beberapa hal berikut:
- Penjelasan mengenai metrik yang digunakan
- Menjelaskan hasil proyek berdasarkan metrik evaluasi

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan formula metrik dan bagaimana metrik tersebut bekerja.

**---Ini adalah bagian akhir laporan---**

## References
[1] J. Pitono, "Pertanian presisi dalam budidaya lada the precision farming on pepper cultivation," Perspektif, vol. 18, no. 2, pp. 1279–1300, 2020.

[2] N. R. Imanuloh, R. Kuswulandari, T. Listiani, and D. Hartanti, "Sistem Pendukung Keputusan Pemilihan Pupuk Terbaik untuk Tanaman Padi di Desa Panggisari dengan Metode Fuzzy," in Prosiding Seminar Nasional Teknologi Informasi dan Bisnis (SENATIB), 2022.

[3] A. Rukmana, H. Susilawati, and Galang, "Pencatat pH Tanah Otomatis," Journal Universitas Garut, vol. 10, no. 1, pp. 25, 2019.
