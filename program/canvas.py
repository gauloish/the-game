import pygame

from .functions import getPath


class Background:
    def __init__(self, screen):
        self.screen = screen

        self.back = pygame.image.load(getPath("images/sky/sky.png"))

        self.rect_back = self.back.get_rect()
        self.screen_back = self.screen.get_rect()

        self.rect_back.centerx = 600
        self.rect_back.bottom = 800

        self.on = False

    def blitBack(self):
        self.screen.blit(self.back, self.rect_back)


class Initial:
    def __init__(self, screen):
        self.screen = screen

        self.initial = pygame.image.load(getPath("images/elements/initial/initial.png"))
        self.start_select = pygame.image.load(
            getPath("images/elements/initial/start_select.png")
        )
        self.option_select = pygame.image.load(
            getPath("images/elements/initial/option_select.png")
        )

        self.rect_initial = self.initial.get_rect()
        self.rect_start_select = self.start_select.get_rect()
        self.rect_option_select = self.option_select.get_rect()

        self.screen_rect_initial = self.screen.get_rect()
        self.screen_rect_start_select = self.screen.get_rect()
        self.screen_rect_option_select = self.screen.get_rect()

        self.rect_initial.centerx = 600
        self.rect_start_select.centerx = 592
        self.rect_option_select.centerx = 600

        self.rect_initial.bottom = 645
        self.rect_start_select.bottom = 569
        self.rect_option_select.bottom = 637

        self.state = 0
        self.val = -1

    def blitInitial(self):
        self.screen.blit(self.initial, self.rect_initial)

    def blitStartSelec(self):
        self.screen.blit(self.start_select, self.rect_start_select)

    def blitOptionSelec(self):
        self.screen.blit(self.option_select, self.rect_option_select)


class Options:
    def __init__(self, screen):
        self.screen = screen

        self.opt = pygame.image.load(getPath("images/elements/options/options.png"))
        self.ships_select = pygame.image.load(
            getPath("images/elements/options/ships_select.png")
        )
        self.level_select = pygame.image.load(
            getPath("images/elements/options/level_select.png")
        )
        self.controls_select = pygame.image.load(
            getPath("images/elements/options/controls_select.png")
        )
        self.back_select = pygame.image.load(
            getPath("images/elements/options/back_select.png")
        )

        self.rect_opt = self.opt.get_rect()
        self.rect_ships_select = self.ships_select.get_rect()
        self.rect_level_select = self.level_select.get_rect()
        self.rect_controls_select = self.controls_select.get_rect()
        self.rect_back_select = self.back_select.get_rect()

        self.screen_opt = self.screen.get_rect()
        self.screen_ships_select = self.screen.get_rect()
        self.screen_level_select = self.screen.get_rect()
        self.screen_controls_select = self.screen.get_rect()
        self.screen_back_select = self.screen.get_rect()

        self.rect_opt.centerx = 600
        self.rect_ships_select.centerx = 600
        self.rect_level_select.centerx = 600
        self.rect_controls_select.centerx = 600
        self.rect_back_select.centerx = 600

        self.rect_opt.bottom = 660
        self.rect_ships_select.bottom = 246
        self.rect_level_select.bottom = 330
        self.rect_controls_select.bottom = 414
        self.rect_back_select.bottom = 652

        self.state = 0
        self.val = -1

    def blitOptions(self):
        self.screen.blit(self.opt, self.rect_opt)

    def blitShipSelec(self):
        self.screen.blit(self.ships_select, self.rect_ships_select)

    def blitLevelSelec(self):
        self.screen.blit(self.level_select, self.rect_level_select)

    def blitControlSelec(self):
        self.screen.blit(self.controls_select, self.rect_controls_select)

    def blitBackSelec(self):
        self.screen.blit(self.back_select, self.rect_back_select)


class Ships:
    def __init__(self, screen):
        self.screen = screen

        self.boxes = pygame.image.load(
            getPath("images/elements/options/ships/boxes.png")
        )
        self.select = pygame.image.load(
            getPath("images/elements/options/ships/select.png")
        )

        self.rect_boxes = self.boxes.get_rect()
        self.rect_select = self.select.get_rect()

        self.screen_rect_boxes = self.screen.get_rect()
        self.screen_rect_select = self.screen.get_rect()

        self.rect_boxes.centerx = 600
        self.rect_select.centerx = 352

        self.rect_boxes.bottom = 462
        self.rect_select.bottom = 462

        self.color = 0
        self.back = False

    def blitBoxes(self):
        self.screen.blit(self.boxes, self.rect_boxes)

    def blitSelec(self):
        self.screen.blit(self.select, self.rect_select)

    def dist(self, num):  # 352 476 600 724 848
        right = {352: 476, 476: 600, 600: 724, 724: 848, 848: 352}
        left = {352: 848, 476: 352, 600: 476, 724: 600, 848: 724}

        if num == 0:
            self.rect_select.centerx = left[self.rect_select.centerx]
        if num == 1:
            self.rect_select.centerx = right[self.rect_select.centerx]


class Level:
    def __init__(self, screen):
        self.screen = screen

        self.levels = pygame.image.load(
            getPath("images/elements/options/level/levels.png")
        )
        self.easy_select = pygame.image.load(
            getPath("images/elements/options/level/easy_select.png")
        )
        self.medium_select = pygame.image.load(
            getPath("images/elements/options/level/medium_select.png")
        )
        self.hard_select = pygame.image.load(
            getPath("images/elements/options/level/hard_select.png")
        )
        self.insane_select = pygame.image.load(
            getPath("images/elements/options/level/insane_select.png")
        )

        self.rect_levels = self.levels.get_rect()
        self.rect_easy_select = self.easy_select.get_rect()
        self.rect_medium_select = self.medium_select.get_rect()
        self.rect_hard_select = self.hard_select.get_rect()
        self.rect_insane_select = self.insane_select.get_rect()

        self.screen_opt = self.screen.get_rect()
        self.screen_easy_select = self.screen.get_rect()
        self.screen_medium_select = self.screen.get_rect()
        self.screen_hard_select = self.screen.get_rect()
        self.screen_insane_select = self.screen.get_rect()

        self.rect_levels.centerx = 600
        self.rect_easy_select.centerx = 600
        self.rect_medium_select.centerx = 600
        self.rect_hard_select.centerx = 600
        self.rect_insane_select.centerx = 600

        self.rect_levels.bottom = 550
        self.rect_easy_select.bottom = 290
        self.rect_medium_select.bottom = 372
        self.rect_hard_select.bottom = 460
        self.rect_insane_select.bottom = 542

        self.lel = 0
        self.back = False

    def blitLevels(self):
        self.screen.blit(self.levels, self.rect_levels)

    def blitEasySelec(self):
        self.screen.blit(self.easy_select, self.rect_easy_select)

    def blitMediumSelec(self):
        self.screen.blit(self.medium_select, self.rect_medium_select)

    def blitHardSelec(self):
        self.screen.blit(self.hard_select, self.rect_hard_select)

    def blitInsaneSelec(self):
        self.screen.blit(self.insane_select, self.rect_insane_select)


class Controls:
    def __init__(self, screen):
        self.screen = screen

        self.cont = pygame.image.load(
            getPath("images/elements/options/controls/controls.png")
        )

        self.rect_cont = self.cont.get_rect()
        self.screen_cont = self.screen.get_rect()

        self.rect_cont.centerx = 600
        self.rect_cont.bottom = 660

        self.back = False

    def blitControls(self):
        self.screen.blit(self.cont, self.rect_cont)


class Count:
    def __init__(self, screen):
        self.screen = screen

        self.number_1 = pygame.image.load(getPath("images/elements/start/number_1.png"))
        self.number_2 = pygame.image.load(getPath("images/elements/start/number_2.png"))
        self.number_3 = pygame.image.load(getPath("images/elements/start/number_3.png"))

        self.rect_number_1 = self.number_1.get_rect()
        self.rect_number_2 = self.number_2.get_rect()
        self.rect_number_3 = self.number_3.get_rect()

        self.screen_number_1 = self.screen.get_rect()
        self.screen_number_2 = self.screen.get_rect()
        self.screen_number_3 = self.screen.get_rect()

        self.rect_number_1.centerx = 600
        self.rect_number_2.centerx = 600
        self.rect_number_3.centerx = 600

        self.rect_number_1.bottom = 500
        self.rect_number_2.bottom = 500
        self.rect_number_3.bottom = 500

    def blitNum(self, num):
        if num == 1:
            self.screen.blit(self.number_1, self.rect_number_1)
        elif num == 2:
            self.screen.blit(self.number_2, self.rect_number_2)
        elif num == 3:
            self.screen.blit(self.number_3, self.rect_number_3)


class End:
    def __init__(self, screen):
        self.screen = screen

        self.gameover = pygame.image.load(getPath("images/elements/final/gameover.png"))
        self.victory = pygame.image.load(getPath("images/elements/final/victory.png"))

        self.rect_gameover = self.gameover.get_rect()
        self.rect_victory = self.victory.get_rect()

        self.screen_gameover = self.screen.get_rect()
        self.screen_victory = self.screen.get_rect()

        self.rect_gameover.centerx = 600
        self.rect_victory.centerx = 600

        self.rect_gameover.bottom = 525
        self.rect_victory.bottom = 456

    def blitEnd(self, defeat):
        if defeat:
            self.screen.blit(self.gameover, self.rect_gameover)
        else:
            self.screen.blit(self.victory, self.rect_victory)
