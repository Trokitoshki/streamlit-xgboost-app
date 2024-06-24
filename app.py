import streamlit as st
import pandas as pd

# Definir la interfaz de usuario
st.title('Predicción de Cantidad de Alimentos (Simulado)')

st.write("""
### Introduce los valores de las características para realizar la predicción:
""")

# Definir las entradas del usuario basadas en las características especificadas
NivelEducativo = st.selectbox('Nivel Educativo', ['Inicial', 'Primaria', 'Secundaria'])
TipoDeAlimento = st.selectbox('Tipo de Alimento', ['Carnes', 'Frutas', 'Lácteos', 'Verduras'])
NúmeroDeEstudiantesEsperados = st.number_input('Número de Estudiantes Esperados', min_value=0, max_value=1000, value=500)
NúmeroDeEstudiantesPresentes = st.number_input('Número de Estudiantes Presentes', min_value=0, max_value=1000, value=450)
IngresoMedio = st.number_input('Ingreso Medio', min_value=0, max_value=10000, value=3000)
ParticipaciónEnProgramasDeApoyo = st.selectbox('Participación en Programas de Apoyo', ['Sí', 'No'])

# Crear DataFrame con las entradas del usuario
input_data = pd.DataFrame({
    'NivelEducativo': [NivelEducativo],
    'TipoDeAlimento': [TipoDeAlimento],
    'NúmeroDeEstudiantesEsperados': [NúmeroDeEstudiantesEsperados],
    'NúmeroDeEstudiantesPresentes': [NúmeroDeEstudiantesPresentes],
    'IngresoMedio': [IngresoMedio],
    'ParticipaciónEnProgramasDeApoyo': [ParticipaciónEnProgramasDeApoyo]
})

# Calcular características adicionales
input_data['RatioEstudiantes'] = input_data['NúmeroDeEstudiantesPresentes'] / (input_data['NúmeroDeEstudiantesEsperados'] if input_data['NúmeroDeEstudiantesEsperados'][0] != 0 else 1)
input_data['IngresoPerCapita'] = input_data['IngresoMedio'] / (input_data['NúmeroDeEstudiantesPresentes'] if input_data['NúmeroDeEstudiantesPresentes'][0] != 0 else 1)

# Mostrar las entradas del usuario
st.write('## Datos Introducidos:')
st.write(input_data)

# Simular la predicción utilizando una fórmula sencilla
def simulate_prediction(data):
    base_value = 50  # Valor base ficticio
    nivel_educativo_factor = {'Inicial': 1.1, 'Primaria': 1.2, 'Secundaria': 1.3}
    tipo_alimento_factor = {'Carnes': 1.2, 'Frutas': 1.0, 'Lácteos': 1.1, 'Verduras': 0.9}
    programa_factor = {'Sí': 1.1, 'No': 1.0}
    
    prediction = base_value
    prediction *= nivel_educativo_factor[data['NivelEducativo'][0]]
    prediction *= tipo_alimento_factor[data['TipoDeAlimento'][0]]
    prediction *= programa_factor[data['ParticipaciónEnProgramasDeApoyo'][0]]
    prediction *= data['RatioEstudiantes'][0]
    prediction *= data['IngresoPerCapita'][0] / 1000  # Escalar el ingreso per capita
    
    return prediction

# Realizar la predicción
if st.button('Predecir'):
    simulated_prediction = simulate_prediction(input_data)
    st.write(f'## Predicción: {simulated_prediction:.2f} kg')
