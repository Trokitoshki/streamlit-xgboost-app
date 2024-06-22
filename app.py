import streamlit as st
import pandas as pd
import joblib

# Cargar el modelo entrenado
model = joblib.load('xgboost_model.pkl')

# Definir la interfaz de usuario
st.title('Predicción de Cantidad de Alimentos (XGBoost)')

st.write("""
### Introduce los valores de las características para realizar la predicción:
""")

# Definir las entradas del usuario basadas en las características mencionadas
NúmeroDeEstudiantesEsperados = st.number_input('Número de Estudiantes Esperados', min_value=0, max_value=1000, value=500)
NúmeroDeEstudiantesPresentes = st.number_input('Número de Estudiantes Presentes', min_value=0, max_value=1000, value=500)
IngresoMedio = st.number_input('Ingreso Medio', min_value=0, max_value=100000, value=25000)
MatemáticaPromedio = st.number_input('Matemática Promedio (%)', min_value=0.0, max_value=100.0, value=50.0)
LecturaPromedio = st.number_input('Lectura Promedio (%)', min_value=0.0, max_value=100.0, value=50.0)
Temperatura = st.number_input('Temperatura', min_value=0.0, max_value=50.0, value=25.0)
NúmeroDeDocentes = st.number_input('Número de Docentes', min_value=0, max_value=100, value=10)
NivelDeSatisfacciónDeLosEstudiantes = st.number_input('Nivel de Satisfacción de los Estudiantes (%)', min_value=0.0, max_value=100.0, value=75.0)

# Crear DataFrame con las entradas del usuario
input_data = pd.DataFrame({
    'NúmeroDeEstudiantesEsperados': [NúmeroDeEstudiantesEsperados],
    'NúmeroDeEstudiantesPresentes': [NúmeroDeEstudiantesPresentes],
    'IngresoMedio': [IngresoMedio],
    'MatemáticaPromedio%': [MatemáticaPromedio],
    'LecturaPromedio%': [LecturaPromedio],
    'Temperatura': [Temperatura],
    'NúmeroDeDocentes': [NúmeroDeDocentes],
    'NivelDeSatisfacciónDeLosEstudiantes%': [NivelDeSatisfacciónDeLosEstudiantes]
})

# Mostrar las entradas del usuario
st.write('## Datos Introducidos:')
st.write(input_data)

# Realizar la predicción
if st.button('Predecir'):
    try:
        prediction = model.predict(input_data)
        st.write(f'## Predicción: {prediction[0]} kg')
    except Exception as e:
        st.write("Error al realizar la predicción:")
        st.write(e)
