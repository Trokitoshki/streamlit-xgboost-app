import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Cargar el modelo preentrenado
model_path = 'xgboost_model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Crear la interfaz de usuario en Streamlit
st.title('Predicción de Demanda de Alimentos en Instituciones Educativas')

# Entrada de usuario
NivelEducativo = st.selectbox('Nivel Educativo', ['Inicial', 'Primaria', 'Secundaria'])
TipoDeAlimento = st.selectbox('Tipo de Alimento', ['Carnes', 'Frutas', 'Lácteos', 'Verduras'])
NúmeroDeEstudiantesEsperados = st.number_input('Número de Estudiantes Esperados', min_value=0, max_value=1000, value=500)
NúmeroDeEstudiantesPresentes = st.number_input('Número de Estudiantes Presentes', min_value=0, max_value=1000, value=450)
IngresoMedio = st.number_input('Ingreso Medio', min_value=0, max_value=10000, value=3000)
ParticipaciónEnProgramasDeApoyo = st.selectbox('Participación en Programas de Apoyo', ['Sí', 'No'])

# Transformar entradas categóricas a numéricas o a la forma necesaria para el modelo
nivel_educativo_mapping = {'Inicial': 0, 'Primaria': 1, 'Secundaria': 2}
tipo_de_alimento_mapping = {'Carnes': 0, 'Frutas': 1, 'Lácteos': 2, 'Verduras': 3}
programa_apoyo_mapping = {'Sí': 1, 'No': 0}

# Crear el DataFrame de entrada para el modelo
input_data = pd.DataFrame({
    'NivelEducativo': [nivel_educativo_mapping[NivelEducativo]],
    'TipoDeAlimento': [tipo_de_alimento_mapping[TipoDeAlimento]],
    'NúmeroDeEstudiantesEsperados': [NúmeroDeEstudiantesEsperados],
    'NúmeroDeEstudiantesPresentes': [NúmeroDeEstudiantesPresentes],
    'IngresoMedio': [IngresoMedio],
    'ParticipaciónEnProgramasDeApoyo': [programa_apoyo_mapping[ParticipaciónEnProgramasDeApoyo]]
})

# Realizar la predicción
if st.button('Predecir'):
    prediction = model.predict(input_data)
    st.write(f'La cantidad de {TipoDeAlimento} requerida es: {prediction[0]:.2f} kg')
