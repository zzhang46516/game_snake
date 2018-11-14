import random, pygame, sys
from pygame.locals import *

FPS = 20
WINDOWWIDTH = 640
WINDOWHEIGHT = 640

CELLSIZE = 20

CELLWIDTH = WINDOWWIDTH / 20
CELLHEIGHT = WINDOWHEIGHT / 20

WHITE = ( 255, 255, 255)
BLACK = ( 0, 0, 0)

BGCLOLOR = BLACK

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

HEAD = 0

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWNHEIGHT, WINDOWNHEIGHT))
    BASICFONT = pygame.font.SysFont("MenloforPowerline.ttf", 40)
    pygame.display.set_caption("Snake!")

    startScreeen()
    while True:
        runGame()


def runGame():
    startx = random.randint(5, CELLWIDTH)
    starty = random.randint(5, CELLHEIGHT)
    snakeCoords = [{
        'x': startx,
        'y': starty
    }, {
        'x': startx - 1,
        'y': starty
    }, {
        'x': startx - 2,
        'y': starty
    }]
    direction = DOWN
    mouse = randomLocation()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT
                        or event.key == K_a) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == K_RIGHT
                      or event.key == K_d) and direction != LEFT:
                    direction = RIGHT
                elif (event.key == K_UP
                      or event.key == K_w) and direction != DOWN:
                    direction = UP
                elif (event.key == K_DOWN
                      or event.key == K_s) and direction != UP:
                    direction = DOWN
                elif event.key == K_ESCAPE:
                    terminate()
        if snakeCoords[HEAD]['x'] == -1 or snakeCoords[HEAD][
                'x'] == CELLWIDTH or snakeCoords[HEAD][
                    'y'] == -1 or snakeCoords[HEAD]['y'] == CELLHEIGHT:
            return
        for snakeBody in snakeCoords[1:]:
            if snakeBody['x'] == snakeCoords[HEAD]['x'] and snakeBody[
                    'y'] == snakeCoords[HEAD]['y']:
                return
        if snakeCoords[HEAD]['x'] == mouse['x'] and snakeCoords[HEAD][
                'y'] == mouse['y']:
            mouse = randomLocation()
        else:
            del snakeCoords[-1]
        if direction == UP:
            newHead = {
                'x': snakeCoords[HEAD]['x'],
                'y': snakeCoords[HEAD]['y'] - 1
            }
        elif direction == DOWN:
            newHead = {
                'x': snakeCoords[HEAD]['x'],
                'y': snakeCoords[HEAD]['y'] + 1
            }
        elif direction == LEFT:
            newHead = {
                'x': snakeCoords[HEAD]['x'] - 1,
                'y': snakeCoords[HEAD]['y']
            }
        elif direction == RIGHT:
            newHead = {
                'x': snakeCoords[HEAD]['x'] + 1,
                'y': snakeCoords[HEAD]['y']
            }
        snakeCoords.insert(0, newHead)
        DISPLAYSURF.fill(BGCOLOR)
        drawSnake(snakeCoords)
        drawMouse(mouse)
        drawGrid()
        drawScore(len(snakeCoords) - 3)
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def terminate():
    pygame.quit()
    sys.exit()


def randomLocation():
    return {
        'x': random.randint(0, CELLWIDTH - 1),
        'y': random.randint(0, CELLHEIGHT - 1)
    }


def drawSnake(snakeCoords):
    for coord in snakeCoords:
        x = coord['x'] * CELLSIZE
        y = coord['y'] * CELLSIZE
        snakeSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(DISPLAYSURF, WHITE, snakeSegmentRect)
        snakeInnerSegmentRect = pygame.Rect(x + 5, y + 5, CELLSIZE - 10,
                                            CELLSIZE - 10)
        pygame.draw.rect(DISPLAYSURF, BLACK, snakeInnerSegmentRect)


def drawMouse(coord):
    x = coord['x'] * CELLSIZE
    y = coord['y'] * CELLSIZE
    mouseRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, WHITE, mouseRect)
    innerMouseRect = pygame.Rect(x + 5, y + 5, CELLSIZE - 10, CELLSIZE - 10)
    pygame.draw.rect(DISPLAYSURF, DARKGRAY, innerMouseRect)


def drawGrid():
    for x in range(0, WINDOWNWIDTH, CELLSIZE):
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINDOWNHEIGHT))
    for y in range(0, WINDOWNHEIGHT, CELLSIZE):
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINDOWNWIDTH, y))


def drawScore(score):
    scoreSurf = BASICFONT.render('Score: {0}'.format(score), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWNWIDTH - 600, 10)
    DISPLAYSURF.blit(scoreSurf, scoreRect)


def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render('Press a key to play.', True, DARKGRAY)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWNWIDTH - 200, WINDOWNHEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)


def startScreeen():
    titleFont = pygame.font.SysFont('freesansbold.ttf', 100)
    titleSurf = titleFont.render('Snake', True, WHITE)    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                return
        titleRect = titleSurf.get_rect()
        titleRect.center = (WINDOWNHEIGHT / 2, WINDOWNWIDTH / 2)
        DISPLAYSURF.fill(BGCOLOR)
        DISPLAYSURF.blit(titleSurf, titleRect)
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def showGameOverScreen():
    drawPressKeyMsg()


if __name__ == '__main__':
    main()