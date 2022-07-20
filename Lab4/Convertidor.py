
def RGB_to_RBG_Normalized(R, G, B):
    print("RGB to RGB Normalized")
    Rprima = R/255
    Gprima = G/255
    Bprima = B/255
    print("Rprima " + str(Rprima))
    print("Gprima " + str(Gprima))
    print("Bprima " + str(Bprima))
    return Rprima, Gprima, Bprima

def RGB_Normalized_to_RGB(R, G, B):
    print("RGB Normalized to RGB")
    R = R*255
    G = G*255
    B = B*255
    print("R " + str(R))
    print("G " + str(G))
    print("B " + str(B))
    return R, G, B

def RGB_to_CMY(R, G, B):
    print("RGB to CMY")
    C = 1-R
    M = 1-G
    Y = 1-B
    print("C " + str(C))
    print("M " + str(M))
    print("Y " + str(Y))
    return C, M , Y

def CMY_to_RGB(C, M, Y):
    print("CMY to RGB")
    R = 1-C
    G = 1-M
    B = 1-Y
    print("R " + str(R))
    print("G " + str(G))
    print("B " + str(B))
    return R, G, B

def CMY_to_CMYK(C, M, Y):
    print("CMY to CMYK")
    K = min(C, M, Y)
    C = (C - K) / (1 - K)
    M = (M - K) / (1 - K)
    Y = (Y - K) / (1 - K)
    print("K " + str(K))
    print("C " + str(C))
    print("M " + str(M))
    print("Y " + str(Y))
    return K, C, M, Y

def CMYK_to_CMY(K, C, M, Y):
    print("CMYK to CMY")
    C = min(1, C * (1 - K) + K)
    M = min(1, M * (1 - K) + K)
    Y = min(1, Y * (1 - K) + K)
    print("C " + str(C))
    print("M " + str(M))
    print("Y " + str(Y))
    return C, M, Y

def RGB_to_YIQ(R, G, B):
    print("RGB to YIQ")
    Y = (0.299 * R + 0.587 * G + 0.114 * B) 
    I = (0.595716 * R - 0.274453 * G - 0.321263 * B)
    Q = (0.211456 * R - 0.522591 * G + 0.311135 * B)
    print("Y " + str(Y))
    print("I " + str(I))
    print("Q " + str(Q))
    return Y, I, Q

def YIQ_to_RGB(Y, I, Q):
    print("YIQ to RGB")
    R = ( Y + 0.9563 * I + 0.6210 * Q)
    G = ( Y - 0.2721 * I - 0.6474 * Q)
    B = ( Y - 1.1070 * I + 1.7046 * Q)
    print("R " + str(R))
    print("G " + str(G))
    print("B " + str(B))
    return R, G, B

def RGB_to_HSV(R, G, B):
    print("RGB to HSV")
    CMax = max(R, G, B)
    CMin = min(R, G, B)
    Delta = CMax - CMin
    if (Delta == 0):
        H = 0
    elif (CMax == R):
        H = 60 * (((G-B)/Delta) % 6)
    elif (CMax == G):
        H = 60 * (((B-R)/Delta) + 2)
    else:
        H = 60 * (((R-G)/Delta) + 4)
    S = (0 if CMax == 0 else Delta/CMax)
    V = CMax
    print("H " + str(H))
    print("S " + str(S))
    print("V " + str(V))
    return H, S, V

def HSV_to_RGB(H, S, V):
    print("HSV to RGB")
    C = V * S
    X = C * (1 - abs(((H/60) % 2) - 1))
    m = V - C
    if (0 <= H < 60):
        R = C; G = X; B = 0
    elif (60 <= H < 120):
        R = X; G = C; B = 0
    elif (120 <= H < 180):
        R = 0; G = C; B = X
    elif (180 <= H < 240):
        R = 0; G = X; B = C
    elif (240 <= H < 300):
        R = X; G = 0; B = C
    elif (300 <= H < 360):
        R = C; G = 0; B = X

    R = (R + m) * 255
    G = (G + m) * 255
    B = (B + m) * 255
    print("R " + str(R))
    print("G " + str(G))
    print("B " + str(B))
    return R, G, B

def RGB_to_HSL(R, G, B):
    print("RGB to HSL")
    CMax = max(R, G, B)
    CMin = min(R, G, B)
    Delta = CMax - CMin
    if (Delta == 0):
        H = 0
    elif (CMax == R):
        H = 60 * (((G-B)/Delta) % 6)
    elif (CMax == G):
        H = 60 * (((B-R)/Delta) + 2)
    else:
        H = 60 * (((R-G)/Delta) + 4)
    L = (CMax + CMin) / 2
    S = 0 if Delta == 0 else (Delta/(1 - abs(2*L - 1)))
    print("H " + str(H))
    print("S " + str(S))
    print("L " + str(L))

def HSL_to_RGB(H, S, L):
    print("HSL to RGB")
    C = (1 - abs(2*L - 1)) * S
    X = C * (1 - abs(((H/60) % 2) - 1))
    m = L - C/2
    if (0 <= H < 60):
        R = C; G = X; B = 0
    elif (60 <= H < 120):
        R = X; G = C; B = 0
    elif (120 <= H < 180):
        R = 0; G = C; B = X
    elif (180 <= H < 240):
        R = 0; G = X; B = C
    elif (240 <= H < 300):
        R = X; G = 0; B = C
    elif (300 <= H < 360):
        R = C; G = 0; B = X

    R = (R + m) * 255
    G = (G + m) * 255
    B = (B + m) * 255
    print("R " + str(R))
    print("G " + str(G))
    print("B " + str(B))
    return R, G, B


R = 12; G = 12; B = 12
R, G, B = RGB_to_RBG_Normalized(R, G , B)
RGB_to_HSV(R, G, B)

H = 212; S = 0.94; V = 0.78431
HSV_to_RGB(H, S, V)

R = 160; G = 255; B = 50
R, G, B = RGB_to_RBG_Normalized(R, G , B)
RGB_to_HSL(R, G, B)

H = 88; S = 1; L = 0.5980
HSL_to_RGB(H, S, L)

R = 80; G = 35; B = 98
R, G, B = RGB_to_RBG_Normalized(R, G , B)
RGB_to_CMY(R, G, B)

C = 0.3529; M = 0.80039; Y = 0.5294
R, G, B = CMY_to_RGB(C, M, Y)
RGB_Normalized_to_RGB(R, G, B)