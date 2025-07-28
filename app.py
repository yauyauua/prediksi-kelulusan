
import streamlit as st
import joblib

# Load model
model = joblib.load("model_rf_compatible_v2.pkl")

st.title("Aplikasi Prediksi Kelulusan Mahasiswa")

ipk = st.number_input("Masukkan IPK:", min_value=0.0, max_value=4.0, step=0.01)
kehadiran = st.number_input("Masukkan Kehadiran (%):", min_value=0, max_value=100, step=1)
sks = st.number_input("Jumlah SKS Lulus:", min_value=0, step=1)

if st.button("Prediksi"):
    hasil = model.predict([[ipk, kehadiran, sks]])
    if hasil[0] == 1:
        st.success("Hasil Prediksi: Diprediksi LULUS 🎓")
    else:
        st.error("Hasil Prediksi: Diprediksi TIDAK LULUS ❌")
