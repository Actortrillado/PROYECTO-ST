import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="imc",
    page_icon="📱",
    layout="wide"
    

# Título
st.title("Calculadora de IMC (Índice de Masa Corporal)")
st.write("Calcula tu IMC ingresando tu peso y altura, y observa tu resultado en el gráfico.")
st.badge("El cambio es hoy")
# Entradas del usuario 
peso = st.number_input("Ingresa tu peso (kg):", min_value=1.0, max_value=500.0, step=1.0)
altura_cm = st.number_input("Ingresa tu altura (cm):", min_value=50.0, max_value=300.0, step=1.0)

# Cálculo del IMC
if peso and altura_cm:
    altura_m = altura_cm / 100
    imc = peso / (altura_m ** 2)

    # Clasificación
    if imc < 18.5:
        estado = "Bajo peso"
        color = "skyblue"
    elif 18.5 <= imc < 24.9:
        estado = "Peso normal"
        color = "lightgreen"
    elif 25 <= imc < 29.9:
        estado = "Sobrepeso"
        color = "gold"
    elif 30 <= imc < 34.9:
        estado = "Obesidad I"
        color = "orange"
    elif 35 <= imc < 39.9:
        estado = "Obesidad II"
        color = "tomato"
    else:
        estado = "Obesidad III (mórbida)"
        color = "red"

    # Muestra los resultados
    st.subheader(f"Tu IMC es: {imc:.2f}")
    st.write(f"**Estado:** {estado}")

    # Crear gráfico
    fig, ax = plt.subplots(figsize=(8, 2))
    ax.barh(["IMC"], [imc], color=color)
    ax.axvline(18.5, color='blue', linestyle='--', label="18.5 Bajo peso")
    ax.axvline(25, color='green', linestyle='--', label="25 Peso normal")
    ax.axvline(30, color='orange', linestyle='--', label="30 Sobrepeso")
    ax.axvline(35, color='red', linestyle='--', label="35 Obesidad I+")
    ax.set_xlim(10, 45)
    ax.set_xlabel("Valor IMC")
    ax.legend()
    ax.text(imc + 0.3, 0, f"{imc:.2f}", va='center')

    st.pyplot(fig)

else:
    st.info("Por favor, ingresa tu peso y altura para calcular el IMC.")
    
    import streamlit as st

# Título
st.title("Calculadora de Calorías Diarias")
st.write("Calcula aproximadamente cuántas calorías necesitas al día según tu peso, altura, edad, sexo y nivel de actividad.")

# datos del usuario
sexo = st.radio("Sexo:", ("M", "F"))
edad = st.slider("Edad (años):", min_value=10, max_value=100, value=25, step=1)
peso = st.slider("Peso (kg):", min_value=30, max_value=200, value=70, step=1)
altura_cm = st.slider("Altura (cm):", min_value=100, max_value=250, value=170, step=1)

# Nivel de actividad
st.write("Nivel de actividad:")
actividad = st.selectbox("Selecciona tu nivel de actividad:", 
    ["Sedentario (poco o nada de ejercicio)",
     "Ligero (ejercicio ligero 1-3 días/semana)",
     "Moderado (ejercicio moderado 3-5 días/semana)",
     "Activo (ejercicio fuerte 6-7 días/semana)",
     "Muy activo (ejercicio muy intenso o trabajo físico)"])

# Botón para calcular
if st.button("Calcular calorías"):
    # Cálculo de TMB
    if sexo == "M":
        tmb = 88.362 + (13.397 * peso) + (4.799 * altura_cm) - (5.677 * edad)
    else:
        tmb = 447.593 + (9.247 * peso) + (3.098 * altura_cm) - (4.330 * edad)

    # Factor de actividad
    factores = [1.2, 1.375, 1.55, 1.725, 1.9]
    factor = factores[actividad := ["Sedentario (poco o nada de ejercicio)",
                                     "Ligero (ejercicio ligero 1-3 días/semana)",
                                     "Moderado (ejercicio moderado 3-5 días/semana)",
                                     "Activo (ejercicio fuerte 6-7 días/semana)",
                                     "Muy activo (ejercicio muy intenso o trabajo físico)"].index(actividad)]
    
    calorias = tmb * factor

    # Mostrar resultado

    st.success(f"Para mantener tu peso, necesitas aproximadamente **{calorias:.0f} calorías al día**.")
