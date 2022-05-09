import math
from vec import VectorRn as vr 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

tiempo = []
class Proyectil():
    def __init__(self,vector):
        self.vector = vr.GetVector(vector)
        self.rn = len(vr.GetVector(vector))
        self.velocidad = 0
        self.posiciones = []

    def setVector(self, vector): 
        self.vector = vector

    def getVector(self): 
        return self.vector

    def setPosiciones(self, vector): 
        self.posiciones.append(vector)
      
    def GetPosiciones(self):
        return self.posiciones

    def setVelocidad(self, vel): 
        self.velocidad =  vel
    
    def GetVelocidad(self): 
        return self.velocidad

## funcion intro: Recibe los datos iniciales
def intro(): 
  print("Ingrese el espacio en que quiere calcular el lanzamiento [1,2,3]")
  Rn = int(input())
  print("Ingrese la velocidad inicial ")
  vel = float(input())
  print("Ingrese posicion inicial en x")
  posx = float(input())
  posy = 0
  posz = 0
  print("Ingrese el delta t (segundos) de la periocidad de las posiciones: ")
  dt = float(input())
  print("Ingrese posicion inicial en y")
  posy = float(input())
  if (Rn == 1): 
    lanzar(Proyectil(vr([posx, posy, posz])), math.radians(90),vel, dt)
  elif (Rn == 2 or Rn == 3): 
    if (Rn == 3): 
      print("Ingrese posicion inicial en z")
      posz = float(input())
      print("Ingrese el angulo phi (de rotacion)")
      angulophi = float(input())
    print("Ingrese el angulo de lanzamiento (en grados): ")
    angulo = float(input())
    angulo = (angulo * math.pi)/180 ## Conversion a radian  

    if (Rn == 3):
      anguloteta = angulo
      angulophi = (angulophi * math.pi)/180 
      lanzarR3(Proyectil(vr([posx, posy, posz])), anguloteta, angulophi, vel, dt)
    else:
      lanzar(Proyectil(vr([posx, posy, posz])), angulo, vel, dt)
  else: 
    print("Datos erroneos")
    exit(0)

def calculaY(posInicial, velocidad, angulo, tiempo): 
  posy = posInicial + velocidad*math.sin(angulo)*tiempo - ((1/2)*9.8* tiempo**2)
  return posy
  


def lanzarR3(proj,anguloteta, angulophi, velocidad, dt):
  a = math.cos(anguloteta)
  b = math.sin(anguloteta)

  if (anguloteta  == math.pi/2):
    a = 0
    b = 1

  print("Es la hora de lanzar!")
  tiempoVuelo = (2*velocidad*b)/9.8
  Proyectil.setVelocidad(proj, velocidad)
  pos = [Proyectil.getVector(proj)[i] for i in range(3)]
  tiempo.append(0)
  Proyectil.setPosiciones(proj, vr(pos))
  i = 0 

  posx0 = pos[0]
  posy0 = pos[1]
  while True: 
    posx = pos[0] + Proyectil.GetVelocidad(proj) * a * i
    aux = posx
    aux1 = pos[1]
    print("HOLAAA111111", aux,aux1)
    posx = (aux-posx0)*math.cos(angulophi) - (aux1-posy0)*math.sin(angulophi)
    posy = (aux-posx0)*math.sin(angulophi) + (aux1-posy0)*math.cos(angulophi)
    posz = calculaY(pos[2], Proyectil.GetVelocidad(proj), anguloteta, i)
    posz1 = calculaY(pos[2], Proyectil.GetVelocidad(proj), anguloteta, i+dt)
    print("Hola2222", posx,posy)
    

    
    Proyectil.setPosiciones(proj, vr([posx, posy, posz]))
    i = i + dt
    tiempo.append(i)
    if (int(posz1) <= 0 and i >= tiempoVuelo): 
      t = ( (Proyectil.GetVelocidad(proj)*b + math.sqrt((Proyectil.GetVelocidad(proj)*b)**2 + 2*9.8*pos[2]))/9.8)
      posx = pos[0] + Proyectil.GetVelocidad(proj) * a * t
      aux = posx
      aux1 = pos[1]
      print("HOLA", aux,aux1)
      posx = (aux-posx0)*math.cos(angulophi) - (aux1-posy0)*math.sin(angulophi)
      posy = (aux-posx0)*math.sin(angulophi) + (aux1-posy0)*math.cos(angulophi)
      posz = 0
      Proyectil.setPosiciones(proj, vr([posx, posy, posz]))
      i = i + t
      print("TERMINE")
      for y in range(len(Proyectil.GetPosiciones(proj))): 
              print("-- ITERACION: " + str(y) )
              print("     posx " + str(vr.GetVector(Proyectil.GetPosiciones(proj)[y])[0]))
              print("     posy " + str(vr.GetVector(Proyectil.GetPosiciones(proj)[y])[1]))
              print("     posz " + str(vr.GetVector(Proyectil.GetPosiciones(proj)[y])[2]))
      print(" --- TIEMPO DE VUELO: " + str(tiempo[len(tiempo)-2]))
      mostrar3(proj)
      break
  print(" **** Simulacion terminada  ****")

def lanzar(proj, angulo, velocidad, dt): 
  a = math.cos(angulo)
  b = math.sin(angulo)
  if (angulo  == math.pi/2):
    a = 0
    b = 1
    
  print("Es la hora de lanzar!")
  tiempoVuelo = (2*velocidad*b)/9.8
  Proyectil.setVelocidad(proj, velocidad)
  pos = [Proyectil.getVector(proj)[i] for i in range(3)]
  tiempo.append(0)
  Proyectil.setPosiciones(proj, vr(pos))
  i = 0 

  while True: 
    posx = pos[0] + Proyectil.GetVelocidad(proj) * a * i
    posy = calculaY(pos[1], Proyectil.GetVelocidad(proj), angulo, i)
    posy1 = calculaY(pos[1], Proyectil.GetVelocidad(proj), angulo, i+dt)
    posz = pos[2]
    Proyectil.setPosiciones(proj, vr([posx, posy, posz]))
    i = i + dt
    tiempo.append(i)
    if (int(posy1) <= 0 and i >= tiempoVuelo): 
      t = ( (Proyectil.GetVelocidad(proj)*b + math.sqrt((Proyectil.GetVelocidad(proj)*b)**2 + 2*9.8*pos[1]))/9.8)
      posx = pos[0] + Proyectil.GetVelocidad(proj) * a * t
      posy = 0
      posz = pos[2]
      Proyectil.setPosiciones(proj, vr([posx, posy, posz]))
      i = i + t
      print("TERMINE")
      for y in range(len(Proyectil.GetPosiciones(proj))): 
        print("-- ITERACION: " + str(y) )
        print("     posx " + str(vr.GetVector(Proyectil.GetPosiciones(proj)[y])[0]))
        print("     posy " + str(vr.GetVector(Proyectil.GetPosiciones(proj)[y])[1]))
        print("     posz " + str(vr.GetVector(Proyectil.GetPosiciones(proj)[y])[2]))
      print(" --- TIEMPO DE VUELO: " + str(tiempo[len(tiempo)-2]))
      mostrar(proj)
      break
  print(" **** Simulacion terminada  ****") 
      

def mostrar(proj): 
  x = []
  y = []
  for i in Proyectil.GetPosiciones(proj): 
      plt.scatter(vr.GetVector(i)[0], vr.GetVector(i)[1])
      x.append(vr.GetVector(i)[0])
      y.append(vr.GetVector(i)[1])
  plt.plot(x, y)
  plt.xlabel("pos x")
  plt.ylabel("pos y")
  plt.title("Esquema: Movimiento en Rn")
  
  plt.show()


def mostrar3(proj): 
  fig = plt.figure(figsize=(4,4))
  ax = fig.add_subplot(111, projection='3d')

  for i in Proyectil.GetPosiciones(proj): 

      #print(vr.GetVector(i)[0], vr.GetVector(i)[1], vr.GetVector(i)[2])
      ax.scatter(vr.GetVector(i)[0], vr.GetVector(i)[1], vr.GetVector(i)[2])

  #plt.plot()
  #plt.xlabel("pos x")
  #plt.ylabel("pos z")
  plt.title("Esquema: Movimiento en R3")
  
  plt.show()