
import streamlit as st

st.title("Calculadora de Área de un Triángulo")

st.write("Ingresa los valores de base y altura para calcular el área.")

base = st.number_input("Base del triángulo:", min_value=0.0, format="%.2f")
altura = st.number_input("Altura del triángulo:", min_value=0.0, format="%.2f")

if st.button("Calcular"):
    area = (base * altura) / 2
    st.success(f"El área del triángulo es: {area:.2f}")
