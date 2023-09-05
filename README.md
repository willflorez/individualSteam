# PrimerProyectoIndividualHenry
<p align="center">
<img src="https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png"  height=300>
</p>

## Índice 
<!-- TABLA DE CONTENIDO -->
<details>
  <summary>Tabla de contenido</summary>
  <ol>  
    <li><a href="#Introducción">Introducción</a></li>
    <li><a href="#Objetivo">Objetivo</a></li>
    <li><a href="#pila-de-tecnologías">Pila de Tecnologías</a></li>
    <li><a href="#ETL">ETL</a></li>
    <li><a href="#EDA">EDA</a></li>
    <li><a href="#funciones-api">Funciones API</a></li>
    <li><a href="#modelo-ml">Modelo ML</a></li>
    <li><a href="#Deployment">Deployment</a></li>
    <li><a href="#Video">Video</a></li>
  </ol>
</details>

## Introducción

El presente proyecto tiene que ver con la puesta en práctica de todo lo aprendido en la carrera de DAta de Henry.
Busco personalmente la apropiación de los conocimientos de ETL, EDA y Machine Learning.
Es un desafío para mi enfrentarme a este Dataset y lograr realizar un modelo de Machine Learning funcional.
## Objetivo

Desarrollar mis aptitudes de análisis con el Dataset entregado y llevar a feliz término el proyecto cumpliendo con la entrega de un modelo de Machine Learning y las funciones solicitadas desplegadas en Render.

- **Transformación y Limpieza de Datos:** Optimizar el proceso de ETL con el fin de entender mejor los datos y tomar decisiones acertadas que me permitan conservna los datos de la mejor manera posible, en pro de cumplir con la creación de las funciones solicitadas y el modelo requerido.

- **Desarrollo de API:** Entregar una API que arroje resultados acordes al contenido de los diferentes Dataset.

- **Modelo ML:** Desarrollar un modelo que recomiende videojuegos.

- **Feature Engineering:** Crear la columna ***Sentiment_analysis*** la cual aplica un analisis de sentimiento a diferentes reseñas que hay en data set, donde se deben tomar los siguientes valores **0** si es ***Malo***, **1** si es ***Neutro*** y **2** si es ***Positivo***. Además, de no estar la reseña se debe tomar el valor de  **1**.

**`Desarrollo API`**:   Propones disponibilizar los datos de la empresa usando el framework ***FastAPI***. Las consultas que propones son las siguientes:

<sub> Debes crear las siguientes funciones para los endpoints que se consumirán en la API, recuerden que deben tener un decorador por cada una (@app.get(‘/’)).<sub/>


+ def **userdata( *`User_id` : str* )**:
    Debe devolver `cantidad` de dinero gastado por el usuario, el `porcentaje` de recomendación en base a reviews.recommend y `cantidad de items`.

+ def **countreviews( *`YYYY-MM-DD` y `YYYY-MM-DD` : str* )**:
    `Cantidad de usuarios` que realizaron reviews entre las fechas dadas y, el `porcentaje` de recomendación de los mismos en base a reviews.recommend.

+ def **genre( *`género` : str* )**:
    Devuelve el `puesto` en el que se encuentra un género sobre el ranking de los mismos analizado bajo la columna PlayTimeForever. 

+ def **userforgenre( *`género` : str* )**:
    `Top 5` de usuarios con más horas de juego en el género dado, con su URL (del user) y user_id.

+ def **developer( *`desarrollador` : str* )**:
    `Cantidad` de items y `porcentaje` de contenido Free por año según empresa desarrolladora. 
Ejemplo de salida:
    | Activision ||
    |----------|----------|
    | Año  | Contenido Free  |
    | 2023   | 27% |
    | 2022    | 25%   |
    | xxxx    | xx%   |


+ def **sentiment_analysis( *`año` : int* )**:
    Según el año de lanzamiento, se devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento. 

    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ejemplo de retorno: *{Negative = 182, Neutral = 120, Positive = 278}*

**Analisis Exploratorio de Datos** Se busca encontrar patrones entre los datos, su relación con cada uno de ellos, ver si hay algun patron interesante entre cada uno de ellos.

**`Modelo de aprendizaje automático`**: Se busca generar un modelo de machine learning de recomendación de videojuegos, el modelo deberá tener una relación ítem-ítem, esto es se toma un item, en base a que tan similar esa ese ítem al resto, se recomiendan similares. Aquí el input es un juego y el output es una lista de juegos recomendados, para ello se aplica la similitud del coseno.
El modelo debe derivar en un endpoint de la API.

+ def **recomendacion_juego( *`id de producto`* )**:
    Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.

**`Video`**: Se requiere mostrar que los enpoints funcionan realmente! Para ello se elabora un video mostrando el resultado de las consultas propuestas y del  modelo de ML entrenado.

## Pila de Tecnologías

![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)

## Proceso de ETL

Para ETL consideré cada Datase por aparte. Aplicando transformaciones donde el tipo de cada columna fuera el mismo. Tratando los nulos con cuidado y siendo cuidadoso con el borrado. Estudié cada columna y sus relaciones para entender que tipo de información me iba a encontrar y fui de a poco diseñando en mi mente una posible solución.  


**1. Eliminación de Duplicados:** Cuando se evidenció la existencia de registros duplicados, se eliminaron, tenían el mismo valor en todas ls columnas.  

**2. Filtrado de Fechas Inválidas:** La colunma release_date fue transformada para poder extraer los datos en formato YYYY-MM-DD.

**3. Creación de Columna de Año:** Como parte de la transformación, se ha creado una nueva columna llamada "release_anio". La cual se ha obtenido a partir del año de la columna "release_date". Esta columna es crucial para los endpoints de la API y proporciona un filtro eficaz para las solicitudes basadas en el año.

**4. Gestión de Valores Nulos:** Cada valor nulo que fuera lo suficientemente alto en porcentaje respecto a los demás datos de la columna se eliminaron. Esto gracias a que con otras columnas se podía seguir trabajando sin miedo a perder información.
**5. Identificación de Outliers:** Para asegurar la integridad de la columna "year_release", se ha revisado cuidadosamente mediante la ordenación y filtrado de los primeros y últimos valores. Esta inspección visual permite identificar posibles outliers o valores incoherentes que podrían requerir tratamiento adicional para su corrección o eliminación.

Del proceso de ETL se lograron obtener datos limpios y optimizado para el análisis y su implementación en la API. 

*Todas estas etapas se llevaron a cabo de manera local en **Visual Studio Code (VSCODE)**, empleando **Jupyter Notebook** como mi entorno principal. Para la implementación de cada paso, contamos con la potencia de **Python** como lenguaje de programación, respaldado por las bibliotecas **numpy y pandas**, que fueron fundamentales para la manipulación y transformación eficiente de los datos.

## EDA

El proceso de EDA lo centré en el conocimiento de las variables y como se relacionan entre sí. Queriendo encontrar datos que me indicarán la información mas relavante a tener en cuenta. De esta manera se obtiene por ejemplo lo siguiente: 
1. De reviews casi el 62% de los datos reflejan sentimientos neutrales, cerca del 30% sentimientos positivos hacia el juego y menos del 9% fue negativo. 
2. Cantidad de usuarios únicos que opinaron: 21432.
3. Dias de pico de reviews

*Estos procesos se desarrollaron localmente en **Visual Studio Code (VSCODE)** utilizando **Jupyter Notebook** como entorno de trabajo. La combinación de herramientas tecnológicas empleada esta basada en **Python** como lenguaje de programación, junto con librerias  como **numpy y pandas** para la manipulación de datos. Además, se utilizo **matplotlib y seaborn** para la creación de visualizaciones gráficas.*

## Funciones API

En el archivo main.py se entrega el código de las funciones solicitadas, probadas en API, preparando el proyecto para su futuro despliegue con Render

## Modelo ML

El modelo de ML de recomendación de videojuegos item-item entrega 5 recomendaciones de videojuegos. 


# Deployment

Luego de completar la implementación de **main.py** y demás archivos que componen el modelo y las funciones, el despliegue de la API se realizó de manera exitosa a través de Render, con ayuda de un **Dockerfile**:

**1. Creación de Entorno Virtual:** Se utiliza venv, lo cual permitió gestionar y separar las dependencias específicas de la API.

**2. Configuración de Archivos Necesarios:** Se llevaron a cabo las configuraciones necesarias para el despliegue, asegurando que todos los archivos necesarios estuvieran presentes. Algunos archivos son los datasets en formato parquet, el archivo de requirements.txt y el archivo .gitignore. 

**3. Inicialización de Git:** Se inició un repositorio de Git para el proyecto **(https://github.com/willflorez/individualSteam.git)** donde se evidencia el desarrollo del proyecto.

**4. Despliegue en Render:** Con Render se despliega la API. [API en ejecución](https://individualsteam.onrender.com). **(Se suguiere agregar "/docs" al final del enlace para acceder a la documentación automática creada por Swagger. Esto brinda una interfaz interactiva y detallada que describe todos los endpoints, métodos y parámetros disponibles en la API de manera clara.)**

## Video

Abajo comparto link de video solicitado.

<div align="center">
  
[https://www.loom.com/share/3c45f5c52b9344088c52cd5bbe820492?sid=5035446d-fc5a-480e-936d-fc211e582ff4]
  
</div>