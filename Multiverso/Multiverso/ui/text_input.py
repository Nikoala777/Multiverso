import sys
import os
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(BASE_DIR)

# Ahora la importación funcionará
import pygame
from ui.animations import render_text_with_outline

class TextInput:
    def __init__(self, x, y, font_path, width=200, height=50):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = pygame.font.Font(font_path, 40)
        self.text = ""  # El texto ingresado
        self.active = False  # Determina si el campo está activo
        self.color_inactive = (255, 255, 255)
        self.color_active = (200, 186 , 2)
        self.rect = pygame.Rect(x, y, width, height)

    def handle_event(self, event):
        """Maneja los eventos del teclado y los clics."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True  
            else:
                self.active = False 
        if event.type == pygame.KEYDOWN:
            if self.active:  
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1] 
                elif event.key == pygame.K_RETURN:
                    pass 
                else:
                    if len(self.text) < 1: 
                        if event.unicode.isdigit():
                            self.text += event.unicode  

    def draw(self, screen):
        """Dibuja el campo de texto en la pantalla."""
        color = self.color_active if self.active else self.color_inactive
        pygame.draw.rect(screen, color, self.rect, 2)
        
        text_surface = self.font.render(self.text, True, (0, 0, 0)) 
        screen.blit(text_surface, (self.x + 85, self.y)) 
