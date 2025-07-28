import sys
import os
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(BASE_DIR)

# Ahora la importación funcionará
import pygame
import ui.animations as an# 🔹 Importamos la función de contorno

# Ruta absoluta para la fuente
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
FONT_PATH = os.path.join(BASE_DIR, "assets", "fonts", "nasaf.ttf")

class Note:
    def __init__(self, text, x, y, font_path, normal_color, hover_color):
        self.text = text
        self.x = x
        self.y = y
        self.font_path = FONT_PATH 
        self.normal_color = (180, 180, 180) 
        self.hover_color = (255, 255, 255)  
        self.is_hovered = False
        self.size = 32  

    def draw(self, screen, mouse_pos):
        """Dibuja la nota con contorno oscuro."""
        font_size = int(self.size * 1.2) if self.is_hovered else self.size
        font = pygame.font.Font(self.font_path, font_size)
        color = self.hover_color if self.is_hovered else self.normal_color

        text_surface = an.render_text_with_outline(self.text, font, color, (0, 0, 0), 2)
        text_rect = text_surface.get_rect(center=(self.x, self.y))
        screen.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):
        """Detecta si el cursor está sobre la nota y cambia el estado."""
        font = pygame.font.Font(self.font_path, self.size)
        text_surface = font.render(self.text, True, self.normal_color)
        text_rect = text_surface.get_rect(center=(self.x, self.y))
        self.is_hovered = text_rect.collidepoint(mouse_pos)
