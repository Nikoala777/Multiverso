import sys
import os
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(BASE_DIR)

import pygame
from scenes.circle import circle
from scenes.octaveMode import OctaveMode  # Importa la nueva escena de 
from scenes.nebula import Nebulosa
from scenes.nebuchords import Nebuchord

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Multiverso de Escalas")
        self.clock = pygame.time.Clock()
        self.running = True
        self.scene = circle(self)  # Inicia con el círculo de quintas
        self.selected_note = None  # Guarda la nota seleccionada

    def change_scene(self, scene_name, *args):
        print(f"🔄 Intentando cambiar a la escena: {scene_name} con args {args}")
        if scene_name == "octave_mode":
            self.scene = OctaveMode(self, *args)
        elif scene_name == "nebulosa":  
            self.scene = Nebulosa(self, *args)
        elif scene_name == "nebuchord":
            self.scene = Nebuchord(self, *args)
        elif scene_name == "menu":
            self.scene = circle(self, *args)




    def run(self):
        while self.running:
            events = pygame.event.get()  
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.scene.handle_events(events)
            self.screen.fill((0, 0, 0)) 
            self.scene.update() 
            self.scene.draw(self.screen) 
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
