import pygame

class Set_text():
    def __init__(self, name_list, game_display):
        self.names = name_list
        self.screen = game_display
        self.color = (0,0,0)
        self._font = pygame.font.Font(None, 18)

    def display_names(self, a, b, c, d, e):
        for i in range(b,c):
            text = self._font.render(self.names[i], True, self.color)
            textrect = text.get_rect()
            posx = a - (textrect[2] / 2)
            self.screen.blit(text, (posx, d))
            a -= e

    def _set_text(self):
        self.display_names( 966, 0, 8, 178, 127)
        self.display_names( 902, 8, 12, 366, 256)
        self.display_names( 774, 12, 14, 554, 512)
        self.display_names( 518, 14, 15, 742, 512)
