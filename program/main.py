import pygame

from .functions import (
    checkEventsInitial,
    updateScreenInitial,
    checkEventsOptions,
    updateScreenOptions,
    checkEventsShips,
    updateScreenShips,
    checkEventsLevel,
    updateScreenLevel,
    checkEventsControls,
    updateScreenControls,
    updateScreenCount,
    checkEventsLead,
    keydownEventLead,
    keyupEventLead,
    updateScreenLead,
    updateEnd,
    gameover,
)

from .settings import Settings
from .canvas import Background, Initial, Options, Ships, Level, Controls, Count, End
from .ship import Ship
from .bullets import Bullet
from .life import Life
from .enemies import Pawn, Knight, Pishop

from random import randint


def run():
    pygame.init()

    settings = Settings()
    screen = pygame.display.set_mode((settings.width, settings.height))

    pygame.display.set_caption(settings.display)

    sky = Background(screen)
    inic = Initial(screen)
    opt = Options(screen)
    ships = Ships(screen)
    level = Level(screen)
    control = Controls(screen)
    end = End(screen)

    while True:
        settings.back[0], settings.back[1], settings.back[2] = 200, 200, 200

        sky.on = True

        # Start Screen
        while True:
            checkEventsInitial(inic, sky)
            updateScreenInitial(settings, screen, sky, inic)

            if inic.val == 0:
                break
            elif inic.val == 1:
                # Options Screen
                while True:
                    checkEventsOptions(opt, sky)
                    updateScreenOptions(settings, screen, sky, opt)

                    if opt.val == 0:
                        opt.state = 0
                        opt.val = -1

                        # Ship Choose
                        while True:
                            checkEventsShips(ships, sky)
                            updateScreenShips(settings, screen, sky, ships)

                            if ships.back:
                                ships.back = False
                                break

                    elif opt.val == 1:
                        opt.state = 0
                        opt.val = -1

                        # Level Choose
                        while True:
                            checkEventsLevel(level, sky)
                            updateScreenLevel(settings, screen, sky, level)

                            if level.back:
                                level.back = False
                                break

                    elif opt.val == 2:
                        opt.state = 0
                        opt.val = -1

                        # Controls Visualizer
                        while True:
                            checkEventsControls(control, sky)
                            updateScreenControls(settings, screen, sky, control)

                            if control.back:
                                control.back = False
                                break

                    elif opt.val == 3:
                        opt.state = 0
                        opt.val = -1

                        inic.state = 0
                        inic.val = -1
                        break

        # Creating Objects
        diff = [
            [10, 8, 6, 2, 2, 2, 1, 1, 1, 1, 1],
            [12, 10, 8, 1, 2, 2, 1, 1, 2, 1, 1],
            [14, 12, 10, 1, 1, 2, 1, 2, 2, 1, 3],
            [16, 14, 12, -1, -1, 1, 2, 2, 2, 2, 5],
        ]  # [pawns, knights, pishops, vel_pawns, vel_knights, vel_pishops, lif_pawns, lif_knights, lif_pishops, vel, life]

        lel = level.lel

        ship = Ship(screen, ships.color, diff[lel][9], diff[lel][10])

        pawns = [
            Pawn(
                screen,
                randint(0, 2),
                randint(400, 800),
                diff[lel][3],
                diff[lel][6],
                ship,
            )
            for _ in range(0, diff[lel][0])
        ]
        knights = [
            Knight(
                screen,
                randint(0, 3),
                randint(200, 1000),
                diff[lel][4],
                diff[lel][7],
                ship,
            )
            for _ in range(0, diff[lel][1])
        ]
        pishops = [
            Pishop(
                screen,
                randint(0, 3),
                randint(100, 1100),
                diff[lel][5],
                diff[lel][8],
                ship,
            )
            for _ in range(0, diff[lel][2])
        ]

        enemies = pawns + knights + pishops

        defeat = False

        count = Count(screen)

        # Count
        for num in range(1, 4):
            for _ in range(0, 350):
                updateScreenCount(settings, screen, sky, count, num)

        # Game
        for enemie in enemies:
            vel = 0

            while True:
                if vel % 100 == 0 and sky.on:
                    if settings.back[0] >= 1:
                        settings.back[0] -= 1
                        settings.back[1] -= 1
                        settings.back[2] -= 1

                checkEventsLead(screen, ship, sky)

                ship.update()
                enemie.move(vel)
                ship.bullet.update(ship.rect.centerx, ship.rect.bottom)

                updateScreenLead(settings, screen, sky, ship, enemie)

                enemie.colision(ship)

                if enemie.invade():
                    ship.hit()

                    if ship.life == 0:
                        defeat = True

                    break

                if enemie.death():
                    break

                vel += 1

            if gameover(defeat):
                break

        for _ in range(0, 1500):
            updateEnd(settings, screen, sky, end, defeat)

        inic.val = -1
