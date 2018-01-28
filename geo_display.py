mport pygame, draw_bg , draw_figure, game_menu, set_text

class Geo_display():
    def __init__(self, array, names):
        self._running = True
        self._surface = None
        self.size = self.width, self.height = 1050, 775
        self.array = array
        self.names = names
 
    def on_init(self):
        pygame.init()
        self._surface = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_render(self):
        self._surface.fill((255,255,255))
        bg = draw_bg.Draw_bg(self._surface)
        bg.draw_bg()
        fig = draw_figure.Draw_figure(self.array, self._surface)
        fig._draw_figure()
        txt = set_text.Set_text(self.names, self._surface)
        txt._set_text()
        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        menu = game_menu.Game_menu(self._surface)
        menu._run_menu()
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
                self.on_render()
        self.on_cleanup()

