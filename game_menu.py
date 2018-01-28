import pygame

class Game_menu():
    def __init__(self, screen):

        self.screen = screen
        self.bg_color = ( 255, 255, 255)
        self.color = ( 0, 0, 0)
        self.clock = pygame.time.Clock()
        self.menu_font = pygame.font.Font( None, 145)
        self.image = pygame.image.load( 'pentagram.png')

    def find_half(self, title, n):
        a = self.screen.get_rect()
        b = title.get_rect()
        return (a[n] /2) - (b[n] / 2)

    def _run_menu(self):
        title = self.menu_font.render("Geomancy", True,
                                     self.color)
        textx = self.find_half(title, 2)
        texty = (self.find_half(title, 3)) * 1.75
        imagex = self.find_half(self.image, 2)
        imagey = self.find_half(self.image, 3) / 2
        end_it = False
        while ( end_it == False):
            self.clock.tick(4)
            self.screen.fill(self.bg_color)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    end_it = True
                elif event.type == pygame.QUIT:
                    pygame.quit()
            self.screen.blit(self.image, (imagex, imagey))
            self.screen.blit(title, ( textx, texty))
            pygame.display.flip()
