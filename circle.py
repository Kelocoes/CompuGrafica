
def pmCircle(x0,y0,r):
    p = 1 - r 

    x = x0
    y = y0 + r
    print(p,x,y)
    while (x-x0) < (y-y0)  - 1 :
        
        if p < 0:
            p = p + 2 * (x-x0) + 1
            x += 1
        else:        
            p = p - 2 * (y-y0) + 2 * (x-x0)
            y -= 1
            x += 1
        print(p,x,y)

def bresenhCircle(x0,y0,r):
    x = 0
    y = r
    d = 3 - 2 * r

    print(x,y)
    while x-x0 < y-y0 - 1:
        x = x + 1
        if d < 0:
            d = d + 4 * x + 6
        else:
            d = d + 4 * (x - y) + 10
            y = y - 1
        print(x,y)



def basicline(x0,y0,x1,y1):
    m = (y1-y0)/(x1-x0)
    y = y0
    x = x0
    while y != y1 + 1:
        print(x,round(y))
        x = x + 1
        y = y + m

def dda(x0,y0,x1,y1):
    dy = y1 - y0
    dx = x1 - x0
    if (dx > dy):
        steps = abs(dx)
    else:
        steps = abs(dy)
    
    xincr = dx / steps
    yincr = dy / steps

    x = x0
    y = y0

    for i in range(steps+1):
        print(round(x),round(y));
        x += xincr
        y += yincr

def bresenLine(x0,y0,x1,y1):
    dy = y1 - y0
    dx = x1 - x0
    p = 2*dy - dx

    x = x0
    y = y0

    print(x,y)
    for i in range(0,dx):
        if p < 0:
            p = p + 2*dy
            x = x + 1
        else:
            p = p + 2*dy  - 2*dx
            x = x + 1
            y = y + 1
        print(x,y)


#basicline(-2,-1,3,4)
#dda(3,4,7,9)
#bresenLine(9,18,14,22)
pmCircle(0,0,5)
#bresenhCircle(0,0,10)


