import pygame

class Draw_bg():
    def __init__(self, game_display):
        self.screen = game_display
        self.color = ( 0, 0, 0)
        self.thick = 8

    def draw_border(self, a):
        for i in range(4):
            pygame.draw.rect(self.screen, self.color,
                             [ 10, a, 1030, 188 ]
                             ,self.thick)
            a += 188

    def draw_grid(self, a, b, c, d, r):
        for i in range(r):
            pygame.draw.line(self.screen, self.color,
                             ( a, b),( a, c), self.thick)
            a -= d

    def draw_bg(self):
        self.draw_border(10)
        self.draw_grid(902, 10, 198, 128, 7)
        self.draw_grid(774, 198, 386, 256, 3)
        self.draw_grid(518, 386, 574, 512, 1)
