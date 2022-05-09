# Desarrollo de la actividad No.3 Taller 1

Utilizando POO (Programación Orientado a Objetos) implemente una o varias clases en C++, Python o Javascript que cumplan con las siguientes características:

[10%] Modele un vector en Rn, con n en {1,2,3} dimensiones en coordenadas cartesianas.
[20%] Implementar las siguientes operaciones.

-Suma, resta y multiplicación de un vector por un escalar.

-Multiplicación de vectores (cross product). 

-Producto interno (producto punto).

-División de un vector por un escalar.

-Calcular ángulo entre dos vectores.

-Normalización de vectores.

[20%] Cree una aplicación que simule el lanzamiento de proyectil en Rn, con n en {1,2,3} se debe considerar:

-La velocidad inicial del proyectil en Rn y el intervalo de tiempo Δt.

-La posición inicial del proyectil.

-El cálculo de todas las posiciones del proyectil cada Δt segundos hasta que el proyectil tenga altura cero.



## Clase vector

Dentro de la clase vector se encuentra la construcción del mismo y sus atributos y operaciones primitivas.

## Operadores como funciones

Los operadores que necesiten de otros vectores para su realización están separados de la clase vector, ya que no son inherentes a un vector en sí. Entre estos están:

-Angulo entre vectores

-Producto punto entre vectores

-Multiplicación entre vectores