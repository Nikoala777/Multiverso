import pygame
import random


class TransitionEffect:
    def __init__(self, game):
        self.game = game
        self.alpha = 255 
        self.speed_lines = [(random.randint(0, self.game.screen.get_width()), random.randint(0, self.game.screen.get_height()), random.randint(10, 30)) for _ in range(20)]
        self.transition_done = False
        self.fade_state = 'fade_in'  

    def update(self):
        """Actualiza la transición dependiendo del estado."""
        
        if self.fade_state == 'fade_in':
            if self.alpha > 0:
                self.alpha -= 5 
            else:
                self.fade_state = 'fade_out' 
        elif self.fade_state == 'fade_out':
            if self.alpha < 255:
                self.alpha += 5 
            else:
                self.alpha = 255
                self.transition_done = True

        # Movimiento de las líneas
        for i in range(len(self.speed_lines)):
            x, y, speed = self.speed_lines[i]
            y += speed
            if y > self.game.screen.get_height():
                y = 0
            self.speed_lines[i] = (x, y, speed)

    def draw(self, screen):
        """Dibuja el efecto de transición en la pantalla."""
        # Fondo negro para las líneas de velocidad
        screen.fill((0, 0, 0))  
        for x, y, speed in self.speed_lines:
            pygame.draw.line(screen, (255, 255, 255), (x, y), (x, y + 20), 2)
        
        # Capa de transición con transparencia (overlay)
        overlay = pygame.Surface(self.game.screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, self.alpha))  # Aplica la transparencia (comienza invisible y aumenta)
        screen.blit(overlay, (0, 0))



def render_text_with_outline(text, font, text_color, outline_color, outline_size):
    """Renderiza un texto con un contorno."""
    base = font.render(text, True, text_color)
    width, height = base.get_size()
    outline = pygame.Surface((width + outline_size * 2, height + outline_size * 2), pygame.SRCALPHA)
    
    # Renderiza el contorno alrededor del texto
    for dx in [-outline_size, 0, outline_size]:
        for dy in [-outline_size, 0, outline_size]:
            if dx != 0 or dy != 0:
                outline.blit(font.render(text, True, outline_color), (dx + outline_size, dy + outline_size))
    
    # Renderiza el texto encima del contorno
    outline.blit(base, (outline_size, outline_size))
    return outline

