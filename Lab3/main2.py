viewport = [(100,100,None),(300,100,None),(300,300,None),(300,120,1),(300, 130,0),(300,170,1),(300,270,0),(100,300,None)]
figura = [(270,120,None),(300,120,1), (400,120,None), (400,270,None), (300,270,0), (270,270,None), (300,170,1), (320,150,None),(300, 130,0)]

originalPolygon = [[400, 120, None], [400, 270, None], [300, 270, 0], [270, 270, None], [300, 170, 1], [320, 150, None], [300, 130, 0], [270, 120, None], [300, 120, 1]]
clippedwindow = [[100, 100, None], [300, 100, None], [300, 120, 1], [300, 130, 0], [300, 170, 1], [300, 270]]

# ingresar los vertices y puntos de interseccion en orden de las manecillas del reloj
## 0 -> entrada 1 -> salida None -> Non intersection point
def WeilerAtherton(originalPolygon):
    resultado = []
    polygon = originalPolygon
    def ordenar(polygon):
        if (polygon[-1][2] != 1):
            polygon.insert(0, polygon[-1])
            polygon.pop()
            ordenar(polygon) 

    ordenar(polygon)

    def sacaPedazoFigura(polygon):
        a = 0
        b = 0
        eYs = []
        poligonosVisibles = []
        for posPareja in range(0,len(polygon)):
            if polygon[posPareja][2] == 0:
                print(posPareja)
                a = a + posPareja
                print("entrada",a)
            if polygon[posPareja][2] == 1 and a > 0:
                b = b + posPareja
                print("salida", b)

                #sacando los puntos entre la entrada (a) y la salida (b)
                while (a <= b):
                    eYs.append(polygon[a])
                    a = a + 1

                a = 0 
                b = 0 
                poligonosVisibles.append(eYs)
                eYs = []
      
        return poligonosVisibles
    resultado = sacaPedazoFigura(polygon)   

        
    print("figuras",resultado)

WeilerAtherton(originalPolygon)
WeilerAtherton(figura)