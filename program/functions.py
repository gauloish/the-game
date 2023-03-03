import sys
import pygame
from os.path import join
from pathlib import Path

####################################processing###################################


def getPath(path):
    if sys.platform in ["win32", "cygwin", "msys"]:
        path.replace("/", "\\")

    return join(Path.cwd(), path)


######################################Start######################################


def checkEventsInitial(initial, sky):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_UP, pygame.K_w]:
                initial.state = (initial.state - 1) % 2

            if event.key in [pygame.K_DOWN, pygame.K_s]:
                initial.state = (initial.state + 1) % 2

            if event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                if initial.state == 0:
                    initial.value = 0
                elif initial.state == 1:
                    initial.value = 1

            if event.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
                sky.on = True


def updateScreenInitial(settings, screen, sky, initial):
    screen.fill(settings.back)
    sky.blitBack()
    initial.blitInitial()

    if initial.state == 0:
        initial.blitStartSelec()
    elif initial.state == 1:
        initial.blitOptionSelec()

    pygame.display.flip()


#####################################Options#####################################


def checkEventsOptions(option, sky):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_UP, pygame.K_w]:
                option.state = (option.state - 1) % 4

            if event.key in [pygame.K_DOWN, pygame.K_s]:
                option.state = (option.state + 1) % 4

            if event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                if option.state == 0:
                    option.value = 0
                elif option.state == 1:
                    option.value = 1
                elif option.state == 2:
                    option.value = 2
                elif option.state == 3:
                    option.value = 3

            if event.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
                sky.on = True


def updateScreenOptions(settings, screen, sky, option):
    screen.fill(settings.back)
    sky.blitBack()
    option.blitOptions()

    if option.state == 0:
        option.blitShipSelec()
    elif option.state == 1:
        option.blitLevelSelec()
    elif option.state == 2:
        option.blitControlSelec()
    elif option.state == 3:
        option.blitBackSelec()

    pygame.display.flip()


###################################Ship Choose###################################


def checkEventsShips(Ships, sky):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_LEFT, pygame.K_a]:
                Ships.color = (Ships.color - 1) % 5
                Ships.dist(0)

            if event.key in [pygame.K_RIGHT, pygame.K_d]:
                Ships.color = (Ships.color + 1) % 5
                Ships.dist(1)

            if event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                Ships.back = True

            if event.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
                sky.on = True


def updateScreenShips(settings, screen, sky, Ships):
    screen.fill(settings.back)
    sky.blitBack()
    Ships.blitBoxes()
    Ships.blitSelec()
    pygame.display.flip()


##################################Level Choose##################################


def checkEventsLevel(level, sky):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_UP, pygame.K_w]:
                level.lel = (level.lel - 1) % 4

            if event.key in [pygame.K_DOWN, pygame.K_s]:
                level.lel = (level.lel + 1) % 4

            if event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                level.back = True

            if event.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
                sky.on = True


def updateScreenLevel(settings, screen, sky, level):
    screen.fill(settings.back)
    sky.blitBack()
    level.blitLevels()

    if level.lel == 0:
        level.blitEasySelec()
    elif level.lel == 1:
        level.blitMediumSelec()
    elif level.lel == 2:
        level.blitHardSelec()
    elif level.lel == 3:
        level.blitInsaneSelec()

    pygame.display.flip()


####################################Controls####################################


def checkEventsControls(control, sky):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                control.back = True

            if event.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
                sky.on = True


def updateScreenControls(settings, screen, sky, control):
    screen.fill(settings.back)
    sky.blitBack()
    control.blitControls()
    pygame.display.flip()


#####################################Count#####################################


def updateScreenCount(settings, screen, sky, count, num):
    screen.fill(settings.back)
    sky.blitBack()
    count.blitNum(num)
    pygame.display.flip()


######################################Game######################################


def checkEventsLead(screen, ship, sky):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            keydownEventLead(screen, event, ship, sky)
        elif event.type == pygame.KEYUP:
            keyupEventLead(event, ship)


def keydownEventLead(screen, event, ship, sky):
    if event.key in [pygame.K_RIGHT, pygame.K_d]:
        ship.moving_right = True
    if event.key in [pygame.K_LEFT, pygame.K_a]:
        ship.moving_left = True

    if event.key == pygame.K_SPACE:
        ship.bullet.moving = True

    if event.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
        sky.on = True


def keyupEventLead(event, ship):
    if event.key in [pygame.K_RIGHT, pygame.K_d]:
        ship.moving_right = False
    if event.key in [pygame.K_LEFT, pygame.K_a]:
        ship.moving_left = False


def updateScreenLead(settings, screen, sky, ship, enemie):
    screen.fill(settings.back)
    sky.blitBack()
    ship.bullet.blitme()
    ship.blitme()
    enemie.blitme()
    pygame.display.flip()


def gameover(defeat):
    if defeat:
        return True
    else:
        return False


def updateEnd(settings, screen, sky, end, defeat):
    screen.fill(settings.back)
    sky.blitBack()
    end.blitEnd(defeat)
    pygame.display.flip()
