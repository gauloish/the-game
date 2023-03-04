import sys
import pygame
from os.path import join
from pathlib import Path

####################################processing###################################


def getPath(path):
    """Get and resolve path

    Args:
        path (str): image path

    Returns:
        path (str): path resolved
    """

    if sys.platform in ["win32", "cygwin", "msys"]:
        path.replace("/", "\\")

    return join(Path.cwd(), path)


######################################Start######################################


def checkEventsInitial(initial, sky):
    """Verify events in initial canvas

    Args:
        initial (Initial): initial canvas
        sky (Background): background canvas
    """

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
    """Update initial canvas

    Args:
        settings (Settings): screen settings
        screen (pygame.Surface): game screen
        sky (Background): background canvas
        initial (Initial): initial canvas
    """

    screen.fill(settings.back)
    sky.blitBack()
    initial.blitInitial()

    if initial.state == 0:
        initial.blitStartSelec()
    elif initial.state == 1:
        initial.blitOptionSelec()

    pygame.display.flip()


#####################################Options#####################################


def checkEventsOptions(options, sky):
    """Verify events in options canvas

    Args:
        options (Options): options canvas
        sky (Background): background canvas
    """

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_UP, pygame.K_w]:
                options.state = (options.state - 1) % 4

            if event.key in [pygame.K_DOWN, pygame.K_s]:
                options.state = (options.state + 1) % 4

            if event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                if options.state == 0:
                    options.value = 0
                elif options.state == 1:
                    options.value = 1
                elif options.state == 2:
                    options.value = 2
                elif options.state == 3:
                    options.value = 3

            if event.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
                sky.on = True


def updateScreenOptions(settings, screen, sky, options):
    """Update options canvas

    Args:
        settings (Settings): screen settings
        screen (pygame.Surface): game screen
        sky (Background): background canvas
        initial (Initial): options canvas
    """

    screen.fill(settings.back)
    sky.blitBack()
    options.blitOptions()

    if options.state == 0:
        options.blitShipSelec()
    elif options.state == 1:
        options.blitLevelSelec()
    elif options.state == 2:
        options.blitControlSelec()
    elif options.state == 3:
        options.blitBackSelec()

    pygame.display.flip()


###################################Ship Choose###################################


def checkEventsShips(ships, sky):
    """Verify events in ships canvas

    Args:
        ships (Ships): ships canvas
        sky (Background): background canvas
    """

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_LEFT, pygame.K_a]:
                ships.color = (ships.color - 1) % 5
                ships.dist(0)

            if event.key in [pygame.K_RIGHT, pygame.K_d]:
                ships.color = (ships.color + 1) % 5
                ships.dist(1)

            if event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                ships.back = True

            if event.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
                sky.on = True


def updateScreenShips(settings, screen, sky, ships):
    """Update ships canvas

    Args:
        settings (Settings): screen settings
        screen (pygame.Surface): game screen
        sky (Background): background canvas
        ships (Ships): ships canvas
    """

    screen.fill(settings.back)
    sky.blitBack()
    ships.blitBoxes()
    ships.blitSelec()
    pygame.display.flip()


##################################Level Choose##################################


def checkEventsLevel(level, sky):
    """Verify events in ships canvas

    Args:
        ships (Ships): ships canvas
        sky (Background): background canvas
    """

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
    """Update level canvas

    Args:
        settings (Settings): screen settings
        screen (pygame.Surface): game screen
        sky (Background): background canvas
        level (Level): level canvas
    """

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


def checkEventsControls(controls, sky):
    """Verify events in control canvas

    Args:
        constrols (Controls): controls canvas
        sky (Background): background canvas
    """

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                controls.back = True

            if event.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
                sky.on = True


def updateScreenControls(settings, screen, sky, controls):
    """Update controls canvas

    Args:
        settings (Settings): screen settings
        screen (pygame.Surface): game screen
        sky (Background): background canvas
        controls (Constrols): controls canvas
    """

    screen.fill(settings.back)
    sky.blitBack()
    controls.blitControls()
    pygame.display.flip()


#####################################Count#####################################


def updateScreenCount(settings, screen, sky, count, number):
    """Update count canvas

    Args:
        settings (Settings): screen settings
        screen (pygame.Surface): game screen
        sky (Background): background canvas
        count (Count): count canvas
        number (int): count number
    """

    screen.fill(settings.back)
    sky.blitBack()
    count.blitNum(number)
    pygame.display.flip()


######################################Game######################################


def checkEventsLead(screen, ship, sky):
    """Verify events in lead canvas

    Args:
        screen (pygame.Surface): game screen
        ship (Ship): ship canvas
        sky (Background): background canvas
    """

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            keydownEventLead(screen, event, ship, sky)
        elif event.type == pygame.KEYUP:
            keyupEventLead(event, ship)


def keydownEventLead(screen, event, ship, sky):
    """Verify keydown events in lead canvas

    Args:
        screen (pygame.Surface): game screen
        event (pygame.Event): event
        ship (Ship): ship canvas
        sky (Background): background canvas
    """

    if event.key in [pygame.K_RIGHT, pygame.K_d]:
        ship.moving_right = True
    if event.key in [pygame.K_LEFT, pygame.K_a]:
        ship.moving_left = True

    if event.key == pygame.K_SPACE:
        ship.bullet.moving = True

    if event.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
        sky.on = True


def keyupEventLead(event, ship):
    """Verify keyup events in lead canvas

    Args:
        event (pygame.Event): event
        ship (Ship): ship canvas
    """

    if event.key in [pygame.K_RIGHT, pygame.K_d]:
        ship.moving_right = False
    if event.key in [pygame.K_LEFT, pygame.K_a]:
        ship.moving_left = False


def updateScreenLead(settings, screen, sky, ship, enemy):
    """Update lead canvas

    Args:
        settings (Settings): screen settings
        screen (pygame.Surface): game screen
        sky (Background): background canvas
        ship (Ship): ship canvas
        enemy (Pawn, Knight, Bishop): enemy canvas
    """

    screen.fill(settings.back)
    sky.blitBack()
    ship.bullet.blitme()
    ship.blitme()
    enemy.blitme()
    pygame.display.flip()


def gameOver(defeat):
    """Verify defeat

    Args:
        defeat (bool): player defeat

    Returns:
        bool: player defeat
    """

    if defeat:
        return True
    else:
        return False


def updateEnd(settings, screen, sky, end, defeat):
    """Update end canvas

    Args:
        settings (Settings): screen settings
        screen (pygame.Surface): game screen
        sky (Background): background canvas
        end (End): end canvas
        defeat (bool): player defeat
    """

    screen.fill(settings.back)
    sky.blitBack()
    end.blitEnd(defeat)
    pygame.display.flip()
