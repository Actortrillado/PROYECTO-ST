# Importa la librería principal de Streamlit para construir la aplicación web.
import streamlit as st

# Configura las propiedades de la página web que se mostrará en el navegador.
st.set_page_config(
    # Establece el título de la pestaña del navegador.
    page_title="Sitio teorico",
    # Define el ícono de la pestaña del navegador (en este caso, unas gafas de sol).
    page_icon=":sunglasses:"
     )
# Agrega un título principal a la aplicación web.
st.title("Bienvenido a ST")
# Muestra un "badge" (insignia o etiqueta) con un mensaje, color e ícono.
# Es una forma de destacar información breve
st.badge("El cambio depende de ti", color="red", icon=":material/done_outline:")

# Agrega un bloque de texto multilinea usando el elemento 'write'.
st.write(
    """
Aquí buscamos e informamos respecto a los temas fisicos de la ingesta de alimentos en el cuerpo humano y como lograr tus metas (fisico soñado). En esta página encontrarás toda la información respecto a las dudas que tengas sobre el tema y podrás saber tu imc (indice masa corporal) y ver como mejorar fisicamente, ver a dos fisicoculturistas que llegaron a un gran extremo de músculos, de manera poco saludable y con dietas extremas (no intentar, puedes llegar a tener graves consecuencias). Retomando acá podrás saber como ver tu IMC y enfocarte en mejorar fisicamente, ponerte saludable y estar en un IMC regular y apto para tí  

"""
    )
# Muestra una línea divisoria horizontal para separar visualmente el contenido.
st.divider()

# Crea un encabezado de sección de nivel 2 y añade una línea divisoria justo debajo.
st.header("Recomendaciones", divider=True)
# Un bloque para escribir un texto utilizando "write"
st.write ("""acá podrás escuchar un audio de Ronnie Coleman emocionandose por levantar peso y escuchar su mitica frase "yeah buddy!!!"
""")
# Inserta un reproductor de audio en la aplicación para el archivo especificado.
# Nota: El archivo "Voicy_Let's Go!!.mp3" debe estar en el mismo directorio.
st.audio ("Voicy_Let's Go!!.mp3")

# Crea dos columnas de igual ancho para organizar los elementos en la página.
coll, col2 = st.columns(2)

# Coloca contenido (texto) en la primera columna ('coll').
coll.write(
    """En las siguientes imagenes se muestra a dos grandes exponedores de el fisicoculturismo y lo que han logrado.

El primero es Ronnie Dean Coleman, conocido como "The King", es un exfisicoculturista profesional y exagente de policía estadounidense, ampliamente considerado como el mejor de la historia, principalmente por haber ganado el título de Mr. Olympia ocho veces consecutivas (1998-2005), un récord que comparte con Lee Haney. Su trayectoria es legendaria no solo por su masivo físico, sino también por las extremas cargas de peso que levantaba, documentadas con sus famosos lemas "Yeah Buddy" y "Lightweight Baby". Aunque el entrenamiento con pesos descomunales afectó gravemente su salud, requiriendo numerosas cirugías de columna y cadera, Coleman afirma que valió la pena y lamenta únicamente no haber entrenado aún más duro, dejando un legado inigualable de fuerza y dedicación extrema en el mundo del culturismo.

El otro fisico culturista es Dorian Andrew Mientjez Yates, conocido como "The Shadow" (La Sombra), es un culturista profesional británico que dominó el deporte al ganar el título de Mr. Olympia seis veces consecutivas, de 1992 a 1997. Yates revolucionó el culturismo de los años 90 al ser un pionero de la era de los "Mass Monsters" y al popularizar el sistema de entrenamiento de Alta Intensidad (HIT), que enfatiza series breves y llevadas al fallo muscular absoluto en lugar de grandes volúmenes de entrenamiento. Su enfoque metodológico, que incluía apariciones esporádicas y silenciosas en la escena competitiva, le valió su apodo. A pesar de retirarse prematuramente en 1997 debido a lesiones graves, como desgarros de bíceps y tríceps, su físico denso, su legendaria espalda y su filosofía de "calidad sobre cantidad" lo consolidaron como una de las figuras más influyentes y enigmáticas de la historia del culturismo. """
    )

# Coloca una imagen en la segunda columna ('col2').
# Nota: El archivo "negroni.jpg" debe estar en el mismo directorio.
col2.image("negroni.jpg")

# Coloca otra imagen en la segunda columna ('col2'), debajo de la anterior.
# Nota: El archivo "yates.jpg" debe estar en el mismo directorio.
col2.image("yates.jpg")

#Titulo
st.title("¿Que es el IMC?")

# Muestra una línea divisoria horizontal para separar visualmente el contenido.
st.divider()

#escribir informacion
st.write("""El Índice de Masa Corporal (IMC) es una herramienta de cribado sencilla, adoptada por la Organización Mundial de la Salud (OMS), que se utiliza para estimar si el peso de una persona es saludable en relación con su estatura. Se calcula dividiendo el peso en kilogramos entre el cuadrado de la estatura en metros ($\text{IMC} = \text{kg}/\text{m}^2$). El resultado permite clasificar rápidamente a los adultos en categorías como bajo peso, peso normal, sobrepeso u obesidad, y sirve como un indicador general para evaluar los riesgos potenciales de salud relacionados con el peso. Sin embargo, su limitación es que no mide directamente el porcentaje de grasa corporal ni distingue entre la masa muscular y la grasa, por lo que no es un diagnóstico definitivo y debe complementarse con otras evaluaciones médicas.
"""
         )

#imagen en este caso del IMC
st.image("Fotoimc.jpg")

#titulooo
st.title("¿Como se cuentan las calorías?")

# Muestra una línea divisoria horizontal para separar visualmente el contenido.
st.divider()

#escribir más informacion
st.write("""Contar calorías (kilocalorías, $kcal$) es una estrategia de gestión de peso basada en el balance energético, donde la clave reside en consumir menos calorías de las que se gastan (déficit) para perder peso, o más (superávit) para ganarlo, o mantener un consumo y gasto iguales para mantener el peso. Aunque no es la única vía, contar calorías es beneficioso porque genera conciencia nutricional (obligando a leer etiquetas y medir porciones), facilita la gestión precisa de los objetivos de peso mediante números medibles y promueve la elección de alimentos más saciantes y nutritivos para mantenerse dentro del "presupuesto". Es importante recordar que la calidad de las calorías importa tanto como la cantidad, y debe ser visto como una herramienta de aprendizaje temporal para establecer hábitos, no una regla eterna que cause obsesión.
"""
         )

st.image("calorias.jpg")
st.write("ahora vamos a adjuntar el video de la imagen el cual es un video para contar las calorías y te puedas guiar")
st.video("https://youtu.be/lHvfNnecQJI?si=bcgYUWsve5OysWBq")
# Inicializa el objeto de navegación de Streamlit (experimental).