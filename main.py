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
    Hola comunidad Henry, para mi un gusto mostrar el desarrollo de las funciones solicitadas.
    Gracias por estar acá.

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



@app.get(path = '/developer')
def developer(desarrollador: str = Query(..., 
                             description="Desarrollador", 
                             example='Kotoshiro')):
     '''
     Esta función devuelve la cantidad de items desarrollados y la de contenido gratuito según el desarrollador ingresado.
         

     '''

     data_filtrada = df_items_developer[df_items_developer['developer'] == desarrollador]

     cantidad_por_año = data_filtrada.groupby('release_anio')['item_id'].count()

     cantidad_gratis_por_año = data_filtrada[data_filtrada['price'] == 0.0].groupby('release_anio')['item_id'].count()

     porcentaje_gratis_por_año = (cantidad_gratis_por_año / cantidad_por_año * 100).fillna(0).astype(int)

     result_dict = {
         'cantidad_por_año': cantidad_por_año.to_dict(),
         'porcentaje_gratis_por_año': porcentaje_gratis_por_año.to_dict()
     }
    
     return result_dict


 @app.get('/sentiment_analysis')
def sentiment_analysis(anio: str = Query(..., 
                                          description="Ingrese un año", 
                                          example="2011")):
     '''
     Realiza un análisis de sentimiento según el año ingresado.
    
     '''

     anio_reviews = df_reviews[df_reviews['release_anio'] == anio]
    

     sentiment_counts = {'Negative': 0, 'Neutral': 0, 'Positive': 0}
    

     for _, row in anio_reviews.iterrows():
         sentiment = row['sentiment_analysis']
         sentiment_category = ''
        

         try:

             if sentiment == 0:
                 sentiment_category = 'Negative'
             elif sentiment == 1:
                 sentiment_category = 'Neutral'
             elif sentiment == 2:
                 sentiment_category = 'Positive'
            

             sentiment_counts[sentiment_category] += 1
         except ValueError:

             pass
    
     return sentiment_counts