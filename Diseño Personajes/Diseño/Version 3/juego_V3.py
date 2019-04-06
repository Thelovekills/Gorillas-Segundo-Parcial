"""
***

"""

import pygame
import sys
import time
import random
import math
from pygame.locals import *





SCR_WIDTH = 640
SCR_HEIGHT = 350
FPS = 30
GAME_CLOCK = pygame.time.Clock()


BUILDING_COLORS = ((173, 170, 173), (0, 170, 173), (173, 0, 0))
LIGHT_WINDOW = (255, 255, 82)
DARK_WINDOW = (82, 85, 82)
SKY_COLOR = (0, 0, 173)
GOR_COLOR = (86, 130, 3)
BAN_COLOR = (255, 255, 82)
EXPLOSION_COLOR = (255, 0, 0)
SUN_COLOR = (255, 255, 0)
DARK_RED_COLOR = (173, 0, 0)
BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)
GRAY_COLOR = (173, 170, 173)


BUILD_EXPLOSION_SIZE = int(SCR_HEIGHT / 50)
GOR_EXPLOSION_SIZE = 30


SUN_X = 300
SUN_Y = 10


pygame.init()
GAME_FONT = pygame.font.SysFont(None, 20)


# orientacion de la bala:
RIGHT = 0
UP = 1
LEFT = 2
DOWN = 3


# tipo de tanque a dibujar
BOTH_ARMS_DOWN = 0
LEFT_ARM_UP = 1
RIGHT_ARM_UP = 2



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
    
    pygame.quit()
    sys.exit()

def makeSurfaceFromASCII(ascii, fgColor=(255,255,255), bgColor=(0,0,0)):
    
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


sunRect = pygame.Rect(SUN_X, SUN_Y, SUN_NORMAL_SURF.get_width(), SUN_NORMAL_SURF.get_height())


def drawText(text, surfObj, x, y, fgcol, bgcol, pos='left'):
   

    textobj = GAME_FONT.render(text, 1, fgcol, bgcol)
    textrect = textobj.get_rect()

    if pos == 'left':
        textrect.topleft = (x, y)
    elif pos == 'center':
        textrect.midtop = (x, y)
    surfObj.blit(textobj, textrect) 
    
    return textrect

def getModCase(s, mod):
    
    if bool(mod & KMOD_RSHIFT or mod & KMOD_LSHIFT) ^ bool(mod & KMOD_CAPS):
        return s.swapcase()
    else:
        return s

def inputMode(prompt, screenSurf, x, y, fgcol, bgcol, maxlen=12, allowed=None, pos='left', cursor='_', cursorBlink=False):
    
    inputText = ''
    
    done = False
    cursorTimestamp = time.time()
    cursorShow = cursor
    while not done:
       

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
    
    if orient + 1 == 4:
        return 0
    else:
        return orient + 1

def drawBanana(screenSurf, orient, x, y):
   
    if orient == DOWN:
        screenSurf.blit(BAN_DOWN_SURF, (x, y))
    elif orient == UP:
        screenSurf.blit(BAN_UP_SURF, (x, y))
    elif orient == LEFT:
        screenSurf.blit(BAN_LEFT_SURF, (x, y))
    elif orient == RIGHT:
        screenSurf.blit(BAN_RIGHT_SURF, (x, y))


def drawSun(screenSurf, shocked=False):
    
    if shocked:
        screenSurf.blit(SUN_SHOCKED_SURF, (SUN_X, SUN_Y))
    else:
        screenSurf.blit(SUN_NORMAL_SURF, (SUN_X, SUN_Y))


def drawGorilla(screenSurf, x, y, arms=BOTH_ARMS_DOWN):
    

    if arms == BOTH_ARMS_DOWN:
        gorSurf = GOR_DOWN_SURF
    elif arms == LEFT_ARM_UP:
        gorSurf = GOR_LEFT_SURF
    elif arms == RIGHT_ARM_UP:
        gorSurf = GOR_RIGHT_SURF
    

    screenSurf.blit(gorSurf, (x, y))

def makeCityScape():
    

    screenSurf = pygame.Surface((SCR_WIDTH, SCR_HEIGHT)) 
    screenSurf.fill(SKY_COLOR) 

    
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

    bottomLine = 335 
    heightInc = 10 
    defBuildWidth = 37 
    randomHeightDiff = 120 
    windowWidth = 4 
    windowHeight = 7 
    windowSpacingX = 10 
    windowSpacingY = 15 
    gHeight = 25 
    

    buildingCoords = [] 
    x = 2 

    while x < SCR_WIDTH - heightInc:
        

        
        if slope == 'upward':
            newHeight += heightInc
        elif slope == 'downward':
            newHeight -= heightInc
        elif slope == 'v':
            if x > SCR_WIDTH / 2:
                newHeight -= (2 * heightInc)
                
            else:
                newHeight += (2 * heightInc)
                
        else:
            if x > SCR_WIDTH / 2:
                newHeight += (2 * heightInc)
                
            else:
                newHeight -= (2 * heightInc)
                

        
        buildWidth = defBuildWidth + random.randint(0, defBuildWidth)
        if buildWidth + x > SCR_WIDTH:
            buildWidth = SCR_WIDTH - x -2

        
        buildHeight = random.randint(heightInc, randomHeightDiff) + newHeight

        
        if bottomLine - buildHeight <= gHeight:
            buildHeight = gHeight

        
        buildingColor = BUILDING_COLORS[random.randint(0, len(BUILDING_COLORS)-1)]

        
        pygame.draw.rect(screenSurf, buildingColor, (x+1, bottomLine - (buildHeight+1), buildWidth-1, buildHeight-1))

        buildingCoords.append( (x, bottomLine - buildHeight) )

        
        for winx in range(3, buildWidth - windowSpacingX + windowWidth, windowSpacingX):
            for winy in range(3, buildHeight - windowSpacingY, windowSpacingY):
                if random.randint(1, 4) == 1:
                    winColor = DARK_WINDOW
                else:
                    winColor = LIGHT_WINDOW
                pygame.draw.rect(screenSurf, winColor, (x + 1 + winx, (bottomLine - buildHeight) + 1 + winy, windowWidth, windowHeight))

        x += buildWidth

    
    return screenSurf, buildingCoords

def placeGorillas(buildCoords):
   

    gorPos = [] 
    xAdj = int(GOR_DOWN_SURF.get_rect().width / 2)
    yAdj = GOR_DOWN_SURF.get_rect().height

    for i in range(0,2): 

        
        if i == 0:
            buildNum = random.randint(1,2)
        else:
            buildNum = random.randint(len(buildCoords)-3, len(buildCoords)-2)

        buildWidth = buildCoords[buildNum + 1][0] - buildCoords[buildNum][0]
        gorPos.append( (buildCoords[buildNum][0] + int(buildWidth / 2) - xAdj, buildCoords[buildNum][1] - yAdj - 1) )

    
    return gorPos

def waitForPlayerToPressKey():
    
    while True:
        key = checkForKeyPress()
        if key:
            return key

def checkForKeyPress():
    
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        if event.type == KEYUP:
            if event.key == K_ESCAPE: 
                terminate()
            return event.key
    return False

def showStartScreen(screenSurf):
    
    vertAdj = 0
    horAdj = 0
    while not checkForKeyPress():
        screenSurf.fill(BLACK_COLOR)

        drawStars(screenSurf, vertAdj, horAdj)
        vertAdj += 1
        if vertAdj == 4: vertAdj = 0
        horAdj += 12
        if horAdj == 84: horAdj = 0
        

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
    
    for i in range(16):
        # draw top row of stars
        screenSurf.blit(STAR_SURF, (2 + (((3 - vertAdj) + i * 4) * STAR_SURF.get_width()), 3))
        # draw bottom row of stars
        screenSurf.blit(STAR_SURF, (2 + ((vertAdj + i * 4) * STAR_SURF.get_width()), SCR_HEIGHT - 7 - STAR_SURF.get_height()))

    for i in range(4):
        # draw left column of stars going down
        screenSurf.blit(STAR_SURF, (5, 6 + STAR_SURF.get_height() + (horAdj + i * 84)))
        # draw right column of stars going up
        screenSurf.blit(STAR_SURF, (SCR_WIDTH - 5 - STAR_SURF.get_width(), (SCR_HEIGHT - (6 + STAR_SURF.get_height() + (horAdj + i * 84)))))



def showSettingsScreen(screenSurf):
    
    p1name = None
    p2name = None
    points = None
    gravity = None

    screenSurf.fill(BLACK_COLOR)

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
        angle = inputMode('Angulo:  ', screenSurf, x, 18, WHITE_COLOR, SKY_COLOR, maxlen=3, allowed='0123456789')
    if angle is None: terminate()
    angle = int(angle)

    velocity = ''
    while velocity == '':
        velocity = inputMode('Velocidad:  ', screenSurf, x, 34, WHITE_COLOR, SKY_COLOR, maxlen=3, allowed='0123456789')
    if velocity is None: terminate()
    velocity = int(velocity)

    
    drawText('Angulo:   ' + str(angle), screenSurf, x, 2, SKY_COLOR, SKY_COLOR)
    drawText('Velocidad:   ' + str(angle), screenSurf, x, 2, SKY_COLOR, SKY_COLOR)
    pygame.display.update()

    if playerNum == 2:
        angle = 180 - angle

    return (angle, velocity)

def displayScore(screenSurf, oneScore, twoScore):
    
    drawText(str(oneScore) + '>Score<' + str(twoScore), screenSurf, 270, 310, WHITE_COLOR, SKY_COLOR, pos='left')

def plotShot(screenSurf, skylineSurf, angle, velocity, playerNum, wind, gravity, gor1, gor2):
    
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
                
                sunHit = True

            
            drawSun(screenSurf, shocked=sunHit)

            if bananaRect.colliderect(gor1rect):
                
                doExplosion(screenSurf, skylineSurf, bananaRect.centerx, bananaRect.centery, explosionSize=int(GOR_EXPLOSION_SIZE*2/3), speed=0.005)
                doExplosion(screenSurf, skylineSurf, bananaRect.centerx, bananaRect.centery, explosionSize=GOR_EXPLOSION_SIZE, speed=0.005)
                drawSun(screenSurf)
                return 'gorilla1'
            elif bananaRect.colliderect(gor2rect):
                # banana has hit player 2
                doExplosion(screenSurf, skylineSurf, bananaRect.centerx, bananaRect.centery, explosionSize=int(GOR_EXPLOSION_SIZE*2/3), speed=0.005)
                doExplosion(screenSurf, skylineSurf, bananaRect.centerx, bananaRect.centery, explosionSize=GOR_EXPLOSION_SIZE, speed=0.005)
                screenSurf.fill(SKY_COLOR, bananaRect) # erase banana
                drawSun(screenSurf)
                return 'gorilla2'
            elif collideWithNonColor(srcPixArray, screenSurf, bananaRect, SKY_COLOR):
                # banana has hit a building
                doExplosion(screenSurf, skylineSurf, bananaRect.centerx, bananaRect.centery)
                screenSurf.fill(SKY_COLOR, bananaRect) # erase banana
                drawSun(screenSurf)
                return 'building'

        del srcPixArray
        

        screenSurf.blit(bananaSurf, (bananaRect.topleft))
        pygame.display.update()
        time.sleep(0.02)

        screenSurf.fill(SKY_COLOR, bananaRect) 

        t += 0.1 
    drawSun(screenSurf)
    return 'miss'

def victoryDance(screenSurf, x, y):
    
    for i in range(4):
        screenSurf.blit(GOR_LEFT_SURF, (x, y))
        pygame.display.update()
        time.sleep(0.3)
        screenSurf.blit(GOR_RIGHT_SURF, (x, y))
        pygame.display.update()
        time.sleep(0.3)


def collideWithNonColor(pixArr, surfObj, rect, color):
    
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
    
    wind = random.randint(5, 15)
    if random.randint(0, 1):
        wind *= -1
    return wind

def drawWind(screenSurf, wind):
    
    if wind != 0:
        wind *= 3
        pygame.draw.line(screenSurf, EXPLOSION_COLOR, (int(SCR_WIDTH / 2), SCR_HEIGHT - 5), (int(SCR_WIDTH / 2) + wind, SCR_HEIGHT - 5))
        # draw the arrow end
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


def main():
    winSurface = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT), 0, 32)
    
    pygame.display.set_caption('Gorillas.py')

    showStartScreen(winSurface)

    while True:
        
        p1name, p2name, winPoints, gravity, nextScreen = showSettingsScreen(winSurface)
        if nextScreen == 'v':
            showIntroScreen(winSurface, p1name, p2name)

        
        p1score = 0
        p2score = 0
        turn = 1

        newRound = True
        while p1score < winPoints and p2score < winPoints:
            if newRound:
                
                skylineSurf, buildCoords = makeCityScape()
                gorPos = placeGorillas(buildCoords)
                wind = getWind()
                newRound = False

            # Do all the drawing.
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
                victoryDance(winSurface, gorPos[1][0], gorPos[1][1])
                p2score += 1
                newRound = True
            elif result == 'gorilla2':
                victoryDance(winSurface, gorPos[0][0], gorPos[0][1])
                p1score += 1
                newRound = True

            if turn == 1:
                turn = 2
            else:
                turn = 1

        showGameOverScreen(winSurface, p1name, p1score, p2name, p2score)

if __name__ == '__main__':
    main()
