import sys
import os
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(BASE_DIR)
import pygame
from ui.text_input import TextInput
from ui.animations import *
from universos.escalas.escalas_modos import scale_modo_vector as smv
from universos.escalas.fund_escalas import crear_diccionario_notas as cdn

class OctaveMode:
    def __init__(self, game, tonalidad):
        self.game = game
        self.tonalidad = tonalidad
        self.font = pygame.font.Font(os.path.join(BASE_DIR, "assets", "fonts", "nasaf.ttf"), 40)
        self.selected_octave = 4
        self.selected_mode = 0
        self.modes = ["Jónico", "Dórico", "Frigio", "Lidio", "Mixolidio", "Eólico", "Locrio", "Random"]
        self.transition = TransitionEffect(self.game)
        self.in_transition = True
        self.octave_input = TextInput(295, 150, os.path.join(BASE_DIR, "assets", "fonts", "nasaf.ttf"))
        self.transition_done = False
        self.note_freq=0
        self.dic, self.inv = cdn(2, 8)

    def handle_events(self, events):
        """Maneja los eventos de teclado y entrada del usuario."""
        for event in events:
            self.octave_input.handle_event(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.octave_input.rect.collidepoint(event.pos):
                    self.octave_input.active = True
                elif self.travel_rect.collidepoint(event.pos):
                    try:
                        self.selected_octave = int(self.octave_input.text)
                        print(self.selected_octave)
                        print(self.tonalidad)

                        if self.selected_octave > 1 and self.selected_octave < 8:
                            print(self.dic.items()) 
                            
                            for tone, freq in self.dic.items():
                                if tone == f"{self.tonalidad}{self.selected_octave}":
                                    print(freq, tone, f"== {self.tonalidad}{self.selected_octave} ???")
                                    self.note_freq = freq
                                    break
                                    
                            self.game.change_scene("nebulosa", self.note_freq, self.selected_octave, self.selected_mode)
                        else:
                            # Si los datos no son válidos, muestra un mensaje de error o algo visual
                            print("Datos incorrectos")
                    except ValueError:
                        # Si los campos contienen valores no numéricos, no hacer nada
                        print("Por favor ingresa números válidos")

        # Otros eventos como teclas
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.selected_mode = (self.selected_mode + 1) % len(self.modes)
                elif event.key == pygame.K_LEFT:
                    self.selected_mode = (self.selected_mode - 1) % len(self.modes)
                elif event.key == pygame.K_RETURN:
                    pass  # No hacer nada cuando se presiona Enter
                # ...


    def update(self):
        """Actualiza la transición y la lógica interna."""
        self.transition.update()
        if self.transition.transition_done and self.in_transition:
            self.in_transition = False

    def draw(self, screen):
        """Dibuja la pantalla actual y los elementos de la interfaz."""
        background = pygame.image.load(os.path.join(BASE_DIR, "assets", "images", "bright.png"))
        screen.blit(pygame.transform.scale(background, screen.get_size()), (0, 0))

        if self.in_transition:
            self.transition.draw(screen)
        else:
            tonalidad_surface = render_text_with_outline(self.tonalidad, self.font, (186, 120, 2), (0, 0, 0), 2)
            tonalidad_rect = tonalidad_surface.get_rect(center=(395, 50))
            screen.blit(tonalidad_surface, tonalidad_rect)

            mode_surface = render_text_with_outline(f"Modo: {self.modes[self.selected_mode]}", self.font, (255, 255, 255), (0, 0, 0), 2)
            mode_rect = mode_surface.get_rect(center=(400, 350))
            screen.blit(mode_surface, mode_rect)
            
            # Dibuja el campo de entrada de altura
            height_surface = render_text_with_outline("Altura: ", self.font, (255, 255, 255), (0, 0, 0), 2)
            height_rect = height_surface.get_rect(center=(400, 250))
            screen.blit(height_surface, height_rect)
            
            mouse_pos = pygame.mouse.get_pos()
            
            # Crear superficie base de "Viajar"
            travel_text = "Viajar"
            base_color = (186, 120, 2)  # Color original (naranja oscuro)
            hover_color = (255, 200, 0)  # Color al hacer hover (naranja brillante)
            
            # Determinar si el mouse está sobre "Viajar"
            travel_surface = render_text_with_outline(travel_text, self.font, base_color, (0, 0, 0), 2)
            self.travel_rect = travel_surface.get_rect(center=(400, 500))
            is_hover = self.travel_rect.collidepoint(mouse_pos)
            
            # Aplicar efecto hover si es necesario
            if is_hover:
                # Crear versión escalada y con color de hover
                scaled_surface = render_text_with_outline(travel_text, self.font, hover_color, (0, 0, 0), 2)
                scaled_surface = pygame.transform.smoothscale(
                    scaled_surface, 
                    (int(scaled_surface.get_width() * 1.4), 
                    int(scaled_surface.get_height() * 1.4)
                ))
                scaled_rect = scaled_surface.get_rect(center=(400, 500))
                screen.blit(scaled_surface, scaled_rect)
            else:
                # Dibujar versión normal
                screen.blit(travel_surface, self.travel_rect)
            self.octave_input.draw(screen)