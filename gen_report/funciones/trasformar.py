import pandas as pd
from reportlab.pdfgen import canvas

class modelosDatos():
    def __init__(self, DataFrame):
        # Objeto DataFrame (pandas*)
        self.DataFrame = DataFrame

        # Propiedades
        self.columnas = DataFrame.columns

    # getters y setters
    def get_columnas(self):
        return self.columnas
    


    


