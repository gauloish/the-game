import sys
import pygame

from pygame import Surface
from pygame.event import Event

from .settings import Settings
from .canvas import Background, Initial, Options, Ships, Level, Controls, Count, End
from .ship import Ship
from .enemies import Pawn, Knight, Bishop

######################################Start######################################


def checkEventsInitial(initial: Initial, background: Background) -> None:
    """Verify events in initial canvas

    Args:
        initial (Initial): initial canvas
        background (Background): background canvas
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
                background.on = True


def updateScreenInitial(
    settings: Settings, screen: Surface, background: Background, initial: Initial
) -> None:
    """Update initial canvas

    Args:
        settings (Settings): screen settings
        screen (Surface): game screen
        background (Background): background canvas
        initial (Initial): initial canvas
    """

    screen.fill(settings.back)
    background.blitBack()
    initial.blitInitial()

    if initial.state == 0:
        initial.blitStartSelect()
    elif initial.state == 1:
        initial.blitOptionSelect()

    pygame.display.flip()


#####################################Options#####################################


def checkEventsOptions(options: Options, background: Background) -> None:
    """Verify events in options canvas

    Args:
        options (Options): options canvas
        background (Background): background canvas
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
                background.on = True


def updateScreenOptions(
    settings: Settings, screen: Surface, background: Background, options: Options
) -> None:
    """Update options canvas

    Args:
        settings (Settings): screen settings
        screen (Surface): game screen
        background (Background): background canvas
        initial (Initial): options canvas
    """

    screen.fill(settings.back)
    background.blitBack()
    options.blitOptions()

    if options.state == 0:
        options.blitShipSelect()
    elif options.state == 1:
        options.blitLevelSelect()
    elif options.state == 2:
        options.blitControlSelect()
    elif options.state == 3:
        options.blitBackSelect()

    pygame.display.flip()


###################################Ship Choose###################################


def checkEventsShips(ships: Ships, background: Background) -> None:
    """Verify events in ships canvas

    Args:
        ships (Ships): ships canvas
        background (Background): background canvas
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
                background.on = True


def updateScreenShips(
    settings: Settings, screen: Surface, background: Background, ships: Ships
) -> None:
    """Update ships canvas

    Args:
        settings (Settings): screen settings
        screen (Surface): game screen
        background (Background): background canvas
        ships (Ships): ships canvas
    """

    screen.fill(settings.back)
    background.blitBack()
    ships.blitBoxes()
    ships.blitSelect()
    pygame.display.flip()


##################################Level Choose##################################


def checkEventsLevel(level: Level, background: Background) -> None:
    """Verify events in ships canvas

    Args:
        ships (Ships): ships canvas
        background (Background): background canvas
    """

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_UP, pygame.K_w]:
                level.number = (level.number - 1) % 4

            if event.key in [pygame.K_DOWN, pygame.K_s]:
                level.number = (level.number + 1) % 4

            if event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                level.back = True

            if event.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
                background.on = True


def updateScreenLevel(
    settings: Settings, screen: Surface, background: Background, level: Level
) -> None:
    """Update level canvas

    Args:
        settings (Settings): screen settings
        screen (Surface): game screen
        background (Background): background canvas
        level (Level): level canvas
    """

    screen.fill(settings.back)
    background.blitBack()
    level.blitLevels()

    if level.number == 0:
        level.blitEasySelect()
    elif level.number == 1:
        level.blitMediumSelect()
    elif level.number == 2:
        level.blitHardSelect()
    elif level.number == 3:
        level.blitInsaneSelect()

    pygame.display.flip()


####################################Controls####################################


def checkEventsControls(controls: Controls, background: Background) -> None:
    """Verify events in control canvas

    Args:
        constrols (Controls): controls canvas
        background (Background): background canvas
    """

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                controls.back = True

            if event.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
                background.on = True


def updateScreenControls(
    settings: Settings,
    screen: Surface,
    background: Background,
    controls: Controls,
) -> None:
    """Update controls canvas

    Args:
        settings (Settings): screen settings
        screen (Surface): game screen
        background (Background): background canvas
        controls (Constrols): controls canvas
    """

    screen.fill(settings.back)
    background.blitBack()
    controls.blitControls()
    pygame.display.flip()


#####################################Count#####################################


def updateScreenCount(
    settings: Settings,
    screen: Surface,
    background: Background,
    count: Count,
    number: int,
) -> None:
    """Update count canvas

    Args:
        settings (Settings): screen settings
        screen (Surface): game screen
        background (Background): background canvas
        count (Count): count canvas
        number (int): count number
    """

    screen.fill(settings.back)
    background.blitBack()
    count.blitNumber(number)
    pygame.display.flip()


######################################Game######################################


def checkEventsLead(ship: Ship, background: Background) -> None:
    """Verify events in lead canvas

    Args:
        ship (Ship): ship canvas
        background (Background): background canvas
    """

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            keydownEventLead(event, ship, background)
        elif event.type == pygame.KEYUP:
            keyupEventLead(event, ship)


def keydownEventLead(event: Event, ship: Ship, background: Background) -> None:
    """Verify keydown events in lead canvas

    Args:
        screen (Surface): game screen
        event (pygame.Event): event
        ship (Ship): ship canvas
        background (Background): background canvas
    """

    if event.key in [pygame.K_RIGHT, pygame.K_d]:
        ship.moving_right = True
    if event.key in [pygame.K_LEFT, pygame.K_a]:
        ship.moving_left = True

    if event.key == pygame.K_SPACE:
        ship.bullet.moving = True

    if event.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
        background.on = True


def keyupEventLead(event: Event, ship: Ship) -> None:
    """Verify keyup events in lead canvas

    Args:
        event (pygame.Event): event
        ship (Ship): ship canvas
    """

    if event.key in [pygame.K_RIGHT, pygame.K_d]:
        ship.moving_right = False
    if event.key in [pygame.K_LEFT, pygame.K_a]:
        ship.moving_left = False


def updateScreenLead(
    settings: Settings,
    screen: Surface,
    background: Background,
    ship: Ship,
    enemy: Pawn | Knight | Bishop,
) -> None:
    """Update lead canvas

    Args:
        settings (Settings): screen settings
        screen (Surface): game screen
        background (Background): background canvas
        ship (Ship): ship canvas
        enemy (Pawn | Knight | Bishop): enemy canvas
    """

    screen.fill(settings.back)
    background.blitBack()
    ship.bullet.blitme()
    ship.blitme()
    enemy.blitme()
    pygame.display.flip()


def gameOver(defeat: bool) -> bool:
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


def updateEnd(
    settings: Settings,
    screen: Surface,
    background: Background,
    end: End,
    defeat: bool,
) -> None:
    """Update end canvas

    Args:
        settings (Settings): screen settings
        screen (Surface): game screen
        background (Background): background canvas
        end (End): end canvas
        defeat (bool): player defeat
    """

    screen.fill(settings.back)
    background.blitBack()
    end.blitEnd(defeat)
    pygame.display.flip()
