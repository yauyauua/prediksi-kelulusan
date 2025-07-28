# Prediksi Tingkat Kelulusan Mahasiswa

Aplikasi ini dibuat untuk memenuhi Ujian Akhir Semester (UAS) mata kuliah **Proyek Data Mining (ST167)** di **Universitas Amikom Yogyakarta**.

Aplikasi berbasis **Streamlit** ini dapat memprediksi apakah seorang mahasiswa akan **lulus** atau **tidak lulus** berdasarkan data akademik seperti jumlah SKS, IPK, lama studi, dan status beasiswa.

---

## ?? Struktur Proyek

| File | Deskripsi |
|------|-----------|
| `app.py` | Script utama aplikasi Streamlit |
| `model_rf_compatible_v2.pkl` | Model Random Forest hasil pelatihan (joblib) |
| `requirements.txt` | Daftar dependensi Python |
| `README.md` | Dokumentasi proyek ini |

---

## ?? Algoritma yang Digunakan

- **Random Forest Classifier** dari `scikit-learn`

---

## ?? Cara Menjalankan Aplikasi

1. Clone repositori ini:
   ```bash
   git clone https://github.com/yauyauua/prediksi-kelulusan.git
   cd prediksi-kelulusan
