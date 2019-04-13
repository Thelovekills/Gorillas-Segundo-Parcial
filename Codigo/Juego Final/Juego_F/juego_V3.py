"""Hello, and welcome to the source code of Gorillas.py. This program is meant to be very well documented so that a
novice programmer can follow along. This program was written by Al Sweigart as a companion for his free, Creative
Commons-licensed book "Invent Your Own Computer Games with Python", which is available in full at:

        http://inventwithpython.com

Feel free to email the author with any programming questions at al@inventwithpython.com

This program seeks to replicate gorillas.bas, a Qbasic program that was popular in the 1990s. By reading
through the comments, you can learn how a simple Python game with the Pygame engine is put together.

The comments will generally come _after_ the lines of code they describe.

If you like this, then check out inventwithpython.com to read the book (which has similar game projects) for free!

The Pygame documentation is pretty good, and can be found at http://www.pygame.org/docs

Unfortunately there is no sound with this game.
"""

import pygame
import sys
import time
import random
import math
from pygame.locals import *
"""Importaremos bastantes módulos para este juego." Pygame "tiene todos los gráficos y funciones relacionadas con el juego que
El motor del juego Pygame proporciona. "sys" tiene la función exit (). "tiempo" tiene la función dormir (). "aleatorio" tiene el randint ()
función, y "math" contiene la constante pi."""


"""Todas las variables a continuación en las LETRAS DE CAPS son constantes, es decir, se supone que solo se deben leer y no
modificado. (No hay nada que impida que el programa los modifique, pero es solo una convención que usan los programadores.
Las constantes son un poco más descriptivas que solo usar los números por sí mismos. Y si alguna vez quieres cambiar
Algún valor (como el tamaño de las explosiones o el color de los gorilas), solo tienes que cambiarlo en uno.
lugar."""

SCR_WIDTH = 640
SCR_HEIGHT = 350
FPS = 30
GAME_CLOCK = pygame.time.Clock()
"""Aquí hay varias constantes que usaremos en el juego. El juego Qbasic original tenía un tamaño de pantalla de 640x350, así que
Usa eso como nuestro tamaño de pantalla. Usaremos un único objeto de reloj global para manejar algunas de las cosas de tiempo en todos nuestros
funciones, y generalmente tienen FPS establecido en 30 (excepto cuando queremos configurarlo en otra cosa).

Las constantes son útiles porque puedes cambiar el valor en un solo lugar y se utilizará en todo el programa.

Intenta experimentar con diferentes valores para estas constantes globales."""

BUILDING_COLORS = ((173, 170, 173), (0, 170, 173), (173, 0, 0))
LIGHT_WINDOW = (255, 255, 82)
DARK_WINDOW = (82, 85, 82)
SKY_COLOR = (0, 0, 0)
GOR_COLOR = (86, 130, 3)
BAN_COLOR = (255, 255, 82)
EXPLOSION_COLOR = (255, 0, 0)
SUN_COLOR = (255, 255, 0)
DARK_RED_COLOR = (173, 0, 0)
BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)
GRAY_COLOR = (173, 170, 173)
"""Aquí hay un montón de colores. Pygame usa una tupla de tres enteros para especificar un color. Los enteros son para el
cantidad de rojo, azul y verde (en orden) en el color. Esto se conoce como un valor RGB.

BUILDING_COLORS tendrá una tupla de estas tuplas RGB y representará los diferentes colores que pueden ser los edificios."""

BUILD_EXPLOSION_SIZE = int(SCR_HEIGHT / 50)
GOR_EXPLOSION_SIZE = 30
"""BUILD_EXPLOSION_SIZE mantiene el tamaño de una explosión cuando un plátano golpea un edificio, y GOR_EXPLOSION_SIZE es el tamaño
cuando golpea a un gorila."""

SUN_X = 300
SUN_Y = 10
"""La posición del sol en el cielo."""

pygame.init()
GAME_FONT = pygame.font.SysFont(None, 20)
"""Se debe llamar a la función pygame.init () antes de llamar a cualquiera de las funciones de Pygame.
Usaremos la fuente del sistema predeterminada en un tamaño de 20 puntos."""

# orientación del plátano:
RIGHT = 0
UP = 1
LEFT = 2
DOWN = 3
"""Algunas constantes de la dirección a la que se enfrenta el plátano (o cualquier otra cosa)."""

# brazos de gorila dibujo tipos
BOTH_ARMS_DOWN = 0
LEFT_ARM_UP = 1
RIGHT_ARM_UP = 2
"""Algunas constantes para cuál de los tres sprites gorila usar: ambos brazos hacia abajo, brazo izquierdo hacia arriba o brazo derecho hacia arriba."""


"""Las siguientes cadenas multilínea se utilizan con la función makeSurfaceFromASCII (). Es básicamente una forma de
generar Superficies distintas de usar las funciones de dibujo o incluir archivos gráficos junto con este archivo .py.

Intenta experimentar cambiando las cuerdas. La primera y la última línea se ignoran (para que no tenga que tratar con
problemas de sangrado en la cadena)."""

STAR_ASCII = """


   XX  XX
    XXXX
  XXXXXXXX
    XXXX
   XX  XX
"""

GOR_DOWN_ASCII = """

              XXXXXXXXXXXX XX XX
              XXXXXXXXXXXX XX XX
              XXXXXXXXXXXX XX XX
              XXXXXXXXXXXX XX XX
        XXXXXXXXXXXXXXXXXXXXXXXXXXXX
      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX 
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        XXXX        XXXX        XXXX
       X    X      X    X      X    X
       X    X      X    X      X    X
        XXXX        XXXX        XXXX
"""

GOR_LEFT_ASCII = """
                                       XXX
              XXXXXXXXXXXX XX XX     XXX
              XXXXXXXXXXXX XX XX   XXX
              XXXXXXXXXXXX XX XX XXX
              XXXXXXXXXXXX XX XX 
        XXXXXXXXXXXXXXXXXXXXXXXXXXXX
      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX 
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        XXXX        XXXX        XXXX
       X    X      X    X      X    X
       X    X      X    X      X    X
        XXXX        XXXX        XXXX
"""

GOR_RIGHT_ASCII = """
  XXX
    XXX     XX XX XXXXXXXXXXX
      XXX   XX XX XXXXXXXXXXX
        XXX XX XX XXXXXXXXXXX
            XX XX XXXXXXXXXXX
        XXXXXXXXXXXXXXXXXXXXXXXXXXXX
      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX 
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        XXXX        XXXX        XXXX
       X    X      X    X      X    X
       X    X      X    X      X    X
        XXXX        XXXX        XXXX
"""

BAN_RIGHT_ASCII = """
    XXXXXXXXXXXXXXXXXXXXXX
   XXX                 X   X
   XXX                 X     X
   XXX                 X    X
   XXX                 X   X
    XXXXXXXXXXXXXXXXXXXXXX
"""

BAN_LEFT_ASCII = """
      XXXXXXXXXXXXXXXXXXXXXX
    X   X                 XXX
   X    X                 XXX                 
    X   X                 XXX
     X  X                 XXX
      XXXXXXXXXXXXXXXXXXXXXX
"""

BAN_UP_ASCII = """
    XXXXXXXXXXXXXXXXXXXXXX
   XXX                 X   X
   XXX                 X     X
   XXX                 X    X
   XXX                 X   X
    XXXXXXXXXXXXXXXXXXXXXX
"""

BAN_DOWN_ASCII = """
      XXXXXXXXXXXXXXXXXXXXXX
    X   X                 XXX
   X    X                 XXX                 
    X   X                 XXX
     X  X                 XXX
      XXXXXXXXXXXXXXXXXXXXXX
"""

SUN_NORMAL_ASCII = """
                    X
                    X
            X       X       X
             X      X      X
             X      X      X
     X        X     X     X        X
      X        X XXXXXXX X        X
       XX      XXXXXXXXXXX      XX
         X  XXXXXXXXXXXXXXXXX  X
          XXXXXXXXXXXXXXXXXXXXX
  X       XXXXXXXXXXXXXXXXXXXXX       X
   XXXX  XXXXXXXXXXXXXXXXXXXXXXX  XXXX
       XXXXXXXXXX XXXXX XXXXXXXXXX
        XXXXXXXX   XXX   XXXXXXXX
        XXXXXXXXX XXXXX XXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        XXXXXXXXXXXXXXXXXXXXXXXXX
        XXXXXXXXXXXXXXXXXXXXXXXXX
       XXXXXX XXXXXXXXXXXXX XXXXXX
   XXXX  XXXXX  XXXXXXXXX  XXXXX  XXXX
  X       XXXXXX  XXXXX  XXXXXX       X
          XXXXXXXX     XXXXXXXX
         X  XXXXXXXXXXXXXXXXX  X
       XX      XXXXXXXXXXX      XX
      X        X XXXXXXX X        X
     X        X     X     X        X
             X      X      X
             X      X      X
            X       X       X
                    X
                    X
"""

SUN_SHOCKED_ASCII = """
                    X
                    X
            X       X       X
             X      X      X
             X      X      X
     X        X     X     X        X
      X        X XXXXXXX X        X
       XX      XXXXXXXXXXX      XX
         X  XXXXXXXXXXXXXXXXX  X
          XXXXXXXXXXXXXXXXXXXXX
  X       XXXXXXXXXXXXXXXXXXXXX       X
   XXXX  XXXXXXXXXXXXXXXXXXXXXXX  XXXX
       XXXXXXXXXX XXXXX XXXXXXXXXX
        XXXXXXXX   XXX   XXXXXXXX
        XXXXXXXXX XXXXX XXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        XXXXXXXXXXXXXXXXXXXXXXXXX
        XXXXXXXXXXXXXXXXXXXXXXXXX
       XXXXXXXXXXXXXXXXXXXXXXXXXXX
   XXXX  XXXXXXXXX     XXXXXXXXX  XXXX
  X       XXXXXXX       XXXXXXX       X
          XXXXXXX       XXXXXXX
         X  XXXXXX     XXXXXX  X
       XX      XXXXXXXXXXX      XX
      X        X XXXXXXX X        X
     X        X     X     X        X
             X      X      X
             X      X      X
            X       X       X
                    X
                    X
"""

def terminate():
    """Llama a las funciones pygame.quit () y sys.exit () para finalizar el programa. (Encontré que no estoy llamando
    pygame.quit () antes de que sys.exit () pueda desordenar el IDLE a veces."""
    pygame.quit()
    sys.exit()

def makeSurfaceFromASCII(ascii, fgColor=(255,255,255), bgColor=(0,0,0)):
    """Devuelve un nuevo objeto pygame.Surface que tiene la imagen dibujada como se especifica en el parámetro ascii.
    La primera y última línea en ascii son ignoradas. De lo contrario, cualquier X en ascii marca un píxel con el color de primer plano
    y cualquier otra letra marca un píxel del color de fondo. El objeto Superficie tiene un ancho de la línea más ancha.
    en la cadena ascii, y siempre es rectangular."""

    """Intente experimentar con esta función para poder especificar más de dos colores. (Pase un dictado de
    Letras ASCII y tuplas RGB, por ejemplo."""
    ascii = ascii.split('\n')[1:-1]
    width = max([len(x) for x in ascii])
    height = len(ascii)
    surf = pygame.Surface((width, height))
    surf.fill(bgColor)

    pArr = pygame.PixelArray(surf)
    for y in range(height):
        for x in range(len(ascii[y])):
            if ascii[y][x] == 'X':
                pArr[x][y] = fgColor
    return surf

GOR_DOWN_SURF    = makeSurfaceFromASCII(GOR_DOWN_ASCII,    GOR_COLOR,      SKY_COLOR)
GOR_LEFT_SURF    = makeSurfaceFromASCII(GOR_LEFT_ASCII,    GOR_COLOR,      SKY_COLOR)
GOR_RIGHT_SURF   = makeSurfaceFromASCII(GOR_RIGHT_ASCII,   GOR_COLOR,      SKY_COLOR)
BAN_RIGHT_SURF   = makeSurfaceFromASCII(BAN_RIGHT_ASCII,   BAN_COLOR,      SKY_COLOR)
BAN_LEFT_SURF    = makeSurfaceFromASCII(BAN_LEFT_ASCII,    BAN_COLOR,      SKY_COLOR)
BAN_UP_SURF      = makeSurfaceFromASCII(BAN_UP_ASCII,      BAN_COLOR,      SKY_COLOR)
BAN_DOWN_SURF    = makeSurfaceFromASCII(BAN_DOWN_ASCII,    BAN_COLOR,      SKY_COLOR)
SUN_NORMAL_SURF  = makeSurfaceFromASCII(SUN_NORMAL_ASCII,  SUN_COLOR,      SKY_COLOR)
SUN_SHOCKED_SURF = makeSurfaceFromASCII(SUN_SHOCKED_ASCII, SUN_COLOR,      SKY_COLOR)
STAR_SURF        = makeSurfaceFromASCII(STAR_ASCII,        DARK_RED_COLOR, BLACK_COLOR)

assert GOR_DOWN_SURF.get_size() == GOR_LEFT_SURF.get_size() == GOR_RIGHT_SURF.get_size()
"""Cree los objetos pygame.Surface a partir de las cadenas ASCII."""

sunRect = pygame.Rect(SUN_X, SUN_Y, SUN_NORMAL_SURF.get_width(), SUN_NORMAL_SURF.get_height())
"""sunRect será un valor global, por lo que siempre sabremos dónde está el sol."""

def drawText(text, surfObj, x, y, fgcol, bgcol, pos='left'):
    """Una función genérica para dibujar una cadena en un objeto pygame.Surface en una determinada ubicación x, y. Esto devuelve
    un objeto pygame.Rect que describe el área en la que se dibujó la cadena.

    Si el parámetro pos es "left", entonces el parámetro x, y especifica la esquina superior izquierda del rectángulo de texto.
    Si el parámetro pos es "center", entonces el parámetro x, y especifica el punto superior medio del rectángulo de texto."""

    textobj = GAME_FONT.render(text, 1, fgcol, bgcol) # crea el texto en la memoria (aún no está en una superficie).
    textrect = textobj.get_rect()

    if pos == 'left':
        textrect.topleft = (x, y)
    elif pos == 'center':
        textrect.midtop = (x, y)
    surfObj.blit(textobj, textrect) #dibuja el texto en la superficie.
    """Recuerde que el texto solo aparecerá en la pantalla si pasa el objeto pygame.Surface que fue
    devuelto de la llamada a pygame.display.set_mode (), y solo después de que se llame a pygame.display.update ()."""
    return textrect

def getModCase(s, mod):
    """Comprueba el estado de las teclas de bloqueo de mayúsculas y mayúsculas, y cambia la caja de la cadena s si es necesario."""
    if bool(mod & KMOD_RSHIFT or mod & KMOD_LSHIFT) ^ bool(mod & KMOD_CAPS):
        return s.swapcase()
    else:
        return s

def inputMode(prompt, screenSurf, x, y, fgcol, bgcol, maxlen=12, allowed=None, pos='left', cursor='_', cursorBlink=False):
    """Toma el control del programa cuando se le llama. Esta función muestra un aviso en la pantalla (la cadena" prompt ")
    parámetro) en la superficie de la pantalla de surf en las coordenadas x, y. El texto está en el color fgcol con un color bgcol
    fondo. Opcionalmente, puede especificar maxlen para una longitud máxima de la respuesta del usuario. "permitido" es una cadena
    de caracteres permitidos (si el jugador solo puede escribir números, digamos) e ignora todas las demás pulsaciones de teclas. La "pos"
    el parámetro puede ser la cadena "izquierda" (donde las coordenadas x, y se refieren a la esquina superior izquierda del texto
    cuadro) o "centro" (donde las coordenadas x, y se refieren al centro superior del cuadro de texto).

    "cursor" es un carácter opcional que se usa para que un cursor muestre dónde irá la siguiente letra. Si "cursorBlink"
    es Verdadero, entonces este carácter del cursor se encenderá y apagará.

    El valor devuelto es una cadena de lo que el jugador escribió, o Ninguno si el jugador presionó la tecla Esc.

    Tenga en cuenta que el jugador solo puede presionar Retroceso para eliminar caracteres, no pueden usar las teclas de flecha para mover el
    cursor."""
    inputText = ''
    """inputText almacenará el texto de lo que el jugador ha escrito hasta ahora."""
    done = False
    cursorTimestamp = time.time()
    cursorShow = cursor
    while not done:
        """Seguiremos en bucle hasta que el jugador haya pulsado la tecla Esc o Intro."""

        if cursor and cursorBlink and time.time() - 1.0 > cursorTimestamp:
            if cursorShow == cursor:
                cursorShow = '   '
            else:
                cursorShow = cursor
            cursorTimestamp = time.time()

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    return None
                elif event.key == K_RETURN:
                    done = True
                    if cursorShow:
                        cursorShow = '   '
                elif event.key == K_BACKSPACE:
                    if len(inputText):
                        drawText(prompt + inputText + cursorShow, screenSurf, textrect.left, textrect.top, bgcol, bgcol, 'left')
                        inputText = inputText[:-1]
                else:
                    if len(inputText) >= maxlen or (allowed is not None and chr(event.key) not in allowed):
                        continue
                    if event.key >= 32 and event.key < 128:
                        inputText += getModCase(chr(event.key), event.mod)

        textrect = drawText(prompt + cursorShow, screenSurf, x, y, fgcol, bgcol, pos)
        drawText(prompt + inputText + cursorShow, screenSurf, textrect.left, textrect.top, fgcol, bgcol, 'left')
        pygame.display.update()
        GAME_CLOCK.tick(FPS)
    return inputText

def nextBananaShape(orient):
    """Devuelve la siguiente forma de plátano en la secuencia de 0, 1, 2, 3 y luego 0 nuevamente. (Estos corresponden a la DERECHA, ARRIBA,
    Variables IZQUIERDA y ABAJO. """
    if orient + 1 == 4:
        return 0
    else:
        return orient + 1

def drawBanana(screenSurf, orient, x, y):
    """Dibuja la forma de plátano a la superficie de la pantalla de surf, con su esquina superior izquierda en la coordenada xy proporcionada.
    "orientar" es uno de los valores DERECHA, ARRIBA, IZQUIERDA o ABAJO (que son los enteros de 0 a 3 respectivamente)."""
    if orient == DOWN:
        screenSurf.blit(BAN_DOWN_SURF, (x, y))
    elif orient == UP:
        screenSurf.blit(BAN_UP_SURF, (x, y))
    elif orient == LEFT:
        screenSurf.blit(BAN_LEFT_SURF, (x, y))
    elif orient == RIGHT:
        screenSurf.blit(BAN_RIGHT_SURF, (x, y))


def drawSun(screenSurf, shocked=False):
    """Dibuja el sprite del sol sobre la superficie de la pantalla de surf. Si el shock es Verdadero, entonces use la cara de aspecto sorprendido,
    De lo contrario, utilice la cara sonriente normal. Esta función no llama a python.display.update ()"""
    if shocked:
        screenSurf.blit(SUN_SHOCKED_SURF, (SUN_X, SUN_Y))
    else:
        screenSurf.blit(SUN_NORMAL_SURF, (SUN_X, SUN_Y))


def drawGorilla(screenSurf, x, y, arms=BOTH_ARMS_DOWN):
    """Dibuja el sprite gorila en la superficie del surf de pantalla en una coordenada x, y específica. La coordenada x, y
    es para la esquina superior izquierda del sprite gorila. Tenga en cuenta que las tres superficies de gorila son del mismo tamaño."""

    if arms == BOTH_ARMS_DOWN:
        gorSurf = GOR_DOWN_SURF
    elif arms == LEFT_ARM_UP:
        gorSurf = GOR_LEFT_SURF
    elif arms == RIGHT_ARM_UP:
        gorSurf = GOR_RIGHT_SURF
    """ Arriba, elegimos qué objeto de superficie usaremos para dibujar el gorila, dependiendo del parámetro" brazos ".
    La llamada a screenSurf.blit () dibujará la superficie en la pantalla (pero no aparecerá en la pantalla hasta que aparezca).
    Se llama a pygame.display.update ()."""

    screenSurf.blit(gorSurf, (x, y))

def makeCityScape():
    """Esta función crea y devuelve un nuevo paisaje urbano de varios edificios en un pygame. Objeto de superficie y devuelve
    este objeto de superficie."""

    screenSurf = pygame.Surface((SCR_WIDTH, SCR_HEIGHT)) # first make the new surface the same size of the screen.
    screenSurf.fill(SKY_COLOR) # fill in the surface with the background sky color

    """Elegiremos una curva hacia arriba, hacia abajo, en v" v ", o curva" ^ "montañosa para la pendiente de los edificios.
    La mitad del tiempo elegiremos la forma de la pendiente del valle, mientras que las tres restantes tendrán 1/6 de probabilidad de
    siendo elegido. La pendiente también determina la altura del primer edificio, que se almacena en newHeight."""
    slope = random.randint(1, 6)
    if slope == 1:
        slope = 'upward'
        newHeight = 15
    elif slope == 2:
        slope = 'downward'
        newHeight = 130
    elif slope >= 3 and slope <= 5:
        slope = 'v'
        newHeight = 15
    else:
        slope = '^'
        newHeight = 130

    bottomLine = 335 # la línea inferior de los edificios. Queremos algo de espacio para que vaya la flecha del viento.
    heightInc = 10 # una línea de base de cuánto crecen o se reducen los edificios en comparación con el último edificio
    defBuildWidth = 37 # ancho de construcción predeterminado, también juzga qué tan amplios pueden ser los edificios
    randomHeightDiff = 120 # sobre cuánto crecen o se reducen los edificios
    windowWidth = 4 # el ancho de cada ventana en píxeles
    windowHeight = 7 # la altura de cada ventana en píxeles
    windowSpacingX = 10 # cuántos píxeles separados del borde izquierdo de cada ventana es
    windowSpacingY = 15 # cuántos píxeles separados del borde superior de cada ventana es
    gHeight = 25 # (No estoy seguro de qué supone esto en el código Qbasic original, pero lo copié de todos modos)
    # (También había una variable maxHeight en el Qbasic original, pero no creo que hiciera nada, así que lo omití).

    buildingCoords = [] # una lista de coords (izquierda, arriba) de cada edificio, de izquierda a derecha

    x = 2 # x se refiere a la esquina superior izquierda del edificio actual que se está dibujando


    while x < SCR_WIDTH - heightInc:
        # En este bucle seguimos dibujando nuevos edificios hasta que nos quedemos sin espacio en la pantalla.

        # Primero, el tipo de pendiente determina si el edificio debe crecer o reducirse.
        if slope == 'upward':
            newHeight += heightInc
        elif slope == 'downward':
            newHeight -= heightInc
        elif slope == 'v':
            if x > SCR_WIDTH / 2:
                newHeight -= (2 * heightInc)
                # Para las pendientes del valle, los edificios se encogen en la mitad izquierda de la pantalla ...
            else:
                newHeight += (2 * heightInc)
                # ...y crecer en la mitad derecha.
        else:
            if x > SCR_WIDTH / 2:
                newHeight += (2 * heightInc)
                # Para las pendientes montañosas, los edificios crecen en la mitad izquierda de la pantalla ...
            else:
                newHeight -= (2 * heightInc)
                # ... y encogerse en la mitad derecha.

        # Obtener el ancho del nuevo edificio.
        buildWidth = defBuildWidth + random.randint(0, defBuildWidth)
        if buildWidth + x > SCR_WIDTH:
            buildWidth = SCR_WIDTH - x -2

        #  Obtener la altura del nuevo edificio.
        buildHeight = random.randint(heightInc, randomHeightDiff) + newHeight

        # Check if the height is too high.
        if bottomLine - buildHeight <= gHeight:
            buildHeight = gHeight

        #Comprobar si la altura es demasiado alta.
        buildingColor = BUILDING_COLORS[random.randint(0, len(BUILDING_COLORS)-1)]

        #  Dibujar el edificio
        pygame.draw.rect(screenSurf, buildingColor, (x+1, bottomLine - (buildHeight+1), buildWidth-1, buildHeight-1))

        buildingCoords.append( (x, bottomLine - buildHeight) )

        # Dibuja las ventanas
        for winx in range(3, buildWidth - windowSpacingX + windowWidth, windowSpacingX):
            for winy in range(3, buildHeight - windowSpacingY, windowSpacingY):
                if random.randint(1, 4) == 1:
                    winColor = DARK_WINDOW
                else:
                    winColor = LIGHT_WINDOW
                pygame.draw.rect(screenSurf, winColor, (x + 1 + winx, (bottomLine - buildHeight) + 1 + winy, windowWidth, windowHeight))

        x += buildWidth

    # Queremos devolver tanto el objeto de superficie en el que hemos dibujado los edificios como las coordenadas de cada edificio.
    return screenSurf, buildingCoords

def placeGorillas(buildCoords):
    """Usando el valor de buildingCoords devuelto por makeCityScape (), queremos colocar los gorilas a la izquierda y a la derecha
    lado de la pantalla en el segundo o tercer edificio desde el borde."""

    gorPos = [] # el artículo 0 es para (izquierda, arriba) del jugador uno, el artículo 1 es para el jugador dos.
    xAdj = int(GOR_DOWN_SURF.get_rect().width / 2)
    yAdj = GOR_DOWN_SURF.get_rect().height

    for i in range(0,2):  # coloca primero y luego segundo jugador

        # Coloca los gorilas en el segundo o tercer edificio desde el borde.
        if i == 0:
            buildNum = random.randint(1,2)
        else:
            buildNum = random.randint(len(buildCoords)-3, len(buildCoords)-2)

        buildWidth = buildCoords[buildNum + 1][0] - buildCoords[buildNum][0]
        gorPos.append( (buildCoords[buildNum][0] + int(buildWidth / 2) - xAdj, buildCoords[buildNum][1] - yAdj - 1) )

    #  El formato de la lista gorPos es [(p1 x, p1 y), (p2 x, p2 y)]
    return gorPos

def waitForPlayerToPressKey():
    """Al llamar a esta función, el programa hará una pausa hasta que el usuario presione una tecla. La tecla será devuelta."""
    while True:
        key = checkForKeyPress()
        if key:
            return key

def checkForKeyPress():
    """Al llamar a esta función, se verificará si se presionó una tecla recientemente. Si es así, se devuelve la tecla.
    Si no, entonces se devuelve Falso. Si se presionó la tecla Esc, entonces el programa termina."""
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        if event.type == KEYUP:
            if event.key == K_ESCAPE: # presionando escape se cierra
                terminate()
            return event.key
    return False

def showStartScreen(screenSurf):
    """Dibuja la pantalla de introducción inicial a screenSurf, con estrellas rojas girando alrededor del borde. Esta pantalla
    Permanece hasta que el usuario presiona una tecla."""
    vertAdj = 0
    horAdj = 0
    while not checkForKeyPress():
        screenSurf.fill(BLACK_COLOR)

        drawStars(screenSurf, vertAdj, horAdj)
        vertAdj += 1
        if vertAdj == 4: vertAdj = 0
        horAdj += 12
        if horAdj == 84: horAdj = 0
        """Las estrellas a los lados de la pantalla mueven 1 píxel cada iteración a través de este bucle y se restablecen cada 4
        píxeles Las estrellas en la parte superior e inferior de la pantalla mueven 12 píxeles cada iteración y se restablecen cada 84 píxeles."""

        drawText('P  y  t  h  o  n     G  O  R  I  L  L  A  S', screenSurf, SCR_WIDTH / 2, 50, WHITE_COLOR, BLACK_COLOR, pos='center')
        drawText('Tu objetivo es golper al oponente mediante explosiones', screenSurf, SCR_WIDTH / 2, 110, GRAY_COLOR, BLACK_COLOR, pos='center')
        drawText('provocadas por el las balas lanzadas', screenSurf, SCR_WIDTH / 2, 130, GRAY_COLOR, BLACK_COLOR, pos='center')
        drawText('esto depende del angulo y la velocidad que tu le asignes', screenSurf, SCR_WIDTH / 2, 150, GRAY_COLOR, BLACK_COLOR, pos='center')
        drawText('Ademas de que el viento es un factor importante', screenSurf, SCR_WIDTH / 2, 170, GRAY_COLOR, BLACK_COLOR, pos='center')
        drawText('sobrevive el más fuerte, asi que adelante!.', screenSurf, SCR_WIDTH / 2, 190, GRAY_COLOR, BLACK_COLOR, pos='center')
        drawText('Press any key to continue', screenSurf, SCR_WIDTH / 2, 300, GRAY_COLOR, BLACK_COLOR, pos='center')

        pygame.display.update()
        GAME_CLOCK.tick(FPS)

def showGameOverScreen(screenSurf, p1name, p1score, p2name, p2score):
    """Dibuja el juego sobre la pantalla para ver la pantalla, y muestra los nombres y las puntuaciones de los jugadores. Esta pantalla ha girado
    las estrellas rojas también, y se cuelga hasta que el usuario presiona una tecla."""
    p1score = str(p1score)
    p2score = str(p2score)
    vertAdj = 0
    horAdj = 0
    while not checkForKeyPress():
        screenSurf.fill(BLACK_COLOR)

        drawStars(screenSurf, vertAdj, horAdj)
        vertAdj += 1
        if vertAdj == 4: vertAdj = 0
        horAdj += 12
        if horAdj == 84: horAdj = 0
        """Las estrellas a los lados de la pantalla mueven 1 píxel cada iteración a través de este bucle y se restablecen cada 4
        píxeles Las estrellas en la parte superior e inferior de la pantalla mueven 12 píxeles cada iteración y se restablecen cada 84 píxeles."""

        drawText('GAME OVER!', screenSurf, SCR_WIDTH / 2, 120, GRAY_COLOR, BLACK_COLOR, pos='center')
        drawText('Score:', screenSurf, SCR_WIDTH / 2, 155, GRAY_COLOR, BLACK_COLOR, pos='center')
        drawText(p1name, screenSurf, 225, 170, GRAY_COLOR, BLACK_COLOR)
        drawText(p1score, screenSurf, 395, 170, GRAY_COLOR, BLACK_COLOR)
        drawText(p2name, screenSurf, 225, 185, GRAY_COLOR, BLACK_COLOR)
        drawText(p2score, screenSurf, 395, 185, GRAY_COLOR, BLACK_COLOR)
        drawText('Press any key to continue', screenSurf, SCR_WIDTH / 2, 298, GRAY_COLOR, BLACK_COLOR, pos='center')

        pygame.display.update()
        GAME_CLOCK.tick(FPS)

def drawStars(screenSurf, vertAdj, horAdj):
    """Esta función dibuja las estrellas rojas en el borde de screenSurf."""
    for i in range(16):
        # dibujar la fila superior de estrellas
        screenSurf.blit(STAR_SURF, (2 + (((3 - vertAdj) + i * 4) * STAR_SURF.get_width()), 3))
        # dibujar la fila inferior de estrellas
        screenSurf.blit(STAR_SURF, (2 + ((vertAdj + i * 4) * STAR_SURF.get_width()), SCR_HEIGHT - 7 - STAR_SURF.get_height()))

    for i in range(4):
        # dibujar columna izquierda de estrellas bajando
        screenSurf.blit(STAR_SURF, (5, 6 + STAR_SURF.get_height() + (horAdj + i * 84)))
        # dibujar columna derecha de estrellas subiendo
        screenSurf.blit(STAR_SURF, (SCR_WIDTH - 5 - STAR_SURF.get_width(), (SCR_HEIGHT - (6 + STAR_SURF.get_height() + (horAdj + i * 84)))))



def showSettingsScreen(screenSurf):
    """Esta es la pantalla que le permite al usuario escribir su nombre y configuración para el juego."""
    p1name = None
    p2name = None
    points = None
    gravity = None
     
# AQUI PODEMOS ALTERAR EL MENU

    screenSurf.fill(BLACK_COLOR)
    key = waitForPlayerToPressKey()
    while p1name is None:
         p1name = inputMode("Nombre del jugador 1 (Default = 'Player 1'):  ", screenSurf, SCR_WIDTH / 2 - 146, 50, GRAY_COLOR, BLACK_COLOR, maxlen=10, pos='left', cursorBlink=True)
    if p1name == '':
        p1name = 'Player 1'

    while p2name is None:
        p2name = inputMode("Nombre del jugador 2 (Default = 'Player 2'):  ", screenSurf, SCR_WIDTH / 2 - 146, 80, GRAY_COLOR, BLACK_COLOR, maxlen=10, pos='left', cursorBlink=True)
    if p2name == '':
        p2name = 'Player 2'

    while points is None:
        points = inputMode("Puntos totales a jugar (Default = 3)?  ", screenSurf, SCR_WIDTH / 2 - 155, 110, GRAY_COLOR, BLACK_COLOR, maxlen=6, allowed='0123456789', pos='left', cursorBlink=True)
    if points == '':
        points = 3
    else:
        points = int(points)

    while gravity is None:
        gravity = inputMode("Gravedad con la que quieres jugar? (Tierra = 9.8)?  ", screenSurf, SCR_WIDTH / 2 - 150, 140, GRAY_COLOR, BLACK_COLOR, maxlen=6, allowed='0123456789.', pos='left', cursorBlink=True)
    if gravity == '':
        gravity = 9.8
    else:
        gravity = float(gravity)

    drawText('--------------', screenSurf, SCR_WIDTH / 2 -10, 170, GRAY_COLOR, BLACK_COLOR, pos='center')
    drawText('V = Ver a la Intro', screenSurf, SCR_WIDTH / 2 -10, 200, GRAY_COLOR, BLACK_COLOR, pos='center')
    drawText('P = Play Game', screenSurf, SCR_WIDTH / 2 -10, 230, GRAY_COLOR, BLACK_COLOR, pos='center')
    drawText('Cual escojes?', screenSurf, SCR_WIDTH / 2 -10, 260, GRAY_COLOR, BLACK_COLOR, pos='center')
    pygame.display.update()

    key = waitForPlayerToPressKey()
    while chr(key) != 'v' and chr(key) != 'p':
        key = waitForPlayerToPressKey()

    return p1name, p2name, points, gravity, chr(key) # returns 'v' or 'p'

def showIntroScreen(screenSurf, p1name, p2name):
    """Esta es la pantalla que se reproduce si el usuario seleccionó" ver introducción "desde la pantalla de inicio."""
    screenSurf.fill(SKY_COLOR)
    drawText('P  y  t  h  o  n     G  O  R  I  L  L  A  S', screenSurf, SCR_WIDTH / 2, 15, WHITE_COLOR, SKY_COLOR, pos='center')
    drawText('STARRING:', screenSurf, SCR_WIDTH / 2, 55, WHITE_COLOR, SKY_COLOR, pos='center')
    drawText('%s AND %s' % (p1name, p2name), screenSurf, SCR_WIDTH / 2, 115, WHITE_COLOR, SKY_COLOR, pos='center')

    x = 278
    y = 175

    for i in range(2):
        drawGorilla(screenSurf, x-13, y, RIGHT_ARM_UP)
        drawGorilla(screenSurf, x+47, y, LEFT_ARM_UP)
        pygame.display.update()

        time.sleep(2)

        drawGorilla(screenSurf, x-13, y, LEFT_ARM_UP)
        drawGorilla(screenSurf, x+47, y, RIGHT_ARM_UP)
        pygame.display.update()

        time.sleep(2)

    for i in range(4):
        drawGorilla(screenSurf, x-13, y, LEFT_ARM_UP)
        drawGorilla(screenSurf, x+47, y, RIGHT_ARM_UP)
        pygame.display.update()

        time.sleep(0.3)

        drawGorilla(screenSurf, x-13, y, RIGHT_ARM_UP)
        drawGorilla(screenSurf, x+47, y, LEFT_ARM_UP)
        pygame.display.update()

        time.sleep(0.3)


def getShot(screenSurf, p1name, p2name, playerNum):
    """Se llama a getShot () cuando queremos obtener el ángulo y la velocidad del jugador."""
    pygame.draw.rect(screenSurf, SKY_COLOR, (0, 0, 200, 50))
    pygame.draw.rect(screenSurf, SKY_COLOR, (550, 0, 00, 50))

    drawText(p1name, screenSurf, 2, 2, WHITE_COLOR, SKY_COLOR)
    drawText(p2name, screenSurf, 538, 2, WHITE_COLOR, SKY_COLOR)

    if playerNum == 1:
        x = 2
    else:
        x = 538

    angle = ''
    while angle == '':
        angle = inputMode('Angle:  ', screenSurf, x, 18, WHITE_COLOR, SKY_COLOR, maxlen=3, allowed='0123456789')
    if angle is None: terminate()
    angle = int(angle)

    velocity = ''
    while velocity == '':
        velocity = inputMode('Velocity:  ', screenSurf, x, 34, WHITE_COLOR, SKY_COLOR, maxlen=3, allowed='0123456789')
    if velocity is None: terminate()
    velocity = int(velocity)

    # Borrar la entrada del usuario
    drawText('Angle:   ' + str(angle), screenSurf, x, 2, SKY_COLOR, SKY_COLOR)
    drawText('Velocity:   ' + str(angle), screenSurf, x, 2, SKY_COLOR, SKY_COLOR)
    pygame.display.update()

    if playerNum == 2:
        angle = 180 - angle

    return (angle, velocity)

def displayScore(screenSurf, oneScore, twoScore):
    """Dibuja el puntaje en la superficie de la pantalla de surf."""
    drawText(str(oneScore) + '>Score<' + str(twoScore), screenSurf, 270, 310, WHITE_COLOR, SKY_COLOR, pos='left')

def plotShot(screenSurf, skylineSurf, angle, velocity, playerNum, wind, gravity, gor1, gor2):
    # startx y starty es la esquina superior izquierda del gorila.
    angle = angle / 180.0 * math.pi
    initXVel = math.cos(angle) * velocity
    initYVel = math.sin(angle) * velocity
    gorWidth, gorHeight = GOR_DOWN_SURF.get_size()
    gor1rect = pygame.Rect(gor1[0], gor1[1], gorWidth, gorHeight)
    gor2rect = pygame.Rect(gor2[0], gor2[1], gorWidth, gorHeight)


    if playerNum == 1:
        gorImg = LEFT_ARM_UP
    else:
        gorImg = RIGHT_ARM_UP
    """El jugador 1 gorila de la izquierda usa su brazo izquierdo para lanzar, el jugador 2 gorila de la derecha usa su
    brazo derecho para lanzar. """

    if playerNum == 1:
        startx = gor1[0]
        starty = gor1[1]
    elif playerNum == 2:
        startx = gor2[0]
        starty = gor2[1]

    drawGorilla(screenSurf, startx, starty, gorImg)
    pygame.display.update()
    time.sleep(0.3)
    drawGorilla(screenSurf, startx, starty, BOTH_ARMS_DOWN)
    pygame.display.update()
    """Dibuja al gorila lanzando el plátano"""

    bananaShape = UP

    if playerNum == 2:
        startx += GOR_DOWN_SURF.get_size()[0]

    starty -= getBananaRect(0, 0, bananaShape).height + BAN_UP_SURF.get_size()[1]

    impact = False
    bananaInPlay = True

    t = 1.0
    sunHit = False

    while not impact and bananaInPlay:
        x = startx + (initXVel * t) + (0.5 * (wind / 5) * t**2)
        y = starty + ((-1 * (initYVel * t)) + (0.5 * gravity * t**2))
        """Esta es básicamente la ecuación que describe el arco del plátano."""

        if x >= SCR_WIDTH - 10 or x <= 3 or y >= SCR_HEIGHT:
            bananaInPlay = False

        bananaRect = getBananaRect(x, y, bananaShape)
        if bananaShape == UP:
            bananaSurf = BAN_UP_SURF
            bananaRect.left -= 2
            bananaRect.top += 2
        elif bananaShape == DOWN:
            bananaSurf = BAN_DOWN_SURF
            bananaRect.left -= 2
            bananaRect.top += 2
        elif bananaShape == LEFT:
            bananaSurf = BAN_LEFT_SURF
        elif bananaShape == RIGHT:
            bananaSurf = BAN_RIGHT_SURF

        bananaShape = nextBananaShape(bananaShape)

        srcPixArray = pygame.PixelArray(skylineSurf)
        if bananaInPlay and y > 0:

            if sunRect.collidepoint(x, y):
                # El plátano ha golpeado el sol, así que dibuja la cara "sorprendida".
                sunHit = True

            # dibujar la cara del sol apropiada
            drawSun(screenSurf, shocked=sunHit)

            if bananaRect.colliderect(gor1rect):
                # banana ha golpeado al jugador 1

                """Tenga en cuenta que dibujamos la explosión en la pantalla (en screenSurf) y en la superficie del horizonte por separado (en skylineSurf).
                Esto se hace para que los plátanos no toquen el sol o cualquier texto y accidentalmente piensen que han golpeado algo. Nosotros tambien queremos
                El objeto de superficie de SkySurf para realizar un seguimiento de los trozos de los edificios que quedan."""
                doExplosion(screenSurf, skylineSurf, bananaRect.centerx, bananaRect.centery, explosionSize=int(GOR_EXPLOSION_SIZE*2/3), speed=0.005)
                doExplosion(screenSurf, skylineSurf, bananaRect.centerx, bananaRect.centery, explosionSize=GOR_EXPLOSION_SIZE, speed=0.005)
                drawSun(screenSurf)
                return 'gorilla1'
            elif bananaRect.colliderect(gor2rect):
                # banana ha golpeado al jugador 2
                doExplosion(screenSurf, skylineSurf, bananaRect.centerx, bananaRect.centery, explosionSize=int(GOR_EXPLOSION_SIZE*2/3), speed=0.005)
                doExplosion(screenSurf, skylineSurf, bananaRect.centerx, bananaRect.centery, explosionSize=GOR_EXPLOSION_SIZE, speed=0.005)
                screenSurf.fill(SKY_COLOR, bananaRect) # erase banana
                drawSun(screenSurf)
                return 'gorilla2'
            elif collideWithNonColor(srcPixArray, screenSurf, bananaRect, SKY_COLOR):
                # banana ha golpeado un edificio
                doExplosion(screenSurf, skylineSurf, bananaRect.centerx, bananaRect.centery)
                screenSurf.fill(SKY_COLOR, bananaRect) # erase banana
                drawSun(screenSurf)
                return 'building'

        del srcPixArray
        """Pygame no nos permite cubrir una superficie mientras exista una matriz de píxeles, por lo que la eliminamos."""

        screenSurf.blit(bananaSurf, (bananaRect.topleft))
        pygame.display.update()
        time.sleep(0.02)

        screenSurf.fill(SKY_COLOR, bananaRect) # borrar banana

        t += 0.1 # avanzar en la trama
    drawSun(screenSurf)
    return 'miss'

def victoryDance(screenSurf, x, y):
    """Dadas las coordenadas x, y de la esquina superior del sprite de gorila, esto pasa por
    La rutina de baile de la victoria del gorila, donde comienzan a agitar los brazos en el aire """
    for i in range(4):
        screenSurf.blit(GOR_LEFT_SURF, (x, y))
        pygame.display.update()
        time.sleep(0.3)
        screenSurf.blit(GOR_RIGHT_SURF, (x, y))
        pygame.display.update()
        time.sleep(0.3)


def collideWithNonColor(pixArr, surfObj, rect, color):
    """Esto verifica el área (descrita por" rect ") en pixArr (una matriz de píxeles derivada del objeto de superficie surfObj)
    si tiene algún píxel que no sea el color especificado por el parámetro "color". Esta función se utiliza para detectar
    si el plátano ha golpeado alguna parte no coloreada del cielo (lo que significa un gorila o un edificio)."""
    rightSide = min(rect.right, SCR_WIDTH)
    bottomSide = min(rect.bottom, SCR_HEIGHT)

    for x in range(rect.left, rightSide):
        for y in range(rect.top, bottomSide):
            if surfObj.unmap_rgb(pixArr[x][y]) != color:
                return True
    return False


def getBananaRect(x, y, shape):
    if shape == UP:
        return pygame.Rect((x, y), BAN_UP_SURF.get_size())
    if shape == DOWN:
        return pygame.Rect((x, y), BAN_DOWN_SURF.get_size())
    if shape == LEFT:
        return pygame.Rect((x, y), BAN_LEFT_SURF.get_size())
    if shape == RIGHT:
        return pygame.Rect((x, y), BAN_RIGHT_SURF.get_size())

def getWind():
    """Determine aleatoriamente cuál debe ser la velocidad y la dirección del viento para este juego."""
    wind = random.randint(5, 15)
    if random.randint(0, 1):
        wind *= -1
    return wind

def drawWind(screenSurf, wind):
    """Dibuja la flecha del viento en el objeto screenSurf en la parte inferior de la pantalla. El parámetro" viento "proviene de
    una llamada a getWind ()."""
    if wind != 0:
        wind *= 3
        pygame.draw.line(screenSurf, EXPLOSION_COLOR, (int(SCR_WIDTH / 2), SCR_HEIGHT - 5), (int(SCR_WIDTH / 2) + wind, SCR_HEIGHT - 5))
        # dibujar el extremo de la flecha
        if wind > 0: arrowDir = -2
        else:        arrowDir = 2
        pygame.draw.line(screenSurf, EXPLOSION_COLOR, (int(SCR_WIDTH / 2) + wind, SCR_HEIGHT - 5), (int(SCR_WIDTH / 2) + wind + arrowDir, SCR_HEIGHT - 5 - 2))
        pygame.draw.line(screenSurf, EXPLOSION_COLOR, (int(SCR_WIDTH / 2) + wind, SCR_HEIGHT - 5), (int(SCR_WIDTH / 2) + wind + arrowDir, SCR_HEIGHT - 5 + 2))

def doExplosion(screenSurf, skylineSurf, x, y, explosionSize=BUILD_EXPLOSION_SIZE, speed=0.05):
    for r in range(1, explosionSize):
        pygame.draw.circle(screenSurf, EXPLOSION_COLOR, (x, y), r)
        pygame.draw.circle(skylineSurf, EXPLOSION_COLOR, (x, y), r)
        pygame.display.update()
        time.sleep(speed)
    for r in range(explosionSize, 1, -1):
        pygame.draw.circle(screenSurf, SKY_COLOR, (x, y), explosionSize)
        pygame.draw.circle(skylineSurf, SKY_COLOR, (x, y), explosionSize)
        pygame.draw.circle(screenSurf, EXPLOSION_COLOR, (x, y), r)
        pygame.draw.circle(skylineSurf, EXPLOSION_COLOR, (x, y), r)
        pygame.display.update()
        time.sleep(speed)
    pygame.draw.circle(screenSurf, SKY_COLOR, (x, y), 2)
    pygame.draw.circle(skylineSurf, SKY_COLOR, (x, y), 2)
    pygame.display.update()

def obtener_puntuacion_mas_alta():
    # Puntuación más alta por defecto
    puntuacion_mas_alta = 0
 
    # Intentemos leer la puntuación más alta desde un archivo
    try:
        archivo_puntuacion_mas_alta = open("high_score.txt", "r")
        puntuacion_mas_alta = int(archivo_puntuacion_mas_alta.read())
        archivo_puntuacion_mas_alta.close()
        print("La puntuación más alta es", puntuacion_mas_alta)
    except IOError:
        # Error al leer el archivo, no existe una puntuación más alta
        print("Aún no existe una puntuación más alta.")
    except ValueError:
        # Hay un archivo allí, pero no entiendo los números.
        print("Estoy confundido. Empezamos sin una puntuación alta.")
 
    return puntuacion_mas_alta

def guardar_puntuacion_mas_alta(nueva_puntuacion_mas_alta):
    try:
        # Escribimos el archivo en disco
        archivo_puntuacion_mas_alta = open("high_score.txt", "w")
        archivo_puntuacion_mas_alta.write(str(nueva_puntuacion_mas_alta))
        archivo_puntuacion_mas_alta.close()
    except IOError:
        # Um, no puedo escribirlo.
        print("No soy capaz de guardar la puntuación alta.")

def records(puntuacion_actual):
    puntuacion_mas_alta = obtener_puntuacion_mas_alta()
    print(puntuacion_mas_alta)
    if puntuacion_actual > puntuacion_mas_alta:
        # Conseguido! Guardamos en disco
        print("Bravo! Nueva puntuación más alta!")
        guardar_puntuacion_mas_alta(puntuacion_actual)
    else:
        print("Mejor suerte la próxima vez.")


class Opcion:

    def __init__(self, fuente, titulo, x, y, paridad, funcion_asignada):
        self.imagen_normal = fuente.render(titulo, 1, (255, 255,255))
        self.imagen_destacada = fuente.render(titulo, 1, (200, 0, 0))
        self.image = self.imagen_normal
        self.rect = self.image.get_rect()
        self.rect.x = 500 * paridad
        self.rect.y = y
        self.funcion_asignada = funcion_asignada
        self.x = float(self.rect.x)

    def actualizar(self):
        destino_x = 105
        self.x += (destino_x - self.x) / 5.0
        self.rect.x = int(self.x)

    def imprimir(self, screen):
        screen.blit(self.image, self.rect)

    def destacar(self, estado):
        if estado:
            self.image = self.imagen_destacada
        else:
            self.image = self.imagen_normal

    def activar(self):
        self.funcion_asignada()


class Cursor:

    def __init__(self, x, y, dy):
        self.image = pygame.image.load('cursor.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.y_inicial = y
        self.dy = dy
        self.y = 0
        self.seleccionar(0)

    def actualizar(self):
        self.y += (self.to_y - self.y) / 10.0
        self.rect.y = int(self.y)

    def seleccionar(self, indice):
        self.to_y = self.y_inicial + indice * self.dy

    def imprimir(self, screen):
        screen.blit(self.image, self.rect)


class Menu:
    "Representa un menú con opciones para un juego"
    
    def __init__(self, opciones):
        self.opciones = []
        fuente = pygame.font.Font('dejavu.ttf', 20)
        x = 105
        y = 105
        paridad = 1

        self.cursor = Cursor(x - 30, y, 30)

        for titulo, funcion in opciones:
            self.opciones.append(Opcion(fuente, titulo, x, y, paridad, funcion))
            y += 30
            if paridad == 1:
                paridad = -1
            else:
                paridad = 1

        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = False

    def actualizar(self):
        """Altera el valor de 'self.seleccionado' con los direccionales."""

        k = pygame.key.get_pressed()

        if not self.mantiene_pulsado:
            if k[K_UP]:
                self.seleccionado -= 1
            elif k[K_DOWN]:
                self.seleccionado += 1
            elif k[K_RETURN]:
                # Invoca a la función asociada a la opción.
                self.opciones[self.seleccionado].activar()

        # procura que el cursor esté entre las opciones permitidas
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1
        
        self.cursor.seleccionar(self.seleccionado)

        # indica si el usuario mantiene pulsada alguna tecla.
        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]

        self.cursor.actualizar()
     
        for o in self.opciones:
            o.actualizar()

    def imprimir(self, screen):
        """Imprime sobre 'screen' el texto de cada opción del menú."""

        self.cursor.imprimir(screen)

        for opcion in self.opciones:
            opcion.imprimir(screen)
def juego():
    main()
    

def mostrar_opciones():
    print ("Gracias por utilizar este programa.")
def creditos():
    print ("Gracias por utilizar este programa.")
def salir_del_programa():
    import sys
    print ("Gracias por utilizar este programa.")
    sys.exit(0)

def menuuu():
          salir = False

          opciones = [
              ("Jugar", juego),
              ("Creditos", creditos),
              ("Salir", salir_del_programa)
              ]

          pygame.font.init()
          screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT), 0, 32)
          fondo = pygame.image.load("fu.jpg").convert()
          menu = Menu(opciones)

          while not salir:

              for e in pygame.event.get():
                  if e.type == QUIT:
                      salir = True

              screen.blit(fondo, (0, 0))
              menu.actualizar()
              menu.imprimir(screen)

              pygame.display.flip()
              pygame.time.delay(10)

def main():
    
    
    winSurface = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT), 0, 32)
    #showStartScreen(winSurface)
    """winSurface, being the surface object returned by pygame.display.set_mode(), will be drawn to the screen
    every time pygame.display.update() is called."""

    # Uncomment either of the following lines to put the game into full screen mode.
    ##winSurface = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT), pygame.FULLSCREEN, 32)
    ##pygame.display.toggle_fullscreen()
    pygame.display.set_caption('Gorillas.py')

    #showStartScreen(winSurface)

    while True:
        #comenzar un nuevo juego.
        p1name, p2name, winPoints, gravity, nextScreen = showSettingsScreen(winSurface)
        if nextScreen == 'v':
            showIntroScreen(winSurface, p1name, p2name)

        # Restablecer la puntuación y hacer que sea el turno del primer jugador.
        p1score = 0
        p2score = 0
        turn = 1

        newRound = True
        while p1score < winPoints and p2score < winPoints:
            if newRound:
                # Al comienzo de una nueva ronda, crea un nuevo paisaje urbano, coloca los gorilas y obtén la velocidad del viento.
                skylineSurf, buildCoords = makeCityScape() # Tenga en cuenta que el horizonte de la ciudad va en skylineSurf, no winSurface.
                gorPos = placeGorillas(buildCoords)
                wind = getWind()
                newRound = False

            #Haz todo el dibujo.
            winSurface.blit(skylineSurf, (0,0))
            drawGorilla(winSurface, gorPos[0][0], gorPos[0][1], 0)
            drawGorilla(winSurface, gorPos[1][0], gorPos[1][1], 0)
            drawWind(winSurface, wind)
            drawSun(winSurface)
            displayScore(winSurface, p1score, p2score)

            pygame.display.update()

            angle, velocity = getShot(winSurface, p1name, p2name, turn)
            if turn == 1:
                gorx, gory = gorPos[0][0], gorPos[0][1]
            elif turn == 2:
                gorx, gory = gorPos[1][0], gorPos[1][1]
            result = plotShot(winSurface, skylineSurf, angle, velocity, turn, wind, 9.8, gorPos[0], gorPos[1])

            if result == 'gorilla1':
                p2score += 1
                newRound = True
                records(p2score)
                victoryDance(winSurface, gorPos[1][0], gorPos[1][1])
                
            elif result == 'gorilla2':
                p1score += 1
                newRound = True
                records(p1score)
                victoryDance(winSurface, gorPos[0][0], gorPos[0][1])
                
            if turn == 1:
                turn = 2
            else:
                turn = 1

        showGameOverScreen(winSurface, p1name, p1score, p2name, p2score)

if __name__ == '__main__':
    menuuu()#main()
