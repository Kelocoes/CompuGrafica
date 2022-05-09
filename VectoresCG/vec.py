import math


class VectorRn():
    def __init__(self,vector):
        self.vector = vector
        self.n = len(vector)

    def GetComponente(self,pos):
        if pos >= len(self.vector):
            return "Posicion incorrecta"
        else:
            return self.vector[pos]

    def GetVector(self):
        return self.vector

    def Suma(self,f):
        return [x+f for x in self.vector]

    def Resta(self,f):
        return [x-f for x in self.vector]

    def Multi(self,f):
        return [x*f for x in self.vector]

    def Division(self,f): 
        return [x/f for x in self.vector]

    def Norma(self):
            aux = 0
            for j in self.vector:
                aux += j**2
            return aux ** 0.5

    def ProductoPunto(self,f2):
        vector2 = f2.GetVector()
        result = 0
        for i in range(0,len(vector2)):
            result += self.GetVector()[i]*vector2[i]
        return result

    def Angulo(self,f2):
        return math.acos((self.ProductoPunto(f2))/(self.Norma() * f2.Norma()))*(180/math.pi)

    def ProductoCruz(self,f2):
        v2 = f2.GetVector()
        if len(v2) == len(self.GetVector()):
            if len(self.GetVector()) != 3  :
                return "Oops, tamaño no válido"
            else: 
                return  [self.GetVector()[1]*v2[2] - self.GetVector()[2]*v2[1],
                        self.GetVector()[2]*v2[0] - self.GetVector()[0]*v2[2],
                        self.GetVector()[0]*v2[1] - self.GetVector()[1]*v2[0]]
        else:
            return "Oops, error, diferente tamaño entre los vectores"




