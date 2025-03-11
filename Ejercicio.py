import pandas as pandas
import matplotlib as plotter
datos = pandas.read_csv('./housing.csv')

def tablaFrecuencias(columna):
    columna = pandas.Series(columna)
    return pandas.DataFrame([columna.mean(), columna.median(), columna.mode(), columna.std(), columna.max()-columna.min(), columna.var()], index=['Media', 'Moda', 'Mediana', 'Desviación Estándar', 'Rango', 'Varianza'])

plotter.scatter(datos['median_house_value'][:10], datos['population'][:10])
plotter.xlabel('Proximidad')
plotter.ylabel('Precio')
plotter.tittle('PEPE')

plotter.show()