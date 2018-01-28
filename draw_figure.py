import pygame

class Draw_figure():

    def __init__(self, array, game_display):
        self._array = array
        self.size = 8
        self.color = (0,0,0)
        self.screen = game_display


    def single(self, x, y):
        pygame.draw.circle(self.screen, self.color,
                           (x , y),
                           self.size, self.size)

    def double(self, x, y):
        for i  in range(2):
            pygame.draw.circle(self.screen, self.color,
                           (x , y),
                               self.size, self.size)
            x -= 30

    def plot_figure(self, x, y, row):
        for i in range(4):
            if row[i] == 1:
                self.single(x - 15, y)
            else:
                self.double(x, y)
            y += 30

    def traverse_row(self, r, x, y, t, cnt):
        for i in range(r):
            self.plot_figure(x, y, self._array[cnt])
            x -= t
            cnt +=1

    def _draw_figure(self):
         self.traverse_row(8, 986, 60, 128, 0)
         self.traverse_row(4, 917, 250, 256, 8)
         self.traverse_row(2, 796, 440, 512, 12)
         self.traverse_row(1, 532, 630, 0, 14)
