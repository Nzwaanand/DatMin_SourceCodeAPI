# 📊 Prediksi Pengangguran Berdasarkan Tingkat Pendidikan di Indonesia

Proyek ini adalah pembuatan API menggunakan **FastAPI** untuk memprediksi jumlah pengangguran di Indonesia berdasarkan tingkat pendidikan.  
Model yang digunakan adalah **XGBoost Regressor** yang telah dilatih dan disimpan dalam file `.pkl`.

---

## 🚀 Libraries and Frameworks
- Python
- FastAPI
- Uvicorn
- Scikit-learn
- XGBoost
- Pandas
- Numpy
- Joblib

---

## 📂 Struktur File

| File/Folder | Keterangan |
|:-----------|:-----------|
| `app.py` | Source code utama API FastAPI. |
| `requirements.txt` | Daftar library yang dibutuhkan. |
| `scaler-2.pkl` | File scaler untuk normalisasi data input sebelum prediksi. |
| `xgb_best_model.pkl` | File model XGBoost Regressor hasil training dan tuning terbaik. |

---

## 📥 Cara Install dan Menjalankan API

1. Clone repository ini:
    ```bash
    git clone https://github.com/username/nama-repo.git
    cd nama-repo
    ```

2. Install semua dependensi:
    ```bash
    pip install -r requirements.txt
    ```

3. Jalankan API menggunakan Uvicorn:
    ```bash
    uvicorn app:app --reload
    ```

4. Akses dokumentasi Swagger UI di:
    ```
    http://127.0.0.1:8000/docs
    ```

---

## 🛠️ Cara Menggunakan API

- Endpoint: `/predict`
- Method: `POST`
- Format Input (JSON):

    ```json
    {
      "pendidikan_rendah": 3500000,
      "pendidikan_menengah": 7000000,
      "pendidikan_tinggi": 1500000,
      "tahun": 2025
    }
    ```

- Contoh Output (JSON):

    ```json
    {
      "tahun_prediksi": 2025,
      "prediksi_pengangguran": 12045678.0
    }
    ```

---

## 📈 Model Machine Learning

- Model yang digunakan adalah **XGBoost Regressor**.
- Dataset berisi jumlah pengangguran berdasarkan tingkat pendidikan dari tahun 2006–2022.
- Model ini telah melalui tahapan:
  - Bussiness Understanding
  - Data Understanding
  - Data Preparation
  - Modelling
  - Evaluation menggunakan MAE, MSE, RMSE, dan MAPE.

---

> Dibuat dengan oleh [Nazwa Tri Ananda - 2309116018]  
> Postest Praktikum *Data Mining* - 2025
