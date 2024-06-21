import streamlit as st
import xgboost as xgb
import pandas as pd
import joblib

# Cargar el modelo entrenado
model = joblib.load('xgboost_model.pkl')

# Definir la interfaz de usuario
st.title('Predicción de Cantidad de Alimentos (XGBoost)')

st.write("""
### Introduce los valores de las características para realizar la predicción:
""")

# Entradas del usuario
feature1 = st.number_input('Número de Estudiantes Esperados', min_value=0, max_value=1000, value=500)
feature2 = st.number_input('Ingreso Medio', min_value=0, max_value=100000, value=25000)
# Añadir más características según tu modelo...

# Convertir las entradas en un DataFrame de pandas
input_data = pd.DataFrame({
    'NúmeroDeEstudiantesEsperados': [feature1],
    'IngresoMedio': [feature2],
    # Añadir más características según tu modelo...
})

# Mostrar las entradas del usuario
st.write('## Datos Introducidos:')
st.write(input_data)

# Realizar la predicción
if st.button('Predecir'):
    prediction = model.predict(input_data)
    st.write(f'## Predicción: {prediction[0]} kg')
