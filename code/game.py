import pygame

from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(600, 480))

    def run(self):
        while True:
            menu = Menu(self.screen)
            menu.run()
            pass

    # o laço for serve para checar todos os eventos (ações) do código (jogo)
    #  for event in pygame.event.get():
    #   if event.type == pygame.QUIT:
    #          pygame.quit()
    #          quit()
