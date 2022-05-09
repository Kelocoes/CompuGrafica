from proyectil import * 
from vec import * 
import matplotlib as plt
import math 

## programa para simular el lanzamiento de un proyectil hasta r3
intro()



hola = VectorRn([0,1,2])
hola1 = VectorRn([1,0,3])
print(hola.GetVector())
print(hola.Suma(1))
print(hola.Resta(1))
print(hola.Multi(10))
print(hola.Division(100))
print(hola.Norma())
print(hola.ProductoPunto(hola1))
print("El angulo en grado es: " + str(hola.Angulo(hola1)))
print(hola.ProductoCruz(hola1))
print(hola.GetComponente(2))
