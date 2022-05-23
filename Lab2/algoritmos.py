import pygame as pg
import sys

pg.init()
    #clock = pg.time.Clock()

## COLORES
WHITE = (255,255,255)
BLACK = (0, 0, 0)

## conf de pantalla
wn_width = 500
wn_height = 500


screen = pg.display.set_mode((wn_width, wn_height))
pg.display.set_caption("Prueba")
screen.fill(BLACK)


def numerosEntre(x0,xn):
    arr = []
    for i in range(x0,xn+1):
        arr.append(i)

    return arr



class linea():
    def __init__(self,x0,y0,x1,y1,color):
        auxX = -1
        auxY = -1
        if x0 > x1:
            auxX,auxY = x1,y1
            x1,y1 = x0,y0
            x0,y0 = auxX,auxY
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.color = color

    def basic(self):
        m = -(self.y1 - self.y0)/(self.x1 - self.x0)
        y = self.y0
        arr = numerosEntre(self.x0, self.x1)
        #print(self.x0,self.x1)
        for i in range(0,len(arr)):
            pg.draw.rect(screen,self.color,(arr[i],round(y),1,1))
            #print(arr[i],round(y))
            y = y - m
        
        

    def DDA(self):
        #print(self.x0,self.y0,self.x1,self.y1)
        dy = (self.y1 - self.y0)
        dx =(self.x1 - self.x0)
        steps = -1
        if (abs(dx) > abs(dy)):
            steps = abs(dx)
        else:
            steps = abs(dy)

        xincr = abs(dx)/steps
        yincr = abs(dy)/steps

        #print(yincr,dy,steps)
        X = self.x0;
        Y = self.y0;
        #print(steps)
        for i in range(0,steps+1):
            pg.draw.rect(screen,self.color,(round(X),round(Y),1,1))
            X += xincr
            Y -= yincr
    
    def Bresenham(self):
        dy = abs((self.y1 - self.y0))
        dx = abs((self.x1 - self.x0))
        Pk = 2*dy - dx
        #print(dx,dy);

        pg.draw.rect(screen,self.color,(self.x0,self.y0,1,1))
        pg.draw.rect(screen,self.color,(self.x1,self.y1,1,1))
        #print(self.x0,self.y0,self.x1,self.y1)
        X = self.x0
        Y = self.y0
        for i in range(0,dx-1):
            if (Pk < 0):
                Pk = Pk + 2*dy
                X = X + 1
                pg.draw.rect(screen,self.color,(X,Y,1,1))
                #print(X,Y)
            else:
                Pk = Pk + 2*dy - 2*dx
                X = X + 1
                Y = Y - 1
                pg.draw.rect(screen,self.color,(X,Y,1,1))
                #print(X,Y)


class circulo():
    def __init__(self,x0,y0,r,color):
        self.x0 = x0
        self.y0 = y0
        self.r = r
        self.color = color

    def midpoint(self):
        x = self.x0;
        y = self.y0 - self.r;
        p = 1 - self.r;
        r = self.r
        x0 = self.x0
        y0 = self.y0

        pg.draw.rect(screen,self.color,(x,y,1,1))#Up
        pg.draw.rect(screen,self.color,(x,y+2*r,1,1))#Down
        pg.draw.rect(screen,self.color,(x-r,y+r,1,1))#Left
        pg.draw.rect(screen,self.color,(x+r,y+r,1,1))#Right
        #print(x,y);

        while (x-x0 < y0 - y - 1):
            #print(p,x,y)
            if (p < 0):
            #print("Entre1");
                p = p + 2 * (x-x0) + 1;
                x = x + 1;
            else:
            #print("Entre2",y-y0,x-x0);
                p = p - 2 * (y0-y) + 2 * (x-x0);
                x = x + 1;
                y = y + 1;
            pg.draw.rect(screen, self.color, (x,y,1,1))#Cuad 1.1
            pg.draw.rect(screen, self.color, (x-2*(x-x0),y,1,1))#Cuad 2.1
            pg.draw.rect(screen, self.color, (x-2*(x-x0),y + 2*(y0-y),1,1))#Cuad 3.1
            pg.draw.rect(screen, self.color, (x,y + 2*(y0-y),1,1))#Cuad 4.1
            pg.draw.rect(screen, self.color, (x0 + (y0 -  y),y0 - (x-x0),1,1))#Cuad 1.2
            pg.draw.rect(screen, self.color, (x0 - (y0 -  y),y0 - (x-x0),1,1))#Cuad 2.2
            pg.draw.rect(screen, self.color, (x0 - (y0 -  y),y0 + (x-x0),1,1))#Cuad 3.2
            pg.draw.rect(screen, self.color, (x0 + (y0 -  y),y0 + (x-x0),1,1))#Cuad 4.2

    def BresenhamCircle(self):
        r = self.r
        x0 = self.x0
        y0 = self.y0
        x = x0
        y = y0 - r
        d = 3 - (2 * r)
        pg.draw.rect(screen,self.color,(x,y,1,1))#Up
        pg.draw.rect(screen,self.color,(x,y+2*r,1,1))#Down
        pg.draw.rect(screen,self.color,(x-r,y+r,1,1))#Left
        pg.draw.rect(screen,self.color,(x+r,y+r,1,1))#Right
        #print(x,y);
        while (x - x0 < y0 - y - 1):
            x = x + 1;
            if (d < 0):
                d = d + 4*(x-x0) + 6
            else:
                d = d + 4*((x-x0) - (y0-y)) + 10
                y = y + 1
            pg.draw.rect(screen, self.color, (x,y,1,1))#Cuad 1.1
            pg.draw.rect(screen, self.color, (x-2*(x-x0),y,1,1))#Cuad 2.1
            pg.draw.rect(screen, self.color, (x-2*(x-x0),y + 2*(y0-y),1,1))#Cuad 3.1
            pg.draw.rect(screen, self.color, (x,y + 2*(y0-y),1,1))#Cuad 4.1
            pg.draw.rect(screen, self.color, (x0 + (y0 -  y),y0 - (x-x0),1,1))#Cuad 1.2
            pg.draw.rect(screen, self.color, (x0 - (y0 -  y),y0 - (x-x0),1,1))#Cuad 2.2
            pg.draw.rect(screen, self.color, (x0 - (y0 -  y),y0 + (x-x0),1,1))#Cuad 3.2
            pg.draw.rect(screen, self.color, (x0 + (y0 -  y),y0 + (x-x0),1,1))#Cuad 4.2
            #print(x,y)



def window():
    
    
    running = True
    while running:
        #linea1 = linea(50,50,100,25,WHITE)
        #linea1.Bresenham()
        #linea2 = linea(50,50,100,25,"red")
        #linea2.DDA()
        # linea3 = linea(200,300,250,250)
        # linea3.Bresenham()
        #ar = circulo(100,100,50,WHITE)
        #ar.midpoint()
        #ar2 = circulo(300,300,50,(255,0,0))
        #ar2.BresenhamCircle()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if running == False:
                pg.quit()
                sys.exit()
        pg.display.update() 
