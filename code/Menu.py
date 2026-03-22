import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface


from code.Const import WIN_WIDTH


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/bg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self,):
        pygame.mixer_music.load('./asset/Menu.wav')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Mountain", COLORt_center_pos: ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", text_color=(255, 128, 0), text_center_pos: ((WIN_WIDTH / 2), 120))
            pygame.display.flip()

            # check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   pygame.quit() # close window
                   quit() # end pygame

    # new *
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, antialias=True,color=text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)

