# Monitoring Factory Workers’ Daily Performance & Attrition

## Project Overview

![Batch Processing Flow](https://raw.githubusercontent.com/mhdalfarisy/Final-Project-Data-Engineer/main/assets/Batch%20Processing%20Flow.jpg)

### 🔗 Link Dashboard Power BI:  
[Dashboard Monitoring Factory Workers’ Daily Performance & Attrition](https://app.powerbi.com/view?r=eyJrIjoiNDk2ZjM0N2MtZTM3My00NjJkLTlkNmEtMTQ3OGYzNTJkZTlhIiwidCI6ImVhZmZiNWNlLTYwZGQtNDNhNC05Mjg3LTc5MzEzMmM2ODQzZSIsImMiOjEwfQ%3D%3D)

---

## 📊 Dataset Description

Kumpulan data sintetis ini berisi data kinerja dan pengurangan karyawan harian selama **18 bulan** (411.948 observasi) untuk sebuah pabrik dengan struktur organisasi yang terdiri dari **508 pekerja**. Karena adanya pergantian karyawan, total **687 orang** muncul dalam dataset ini.  

Dataset ini mencakup berbagai kejadian harian seperti:
- **Kehadiran pekerja**  
- **Tingkat efikasi harian**  
- **Kecelakaan kerja**  
- **Pemutusan hubungan kerja (PHK)**  
- **Penerimaan karyawan baru**  

Dataset ini juga memiliki hubungan kausal tersembunyi yang dapat diungkap melalui teknik **Machine Learning**.

### 🔍 Analisis yang dapat dilakukan:
- Bagaimana kinerja tinggi pekerja meningkatkan peluang mereka direkrut oleh pesaing.
- Bagaimana kesalahan mental atau kecelakaan dapat menjadi indikasi pekerja sedang sakit.
- Pengaruh hari dalam seminggu, bulan, dan tahun terhadap efikasi pekerja.
- Hubungan antara perbedaan usia dengan atasan terhadap efikasi pekerja.
- Pengaruh gender dalam tim terhadap produktivitas pekerja.
- Korelasi antara tekanan tenggat waktu dengan perilaku kerja sama tim dan gangguan.
- Pengelompokan pekerja berdasarkan efikasi harian tinggi, sedang, atau rendah.

---

## 📈 Visualization

### 1️⃣ Batch Processing Flow
![Batch Processing Flow](https://raw.githubusercontent.com/mhdalfarisy/Final-Project-Data-Engineer/main/assets/Batch%20Processing%20Flow.jpg)

### 2️⃣ Monitoring Dashboard  
![Visualization 1](https://raw.githubusercontent.com/mhdalfarisy/Final-Project-Data-Engineer/main/assets/Picture1.jpg)

![Visualization 2](https://raw.githubusercontent.com/mhdalfarisy/Final-Project-Data-Engineer/main/assets/Picture2.jpg)

---

## 🛠️ Tech Stack

- **Google Cloud Platform (GCP)**: BigQuery, Cloud Storage, Dataflow  
- **Python**: Pandas, NumPy, Scikit-learn  
- **Power BI**: Data visualization  
- **SQL**: Data extraction & transformation  
- **Apache Airflow**: Workflow orchestration  
- **Git & GitHub**: Version control  

---

## 📢 How to Use

1. Clone repository ini ke lokal:
   ```sh
   git clone https://github.com/mhdalfarisy/Final-Project-Data-Engineer.git
