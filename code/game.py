import pygame

from code.const import WIN_WHIDTH, WIN_HEIGHT
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(WIN_WHIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.screen)
            menu.run()
            pass
