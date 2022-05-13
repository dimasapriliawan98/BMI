import streamlit as st
st.write("""
# Menghitung Indeks Massa Tubuh
Ini adalah aplikasi untuk menghitung Indeks Massa Tubuh menggunakan Streamlit 
Indeks Massa Tubuh adalah metrik standar yang digunakan untuk menentukan siapa saja yang masuk dalam golongan berat badan sehat dan tidak sehat.
BMI = (weight in kilograms / height in meters^2  )
""")
weight = st.number_input("Masukkan weight", 0)
height = st.number_input("Masukkan height", 0)
hitung = st.button("Hitung BMI")
kriteria = st.button("Kriteria BMI")

if hitung:
	BMI = weight / ((height/100)**2)
	st.write("Hitungan BMInya adalah ", BMI)
if BMI < 18,5
	st.write("Berat Badan Kurang")
if BMI >= 18,5 <= 22,9
	st.write("Berat Badan Normal")
if	BMI >= 23 <= 29,9
	st.write("Berat Badan Berlebih (Obesitas)")
if	BMI > 30
	st.write("Obesitas")
