import numpy as np

# crear una matriz de articulos con:
#   codigo, nombre, stock_actual, stock_minimo_requerido

data = np.array(
    [
        [1234, "celular", 10,20],
        [4234, "tableta", 20,35],
        [1345, "laptop", 4,15],
        [4234, "tableta", 20,20],
        [2341, "smartwatch", 8,25],
    ]
)


def cantidadStock(data):
    diferencia=0
    for i in range(len(data)):
        stockActual=int(data[i,2])
        stockMinimo=int(data[i,3])
        if(stockActual>=stockMinimo):
            diferencia=0
            print("el articulo",data[i,1],"tiene suficiente stock")
        else:
            diferencia=stockMinimo-stockActual
            print("necesitamos pedir",diferencia ,"unidades del articulo",data[i,1])
            

cantidadStock(data)
