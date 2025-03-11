import pandas as pandas
import matplotlib.pyplot as plotter

datos = pandas.read_csv('./housing.csv')
nombresColumnas = ['longitude', 'latitude', 'housing_median_age','total_rooms',	'total_bedrooms', 'population', 'households', 'median_income', 'median_house_value']

def tablaFrecuencias(columna):
    columna = pandas.Series(columna)
    return pandas.DataFrame([columna.mean(), columna.median(), columna.mode().iloc[0], columna.std(), columna.max()-columna.min(), columna.var()], index=['Media', 'Moda', 'Mediana', 'Desviación Estándar', 'Rango', 'Varianza'])

for i in range(0, len(nombresColumnas)):
    print("Medidas estadísticas de la columna:", nombresColumnas[i], "\n", tablaFrecuencias(datos[nombresColumnas[i]]))

plotter.bar(datos['population'][:10000], datos['median_house_value'][:10000], width=500)
plotter.xlabel('Poblacion')
plotter.ylabel('Precio de la vivienda')
plotter.title('Población y precio de la vivienda')
plotter.show()
