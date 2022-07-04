def clippingKevin(figura, viewport):

    def dentro(p, c1, c2):
        R = (c2[0] - c1[0]) * (p[1] - c1[1]) - (c2[1] - c1[1]) * (p[0] - c1[0]) 
        if R <= 0:
            return True
        else:
            return False

    def interseccion(s1,s2,c1,c2):
        dc = [ c1[0] - c2[0], c1[1] - c2[1] ]
        dp = [ s1[0] - s2[0], s1[1] - s2[1] ]
        n1 = c1[0] * c2[1] - c1[1] * c2[0]
        n2 = s1[0] * s2[1] - s1[1] * s2[0] 
        n3 = 1.0 / (dc[0] * dp[1] - dc[1] * dp[0])
        return [(n1*dp[0] - n2*dc[0]) * n3, (n1*dp[1] - n2*dc[1]) * n3]

    #Se toma una copia de la figura 
    salida = figura.copy()

    #Por cada lado del viewport, deberá hacerse la comparación con cada lado de la figura dada, y así saber cuales puntos están afuera o adentro
    for i in range(len(viewport)):
        copia = salida.copy()#Copia de la salida para utilizarla como iterador
        salida = [] #Se reinicia el arreglo de salida 

        c1 = viewport[i - 1] #Se toma el punto de inicio del lado del viewport
        c2 = viewport[i] #Se toma el punto final del lado del viewport
        for j in range(len(copia)): #Iterar por cada lado de la figura que está siendo recortada

            s1 = copia[j-1] #Se toma el punto de inicio del lado de la figura recortada
            s2 = copia[j] #Se toma el punto final del lado de la figura recortada
            if dentro(s2,c1,c2): #Se pregunta si el punto final del lado actual (figura) está dentro del área marcada por el lado del viewport
                if not dentro(s1,c1,c2):  #Se pregunta si el punto inicial del lado actual (figura) está fuera del área marcada por el lado del viewport
                    salida.append(interseccion(s1,s2,c1,c2)) #Nuevo punto de la figura recortada respecto a la intersección
                salida.append(s2) #Nuevo punto de la figura recortada, es el punto final del lado actual
            elif dentro(s1,c1,c2): #Se pregunta si el punto inicial del lado actual (figura) está dentro del área marcada por el lado del viewport
                salida.append(interseccion(s1,s2,c1,c2)) #Nuevo punto de la figura recortada respecto a la intersección
            
            #Se tiene al final de cada iteración un arreglo salida que representará la figura recortada debido a los lados del viewport
        
    print(salida)


#Siempre en orden en sentido de las manecillas del reloj
clippingKevin([[3,3],[3,7],[7,7],[7,3]],[[0,0],[0,5],[5,5],[5,0]])