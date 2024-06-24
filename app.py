import streamlit as st
import pandas as pd


# Definir la interfaz de usuario
st.title('Predicción de Cantidad de Alimentos (XGBoost)')

st.write("""
### Introduce los valores de las características para realizar la predicción:
""")


# Definir las entradas del usuario basadas en las características especificadas
NivelEducativo = st.selectbox('Nivel Educativo', ['Inicial', 'Primaria', 'Secundaria'])
TipoDeAlimento = st.selectbox('Tipo de Alimento', ['Carnes', 'Frutas', 'Lácteos', 'Verduras'])
NúmeroDeEstudiantesEsperados = st.number_input('Número de Estudiantes Esperados', min_value=0, max_value=1000, value=500)
NúmeroDeEstudiantesPresentes = st.number_input('Número de Estudiantes Presentes', min_value=0, max_value=1000, value=450)

# Crear DataFrame con las entradas del usuario
input_data = pd.DataFrame({
    'NivelEducativo': [NivelEducativo],
    'TipoDeAlimento': [TipoDeAlimento],
    'NúmeroDeEstudiantesEsperados': [NúmeroDeEstudiantesEsperados],
    'NúmeroDeEstudiantesPresentes': [NúmeroDeEstudiantesPresentes]
})

# Calcular características adicionales
input_data['RatioEstudiantes'] = input_data['NúmeroDeEstudiantesPresentes'] / (input_data['NúmeroDeEstudiantesEsperados'] if input_data['NúmeroDeEstudiantesEsperados'][0] != 0 else 1)

# Mostrar las entradas del usuario
st.write('## Datos Introducidos:')
st.write(input_data)

# Simular la predicción utilizando las condiciones especificadas
def simulate_prediction(data):
    # Asignar valores base según el nivel educativo
    nivel_educativo_factor = {'Inicial': 0.79, 'Primaria': 1.0, 'Secundaria': 1.43}
    tipo_alimento_factor = {'Carnes': 0.21, 'Frutas': 0.32, 'Lácteos': 0.24, 'Verduras': 0.37}
    
    nivel_educativo = data['NivelEducativo'][0]
    tipo_alimento = data['TipoDeAlimento'][0]
    ratio_estudiantes = data['RatioEstudiantes'][0]
    estudiantes_presentes = data['NúmeroDeEstudiantesPresentes'][0]

    # Calcular la cantidad base de alimentos según el nivel educativo y el tipo de alimento
    base_alimentos = nivel_educativo_factor[nivel_educativo] * estudiantes_presentes
    base_alimentos_tipo = tipo_alimento_factor[tipo_alimento] * estudiantes_presentes

    # Ajustar la cantidad de alimentos según el ratio de estudiantes
    if ratio_estudiantes >= 0.8:
        # Ratio alto
        prediccion = base_alimentos + base_alimentos_tipo
    elif 0.5 <= ratio_estudiantes < 0.8:
        # Ratio medio
        prediccion = (base_alimentos + base_alimentos_tipo) * 0.74
    else:
        # Ratio bajo
        prediccion = (base_alimentos + base_alimentos_tipo) * 0.53
    
    return prediccion

# Realizar la predicción
if st.button('Predecir'):
    simulated_prediction = simulate_prediction(input_data)
    st.write(f'## Predicción: {simulated_prediction:.2f} kg')
