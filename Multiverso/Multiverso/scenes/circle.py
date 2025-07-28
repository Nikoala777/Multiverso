import sys
import os
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(BASE_DIR)

import math
import pygame
from ui.buttons import Note

class circle:
    def __init__(self, game):
        self.game = game
        self.notes = []
        self.font_path = "assets/fonts/nasaf.ttf"
        self.center = (400, 300)
        self.radius = 150

        note_names = ["C", "G", "D", "A", "E", "B", "F#", "C#", "G#", "D#", "A#", "F"]
        angle_step = 2 * math.pi / len(note_names)

        for i, note in enumerate(note_names):
            angle = angle_step * i
            x = self.center[0] + self.radius * math.cos(angle)
            y = self.center[1] + self.radius * math.sin(angle)

            self.notes.append(Note(note, x, y, self.font_path, (180, 180, 180), (255, 255, 255)))
    def handle_events(self, events):
        mouse_pos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for note in self.notes:
                    
                    if note.is_hovered:
                        print(f"✅ Nota seleccionada: {note.text}") 
                        self.game.change_scene("octave_mode", note.text)




        for note in self.notes:
            note.check_hover(mouse_pos)

    def draw(self, screen):
        """Dibuja el fondo cósmico y el círculo de quintas."""
        background = pygame.image.load(os.path.join(BASE_DIR, "assets", "images", "cosmos.png"))
        screen.blit(pygame.transform.scale(background, screen.get_size()), (0, 0))

        for note in self.notes:
            note.draw(screen, pygame.mouse.get_pos())
            
    def update(self):
        pass  # No hace nada, pero evita el error

