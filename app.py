import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import MinMaxScaler

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

# Crear DataFrame con las entradas del usuario
input_data = pd.DataFrame({
    'NúmeroDeEstudiantesEsperados': [NúmeroDeEstudiantesEsperados],
    'NúmeroDeEstudiantesPresentes': [NúmeroDeEstudiantesPresentes]
})

# Paso 1: Escalado de las columnas numéricas (asumiendo que se utilizó MinMaxScaler)
scaler = MinMaxScaler()
numeric_columns = ['NúmeroDeEstudiantesEsperados', 'NúmeroDeEstudiantesPresentes']

# Aplicar el escalado a las columnas numéricas
input_data[numeric_columns] = scaler.fit_transform(input_data[numeric_columns])

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
