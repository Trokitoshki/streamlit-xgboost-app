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

# Definir las entradas del usuario basadas en las características especificadas
NivelEducativo = st.selectbox('Nivel Educativo', ['Inicial', 'Primaria', 'Secundaria'])
ModalidadAtencion = st.selectbox('Modalidad de Atención', ['Presencial', 'Virtual'])
NecesidadesEspeciales = st.selectbox('Necesidades Especiales', ['Sí', 'No'])
TipoDeAlimento = st.selectbox('Tipo de Alimento', ['Carnes', 'Frutas', 'Granos', 'Lácteos', 'Verduras'])
NúmeroDeEstudiantesEsperados = st.number_input('Número de Estudiantes Esperados', min_value=0, max_value=1000, value=500)

# Crear DataFrame con las entradas del usuario
input_data = pd.DataFrame({
    'NivelEducativo': [NivelEducativo],
    'ModalidadAtencion': [ModalidadAtencion],
    'NecesidadesEspeciales': [NecesidadesEspeciales],
    'TipoDeAlimento': [TipoDeAlimento],
    'NúmeroDeEstudiantesEsperados': [NúmeroDeEstudiantesEsperados]
})

# Procesar las características categóricas con One-Hot Encoding
categorical_columns = ['NivelEducativo', 'ModalidadAtencion', 'NecesidadesEspeciales', 'TipoDeAlimento']
input_data_encoded = pd.get_dummies(input_data, columns=categorical_columns)

# Asegurarse de que las columnas estén en el mismo orden que el modelo espera
expected_columns = [
    # Añadir todas las columnas esperadas por el modelo después de One-Hot Encoding
    'NivelEducativo_Primaria', 'NivelEducativo_Secundaria',
    'ModalidadAtencion_Presencial', 'ModalidadAtencion_Virtual',
    'NecesidadesEspeciales_No', 'NecesidadesEspeciales_Sí',
    'TipoDeAlimento_Fresco', 'TipoDeAlimento_Seco',
    'NúmeroDeEstudiantesEsperados'
]

# Asegurar que todas las columnas estén presentes, agregar columnas faltantes con valor 0
for col in expected_columns:
    if col not in input_data_encoded.columns:
        input_data_encoded[col] = 0
input_data_encoded = input_data_encoded[expected_columns]

# Mostrar las entradas del usuario
st.write('## Datos Introducidos:')
st.write(input_data_encoded)

# Realizar la predicción
if st.button('Predecir'):
    try:
        prediction = model.predict(input_data_encoded)
        st.write(f'## Predicción: {prediction[0]} kg')
    except Exception as e:
        st.write("Error al realizar la predicción:")
        st.write(e)

