
import pandas as pd
from matplotlib import pyplot as plt


def get_graficas(Dataframe):
    graficas = []

    grafica_barras = plt.bar(Dataframe.loc[:, 'Nombre del anuncio'], Dataframe.loc[:, 'Resultados'])
    
    graficas.append(grafica_barras)

    grafica_alcance = plt.pie(Dataframe.loc['Nombre del anuncio', 'Alcance'])
    graficas.append(grafica_alcance)


    return graficas
