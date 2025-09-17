import pygame

from code.const import WIN_WHIDTH, WIN_HEIGHT, MENU_OPTION
from code.level import Level
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(WIN_WHIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.screen)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.screen, 'Level 1', menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()
            else:
                pass
