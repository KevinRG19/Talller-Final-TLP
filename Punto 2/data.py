import pandas as pd

df = pd.read_csv('Punto 2/HorrorMovies.csv', quotechar='"', sep=',')


#Primeras 5 filas
print("Primeras 5 filas del DataSet:")
print(df.head(5))
print()

#Longitud del Dataset
print("Longitud del DataSet:")
print(len(df))
print()

#Encabezados
print("Encabezados:")
print(",  ".join(item for item in df.columns.tolist()))
print()

#Películas a partir de 1980
print("Peliculas de 1980 hasta la actualidad:")
recientes = df[df['Movie Year'] >= 1980].copy()
print(recientes)
print()

#Película más corta desde 1980
print("Película más corta desde 1980:")
pelicula_corta = recientes[recientes['Runtime'] == recientes['Runtime'].min()]
print(pelicula_corta)
print()

#Película menos rentable
print("Película menos rentable:")
#Limpiar la columna de recaudo para quitar los símbolos de dinero y puntos decimales
recientes['Gross'] = recientes['Gross'].replace('[$M]','', regex=True)
recientes['Gross'] = pd.to_numeric(recientes['Gross'], errors='coerce')
pelicula_menos_rentable = recientes[recientes['Gross'] == recientes['Gross'].min()] #Encontrar el mínimo
print(pelicula_menos_rentable)
print()

#Promedio de duración de las películas
print("Duración promedio de las películas (Redondeado a 2 decimales):")
print(f"{round(recientes['Runtime'].mean(), 2)} minutos")
print()

#Desviación estándar de la puntuación
print("Desviación estándar de la puntuación:")
print(f"{round(recientes['Rating'].std(), 2)}")
print()

#TODO: Verifíquese si las siguientes OPs son en el dataframe original o en el filtrado
#^^^^^^^^^^Se hizo la pregunta en el grupo de WhatsApp y no hubo respuesta, se asume que es en dataframe original^^^^^^^^^^^

#Promedio de votos por género
print("Promedio de votos por género:")
#Separar los géneros
df['Genre'] = df['Genre'].str.replace(' ', '')
df_generos = df.explode('Genre') if isinstance(df['Genre'].iloc[0], list) else df.assign(Genre=df['Genre'].str.split(',')).explode('Genre')

df_generos["Votes"] = pd.to_numeric(df_generos["Votes"].str.replace(',', ''), errors='coerce') #Limpiar los votos

promedio_por_genero = df_generos.groupby("Genre")["Votes"].mean().sort_values(ascending=False).round(2)

print(promedio_por_genero)
print()

#Número de directores y cuantas películas tiene en el dataset
print("Directores por películas:")
directores = df["Director"].value_counts()
print(directores)
print()

#Mejores películas que sean de género Horror && Mystery && Sci-Fi
print("Mejores películas de Horror, Mystery y Sci-Fi:")
df["Lista_generos"]= df['Genre'].str.lower().str.replace(' ', '').str.split(',')

def peliculas_con_generos(generos):
    return all(genero in generos for genero in ['horror', 'mystery', 'sci-fi'])

peliculas_cumplen = df[df['Lista_generos'].apply(peliculas_con_generos)]

mejores_peliculas = peliculas_cumplen.sort_values(by='Rating', ascending=False)

print(mejores_peliculas.drop(columns=['Lista_generos']))
print()