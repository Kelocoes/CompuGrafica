import pygame, sys, pygame_textinput 
from button import Button
from algoritmos import circulo
from algoritmos import linea
pygame.init()


SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def menu_linea():
    while True:
        LINEA_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        LINEA_TEXT = get_font(30).render("SELECCIONE EL ALGORITMO DE LINEA:", True, "White")
        LINEA_RECT = LINEA_TEXT.get_rect(center=(640, 260))


        SCREEN.blit(LINEA_TEXT,LINEA_RECT)
        
        ## botones

        LINEA_BASICO = Button(image = None, pos=(640, 360), 
                            text_input = "Basico", font=get_font(25), base_color="White", hovering_color = "Green")
        
        LINEA_DDA = Button(image = None, pos=(640, 400), 
                            text_input= "DDA", font=get_font(25), base_color="White", hovering_color = "Green")
        
        LINEA_BRESSENHAM = Button(image = None, pos=(640, 440), 
                            text_input= "BRESSENHAM", font=get_font(25), base_color="White", hovering_color = "Green")

        LINEA_BACK = Button(image=None, pos=(640, 640), 
                            text_input="ATRAS", font=get_font(25), base_color="White", hovering_color="Green")

    
        for button in [LINEA_BASICO, LINEA_DDA, LINEA_BRESSENHAM, LINEA_BACK]: 
            button.changeColor(LINEA_MOUSE_POS)
            button.update(SCREEN)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LINEA_BASICO.checkForInput(LINEA_MOUSE_POS): 
                    general_linea(1)
                if LINEA_DDA.checkForInput(LINEA_MOUSE_POS): 
                    general_linea(2)
                if LINEA_BRESSENHAM.checkForInput(LINEA_MOUSE_POS): 
                    general_linea(3)
                if LINEA_BACK.checkForInput(LINEA_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def general_linea(opcion):
    posit = []
    #MANEJADOR DE LA LIBRERIS
    manager = pygame_textinput.TextInputManager(validator = lambda input: len(input) <= 50)

    #CREAR VISUALIZADOR DE TEXTO 
    textinput = pygame_textinput.TextInputVisualizer()
    textinput.font_color = "White"
    textinput.cursor_color = "White"
    textinput.font_object = get_font(30)
    textinput.manager = manager

    clock = pygame.time.Clock()

    
    while True:
        MID_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("Black")
        
        LINEA_TEXT = get_font(30).render("Ingrese coordenadas iniciales x0 y0 xn yn" , True, "White")
        LINEA2_TEXT = get_font(30).render("(separados por comas)", True, "White")
        LINEA_RECT = LINEA_TEXT.get_rect(center=(640, 260))
        LINEA_RECT2 = LINEA2_TEXT.get_rect(center=(640, 300))

        SCREEN.blit(LINEA_TEXT,LINEA_RECT)
        SCREEN.blit(LINEA2_TEXT,LINEA_RECT2)

        ## visualizacion de entradas al teclado 
        events = pygame.event.get()
        textinput.update(events)
        SCREEN.blit(textinput.surface, (440, 360))

        #OPCION DE INGRESAR
        OPTIONS_INPUT = Button(image=None, pos=(640, 460), text_input="INGRESAR", font=get_font(25), base_color="White", hovering_color="Green")
         
        ## OPCION DE VOLVER
        OPTIONS_BACK = Button(image=None, pos=(640, 660), text_input="VOLVER", font=get_font(25), base_color="White", hovering_color="Green")

        for button in [OPTIONS_INPUT, OPTIONS_BACK]: 
            button.changeColor(MID_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(MID_MOUSE_POS):
                    main_menu()
                if OPTIONS_INPUT.checkForInput(MID_MOUSE_POS):
                    posit = [int(i) for i in manager.value.split(",")]
                    if (opcion == 1): 
                        print("Basico")
                        linea1 = linea(posit[0],posit[1],posit[2],posit[3],"white")
                        running = True
                        while running:
                            SCREEN.fill("black")
                            linea1.basic()
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    running = False
                                if running == False:
                                    pygame.quit()
                                    sys.exit()
                            pygame.display.update() 
                    if (opcion == 2): 
                        print("DDA")
                        linea1 = linea(posit[0],posit[1],posit[2],posit[3],"white")
                        running = True
                        while running:
                            SCREEN.fill("black")
                            linea1.DDA()
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    running = False
                                if running == False:
                                    pygame.quit()
                                    sys.exit()
                            pygame.display.update() 
                    if (opcion == 3):  
                        print("Bressenham")
                        linea1 = linea(posit[0],posit[1],posit[2],posit[3],"white")
                        running = True
                        while running:
                            SCREEN.fill("black")
                            linea1.Bresenham()
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    running = False
                                if running == False:
                                    pygame.quit()
                                    sys.exit()
                            pygame.display.update() 
                    print(posit)

        pygame.display.update()
        clock.tick(30)

def linea_dda(): 
    return "hi"
def linea_bress(): 
    return "hi"
    
def options():
    while True:
        #POSICION DEL MOUSE EN LA PANTALLA
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")
        #TITULO
        OPTIONS_TEXT = get_font(30).render("SELECCIONE EL ALGORITMO DE CIRCUFERENCIA", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        
        #OPCION ALGORITMO PUNTO MEDIO 
        OPTIONS_MID_POINT = Button(image=None, pos=(640, 360), 
                            text_input="ALGORITMO PUNTO MEDIO", font=get_font(25), base_color="Black", hovering_color="Green")

        OPTIONS_MID_POINT.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_MID_POINT.update(SCREEN)

        #OPCION ALGORITMO BRESENHAM 
        OPTIONS_BRESENHAM = Button(image=None, pos=(640, 400), 
                            text_input="ALGORITMO BRESENHAM", font=get_font(25), base_color="Black", hovering_color="Green")

        OPTIONS_BRESENHAM.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BRESENHAM.update(SCREEN)


        #OPCION DE VOLVER
        OPTIONS_BACK = Button(image=None, pos=(640, 640), 
                            text_input="VOLVER", font=get_font(25), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                if OPTIONS_MID_POINT.checkForInput(OPTIONS_MOUSE_POS):
                    mid_point()
                if OPTIONS_BRESENHAM.checkForInput(OPTIONS_MOUSE_POS):
                    bresenham()

        pygame.display.update()

def mid_point():
    #MANEJADOR DE LA LIBRERIS
    manager = pygame_textinput.TextInputManager(validator = lambda input: len(input) <= 15)

    #CREAR VISUALIZADOR DE TEXTO 
    textinput = pygame_textinput.TextInputVisualizer()
    textinput.font_object = get_font(30)
    textinput.manager = manager

    clock = pygame.time.Clock()


    while True: 
        #POSICION DEL MOUSE EN LA PANTALLA
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("white")

        #TITULO
        LINEA_TEXT = get_font(20).render("Ingrese coordenadas del centro y el radio x0 y0 r" , True, "black")
        LINEA2_TEXT = get_font(20).render("(separados por comas)", True, "black")
        LINEA_RECT = LINEA_TEXT.get_rect(center=(640, 260))
        LINEA_RECT2 = LINEA2_TEXT.get_rect(center=(640, 300))

        SCREEN.blit(LINEA_TEXT,LINEA_RECT)
        SCREEN.blit(LINEA2_TEXT,LINEA_RECT2)

        
        events = pygame.event.get()
        textinput.update(events)
        SCREEN.blit(textinput.surface, (340, 360))

        #OPCION DE INGRESAR
        OPTIONS_INPUT = Button(image=None, pos=(640, 460), text_input="INGRESAR", font=get_font(20), base_color="Black", hovering_color="Green")

        OPTIONS_INPUT.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_INPUT.update(SCREEN)        

        #OPCION DE VOLVER
        OPTIONS_BACK = Button(image=None, pos=(640, 660), text_input="VOLVER", font=get_font(20), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                if OPTIONS_INPUT.checkForInput(OPTIONS_MOUSE_POS):
                    print(str(manager.value))
                    arr = str(manager.value).split(",")
                    circulo1 = circulo(int(arr[0]),int(arr[1]),int(arr[2]),"white")
                    running = True
                    while running:
                        SCREEN.fill("black")
                        circulo1.midpoint()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                running = False
                            if running == False:
                                pygame.quit()
                                sys.exit()
                        pygame.display.update() 
        pygame.display.update()

        clock.tick(30)


def bresenham():
    #MANEJADOR DE LA LIBRERIS
    manager = pygame_textinput.TextInputManager(validator = lambda input: len(input) <= 15)

    #CREAR VISUALIZADOR DE TEXTO 
    textinput = pygame_textinput.TextInputVisualizer()
    textinput.font_object = get_font(30)
    textinput.manager = manager

    clock = pygame.time.Clock()


    while True: 
        #POSICION DEL MOUSE EN LA PANTALLA
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("white")

        #TITULO 
        LINEA_TEXT = get_font(20).render("Ingrese coordenadas del centro y el radio x0 y0 r" , True, "black")
        LINEA2_TEXT = get_font(20).render("(separados por comas)", True, "black")
        LINEA_RECT = LINEA_TEXT.get_rect(center=(640, 260))
        LINEA_RECT2 = LINEA2_TEXT.get_rect(center=(640, 300))

        SCREEN.blit(LINEA_TEXT,LINEA_RECT)
        SCREEN.blit(LINEA2_TEXT,LINEA_RECT2)


        events = pygame.event.get()
        textinput.update(events)
        SCREEN.blit(textinput.surface, (340, 360))

        #OPCION DE INGRESAR
        OPTIONS_INPUT = Button(image=None, pos=(640, 460), text_input="INGRESAR", font=get_font(20), base_color="Black", hovering_color="Green")

        OPTIONS_INPUT.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_INPUT.update(SCREEN)        

        #OPCION DE VOLVER
        OPTIONS_BACK = Button(image=None, pos=(640, 660), text_input="VOLVER", font=get_font(20), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                if OPTIONS_INPUT.checkForInput(OPTIONS_MOUSE_POS):
                    print(str(manager.value))
                    arr = str(manager.value).split(",")
                    circulo1 = circulo(int(arr[0]),int(arr[1]),int(arr[2]),"white")
                    running = True
                    while running:
                        SCREEN.fill("black")
                        circulo1.BresenhamCircle()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                running = False
                            if running == False:
                                pygame.quit()
                                sys.exit()
                        pygame.display.update() 



        pygame.display.update()
        clock.tick(30)
    return 


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(35).render("ALGORITMOS DISCRETIZACION", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        LINEAS_BUTTON = Button(None, pos=(640, 250), 
                            text_input="LINEAS", font=get_font(25), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(None, pos=(640, 400), 
                            text_input="CIRCUNFERENCIAS", font=get_font(25), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(None, pos=(640, 550), 
                            text_input="SALIR", font=get_font(25), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [LINEAS_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LINEAS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    menu_linea()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()