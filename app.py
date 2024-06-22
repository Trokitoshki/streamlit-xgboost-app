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

# Definir las entradas del usuario (asegúrate de incluir todas las características que tu modelo espera)
NivelEducativo = st.selectbox('Nivel Educativo', ['Primaria', 'Secundaria'])
Item = st.number_input('Item', min_value=0, max_value=100, value=0)
ModalidadAtencion = st.selectbox('Modalidad de Atención', ['Presencial', 'Virtual'])
NecesidadesEspeciales = st.selectbox('Necesidades Especiales', ['Sí', 'No'])
TipoDeAlimento = st.selectbox('Tipo de Alimento', ['Fresco', 'Seco'])
Incidente = st.selectbox('Incidente', ['Sí', 'No'])
Descripción = st.text_input('Descripción', 'Ninguna')
Clima = st.selectbox('Clima', ['Soleado', 'Nublado', 'Lluvioso'])
Infraestructura = st.selectbox('Infraestructura', ['Buena', 'Regular', 'Mala'])
AccesoAInternet = st.selectbox('Acceso a Internet', ['Sí', 'No'])
ParticipaciónEnProgramasDeApoyo = st.selectbox('Participación en Programas de Apoyo', ['Sí', 'No'])
NúmeroDeEstudiantesEsperados = st.number_input('Número de Estudiantes Esperados', min_value=0, max_value=1000, value=500)
NúmeroDeEstudiantesPresentes = st.number_input('Número de Estudiantes Presentes', min_value=0, max_value=1000, value=500)
IngresoMedio = st.number_input('Ingreso Medio', min_value=0, max_value=100000, value=25000)
CantidadDeAlimentosKg = st.number_input('Cantidad de Alimentos (Kg)', min_value=0.0, value=0.0)
MatemáticaPromedio = st.number_input('Matemática Promedio (%)', min_value=0.0, max_value=100.0, value=50.0)
LecturaPromedio = st.number_input('Lectura Promedio (%)', min_value=0.0, max_value=100.0, value=50.0)
Temperatura = st.number_input('Temperatura', min_value=0.0, max_value=50.0, value=25.0)
NúmeroDeDocentes = st.number_input('Número de Docentes', min_value=0, max_value=100, value=10)
NivelDeSatisfacciónDeLosEstudiantes = st.number_input('Nivel de Satisfacción de los Estudiantes (%)', min_value=0.0, max_value=100.0, value=75.0)

# Convertir las entradas en un DataFrame de pandas
input_data = pd.DataFrame({
    'NivelEducativo': [NivelEducativo],
    'Item': [Item],
    'ModalidadAtencion': [ModalidadAtencion],
    'NecesidadesEspeciales': [NecesidadesEspeciales],
    'TipoDeAlimento': [TipoDeAlimento],
    'Incidente': [Incidente],
    'Descripción': [Descripción],
    'Clima': [Clima],
    'Infraestructura': [Infraestructura],
    'AccesoAInternet': [AccesoAInternet],
    'ParticipaciónEnProgramasDeApoyo': [ParticipaciónEnProgramasDeApoyo],
    'NúmeroDeEstudiantesEsperados': [NúmeroDeEstudiantesEsperados],
    'NúmeroDeEstudiantesPresentes': [NúmeroDeEstudiantesPresentes],
    'IngresoMedio': [IngresoMedio],
    'CantidadDeAlimentosKg': [CantidadDeAlimentosKg],
    'MatemáticaPromedio%': [MatemáticaPromedio],
    'LecturaPromedio%': [LecturaPromedio],
    'Temperatura': [Temperatura],
    'NúmeroDeDocentes': [NúmeroDeDocentes],
    'NivelDeSatisfacciónDeLosEstudiantes%': [NivelDeSatisfacciónDeLosEstudiantes]
})

# Realizar la predicción
if st.button('Predecir'):
    try:
        prediction = model.predict(input_data)
        st.write(f'## Predicción: {prediction[0]} kg')
    except Exception as e:
        st.write("Error al realizar la predicción:")
        st.write(e)
