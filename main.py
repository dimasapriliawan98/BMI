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

if BMI < 18.5:
	st.write("berat badan kurang", kriteria)
elif BMI >= 18.5 and <= 22.9:
	st.write("Berat Badan Normal", kriteria)
else BMI >= 23 and <= 29,9:
	st.write("Berat Badan Berlebih (Obesitas)", kriteria) 
else BMI > 30:
	st.write("Obesitas", kriteria)
	
