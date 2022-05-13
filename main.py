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

hitung = st.button("Hitung BMI")

if hitung:
	BMI = weight / ((height/100)**2)
	st.write("Hitungan BMInya adalah ", if BMI < 18.5 ="Berat Badan Kurang" else BMI >= 18.5 and <= 22.9 ="Berat Badan Normal" else BMI >= 23 and <= 29,9 ="Berat Badan Berlebih (Obesitas)" else BMI > 30 = "Obesitas" )
	
