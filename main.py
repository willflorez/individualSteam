from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
import pandas as pd
import pandas as pd
import operator
from API import presentacion

app = FastAPI()

df_reviews = pd.read_csv('reviews.csv')
df_gastos_items = pd.read_csv('gastos_items.csv')
df_genre_ranking = pd.read_csv('genre_ranking.csv')
df_items_developer = pd.read_csv('items_developer.csv')


@app.get(path="/", 
         response_class=HTMLResponse,
         tags=["Home"])
def home():
    '''
    Página de inicio que muestra una presentación.

    Returns:
    HTMLResponse: Respuesta HTML que muestra la presentación.
    '''
    return presentacion()

@app.get(path = '/userdata')
def userdata(user_id: str = Query(..., 
                                description="Coloque acá su id de usuario", 
                                example="js41637")):
    '''
    Esta función devuelve cantidad de dinero gastado, porcentaje de recomendación y el total de items segun el id usuario ingresado.
         
    '''
    
    usuario = df_reviews[df_reviews['user_id'] == user_id]
    
    cantidad_dinero = df_gastos_items[df_gastos_items['user_id']== user_id]['price'].iloc[0]
        
    count_items = df_gastos_items[df_gastos_items['user_id']== user_id]['items_count'].iloc[0]
    
    
    total_recomendaciones = usuario['recommend'].sum()
    
    total_reviews = len(df_reviews['user_id'].unique())
    
    porcentaje_recomendaciones = (total_recomendaciones / total_reviews) * 100
    
    return {
        'cantidad_dinero': int(cantidad_dinero),
        'porcentaje_recomendacion': round(float(porcentaje_recomendaciones), 2),
        'total_items': int(count_items)
    }
    
     
@app.get(path = '/countreviews')       
def countreviews(fecha_inicio: str = Query(..., 
                                 description="Fechas de inicio para filtar la información", 
                                 example='2010-01-01'), 
                  fecha_fin: str = Query(..., 
                                 description="Fechas de Fin para filtar la información", 
                                 example='2012-12-31')):
     '''
     Esta función devolverá información en pantalla sobre las reviews realizadas por los usuarios entre dos fechas ingresadas.
         
     '''
     
     user_data_entre_fechas = df_reviews[(df_reviews['reviews_date'] >= fecha_inicio) & (df_reviews['reviews_date'] <= fecha_fin)]
     
     total_usuarios = user_data_entre_fechas['user_id'].nunique()
     
     total_recomendacion = len(user_data_entre_fechas)
     
     total_recomendaciones_True = user_data_entre_fechas['recommend'].sum()
     
     porcentaje_recomendaciones = (total_recomendaciones_True / total_recomendacion) * 100
    
     return {
         'total_usuarios_reviews': int(total_usuarios),
         'porcentaje_recomendaciones': round(float(porcentaje_recomendaciones),2)
     }


@app.get(path = '/genre')
def genre(genero: str = Query(..., 
                             description="Ingrese género del videojuego", 
                             example='Action')):
     '''
     Esta función entrega el ranking del género ingresado según la cantidad de horas jugadas.
     '''


     rank = df_genre_ranking[df_genre_ranking['genres'] == genero]['ranking'].iloc[0]
     return {
         'rank': int(rank)
     }


# @app.get(path = '/userforgenre',
#           description = """ <font color="blue">
#                         1. Haga clik en "Try it out".<br>
#                         2. Ingrese el género en el box abajo.<br>
#                         3. Scrollear a "Resposes" para ver Top 5 de usuarios con más horas de juego en el género dado, con su URL y user_id.
#                         </font>
#                         """,
#          tags=["Consultas Generales"])
# def userforgenre(genero: str = Query(..., 
#                             description="Género del videojuego", 
#                             example='Simulation')):
#     '''
#     Esta función devuelve el top 5 de usuarios con más horas de juego en un género específico, junto con su URL de perfil y ID de usuario.
         
#     Args:
#         genero (str): Género del videojuego.
    
#     Returns:
#         dict: Un diccionario que contiene el top 5 de usuarios con más horas de juego en el género dado, junto con su URL de perfil y ID de usuario.
#             - 'user_id' (str): ID del usuario.
#             - 'user_url' (str): URL del perfil del usuario.
#     '''
#     # Filtra el dataframe por el género de interés
#     #data_por_genero = df_playtime_forever[df_playtime_forever['genres'] == genero]
#     # Agrupa el dataframe filtrado por usuario y suma la cantidad de horas
#     #top_users = data_por_genero.groupby(['user_url', 'user_id'])['playtime_horas'].sum().nlargest(5).reset_index()
    
#     # Se hace un diccionario vacío para guardar los datos que se necesitan
#     #top_users_dict = {}
#     #for index, row in top_users.iterrows():
#         # User info recorre cada fila del top 5 y lo guarda en el diccionario
#         #user_info = {
#             #'user_id': row['user_id'],
#             #'user_url': row['user_url']
#         #}
#         #top_users_dict[index + 1] = user_info
    
#     #return top_users_dict

# @app.get(path = '/developer',
#           description = """ <font color="blue">
#                         1. Haga clik en "Try it out".<br>
#                         2. Ingrese el nombre del desarrollador en el box abajo.<br>
#                         3. Scrollear a "Resposes" para ver la cantidad de items y porcentaje de contenido Free por año de ese desarrollador.
#                         </font>
#                         """,
#          tags=["Consultas Generales"])
# def developer(desarrollador: str = Query(..., 
#                             description="Desarrollador del videojuego", 
#                             example='Valve')):
#     '''
#     Esta función devuelve información sobre una empresa desarrolladora de videojuegos.
         
#     Args:
#         desarrollador (str): Nombre del desarrollador de videojuegos.
    
#     Returns:
#         dict: Un diccionario que contiene información sobre la empresa desarrolladora.
#             - 'cantidad_por_año' (dict): Cantidad de items desarrollados por año.
#             - 'porcentaje_gratis_por_año' (dict): Porcentaje de contenido gratuito por año según la empresa desarrolladora.
#     '''
#     # Filtra el dataframe por desarrollador de interés
#     data_filtrada = df_items_developer[df_items_developer['developer'] == desarrollador]
#     # Calcula la cantidad de items por año
#     cantidad_por_año = data_filtrada.groupby('release_anio')['item_id'].count()
#     # Calcula la cantidad de elementos gratis por año
#     cantidad_gratis_por_año = data_filtrada[data_filtrada['price'] == 0.0].groupby('release_anio')['item_id'].count()
#     # Calcula el porcentaje de elementos gratis por año
#     porcentaje_gratis_por_año = (cantidad_gratis_por_año / cantidad_por_año * 100).fillna(0).astype(int)

#     result_dict = {
#         'cantidad_por_año': cantidad_por_año.to_dict(),
#         'porcentaje_gratis_por_año': porcentaje_gratis_por_año.to_dict()
#     }
    
#     return result_dict


# @app.get('/sentiment_analysis',
#          description=""" <font color="blue">
#                     INSTRUCCIONES<br>
#                     1. Haga clik en "Try it out".<br>
#                     2. Ingrese el año en box abajo.<br>
#                     3. Scrollear a "Resposes" para ver la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento.
#                     </font>
#                     """,
#          tags=["Consultas Generales"])
# def sentiment_analysis(anio: str = Query(..., 
#                                          description="Año para filtrar los sentimientos de las reseñas", 
#                                          example="2009")):
#     '''
#     Realiza un análisis de sentimiento en base al año ingresado.
    
#     Args:
#         anio (str): El año para filtrar las reseñas.
    
#     Returns:
#         dict: Un diccionario con el recuento de categorías de sentimiento.
#     '''
#     # Filtra las reseñas del año específico
#     anio_reviews = df_reviews[df_reviews['release_anio'] == anio]
    
#     # Inicializa un diccionario para contar las categorías de sentimiento
#     sentiment_counts = {'Negative': 0, 'Neutral': 0, 'Positive': 0}
    
#     # Itera a través de las reseñas del año seleccionado
#     for _, row in anio_reviews.iterrows():
#         sentiment = row['sentiment_analysis']
#         sentiment_category = ''
        
#         # Maneja valores no numéricos en la columna 'release_anio'
#         try:
#             # Asigna la categoría de sentimiento correspondiente
#             if sentiment == 0:
#                 sentiment_category = 'Negative'
#             elif sentiment == 1:
#                 sentiment_category = 'Neutral'
#             elif sentiment == 2:
#                 sentiment_category = 'Positive'
            
#             # Incrementa el contador correspondiente en el diccionario
#             sentiment_counts[sentiment_category] += 1
#         except ValueError:
#             # Maneja el valor no numérico (como 'Sin Dato Disponible')
#             pass
    
#     return sentiment_counts


# @app.get('/recomendacion_juego',
#          description=""" <font color="blue">
#                     INSTRUCCIONES<br>
#                     1. Haga clik en "Try it out".<br>
#                     2. Ingrese el nombre de un juego en box abajo.<br>
#                     3. Scrollear a "Resposes" para ver los juegos recomendados.
#                     </font>
#                     """,
#          tags=["Recomendación"])
# def recomendacion_juego(game: str = Query(..., 
#                                          description="Juego a partir del cuál se hace la recomendación de otros juego", 
#                                          example="Killing Floor")):
#     '''
#     Muestra una lista de juegos similares a un juego dado.

#     Args:
#         game (str): El nombre del juego para el cual se desean encontrar juegos similares.

#     Returns:
#         None: Un diccionario con 5 nombres de juegos recomendados.

#     '''
#     # Obtener la lista de juegos similares ordenados
#     similar_games = item_sim_df.sort_values(by=game, ascending=False).iloc[1:6]

#     count = 1
#     contador = 1
#     recomendaciones = {}
    
#     for item in similar_games:
#         if contador <= 5:
#             item = str(item)
#             recomendaciones[count] = item
#             count += 1
#             contador += 1 
#         else:
#             break
#     return recomendaciones


# @app.get('/recomendacion_usuario',
#          description=""" <font color="blue">
#                     INSTRUCCIONES<br>
#                     1. Haga clik en "Try it out".<br>
#                     2. Ingrese el id del usuario en box abajo.<br>
#                     3. Scrollear a "Resposes" para ver los juegos recomendados para ese usuario.
#                     </font>
#                     """,
#          tags=["Recomendación"])
# def recomendacion_usuario(user: str = Query(..., 
#                                          description="Usuario a partir del cuál se hace la recomendación de los juego", 
#                                          example="76561197970982479")):
#     '''
#     Genera una lista de los juegos más recomendados para un usuario, basándose en las calificaciones de usuarios similares.

#     Args:
#         user (str): El nombre o identificador del usuario para el cual se desean generar recomendaciones.

#     Returns:
#         list: Una lista de los juegos más recomendados para el usuario basado en la calificación de usuarios similares.

#     '''
#     # Verifica si el usuario está presente en las columnas de piv_norm (si no está, devuelve un mensaje)
#     if user not in piv_norm.columns:
#         return('No data available on user {}'.format(user))
    
#     # Obtiene los usuarios más similares al usuario dado
#     sim_users = user_sim_df.sort_values(by=user, ascending=False).index[1:11]
    
#     best = [] # Lista para almacenar los juegos mejor calificados por usuarios similares
#     most_common = {} # Diccionario para contar cuántas veces se recomienda cada juego
    
#     # Para cada usuario similar, encuentra el juego mejor calificado y lo agrega a la lista 'best'
#     for i in sim_users:
#         i = str(i)
#         max_score = piv_norm.loc[:, i].max()
#         best.append(piv_norm[piv_norm.loc[:, i]==max_score].index.tolist())
    
#     # Cuenta cuántas veces se recomienda cada juego
#     for i in range(len(best)):
#         for j in best[i]:
#             if j in most_common:
#                 most_common[j] += 1
#             else:
#                 most_common[j] = 1
    
#     # Ordena los juegos por la frecuencia de recomendación en orden descendente
#     sorted_list = sorted(most_common.items(), key=operator.itemgetter(1), reverse=True)
#     recomendaciones = {} 
#     contador = 1 
#     # Devuelve los 5 juegos más recomendados
#     for juego, _ in sorted_list:
#         if contador <= 5:
#             recomendaciones[contador] = juego 
#             contador += 1 
#         else:
#             break
    
#     return recomendaciones 
#     """