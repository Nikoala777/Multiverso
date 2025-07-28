import sys
import os
import pygame
import math
import random 
from colorsys import hls_to_rgb
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(BASE_DIR)
from ui.animations import *
from universos.escalas.escalas_modos import scale_modo_vector as smv
from universos.escalas.fund_escalas import crear_diccionario_notas as cdn
from audio import reproductor_order as rp
from audio import reproductor_norder as nrp
from universos.acordes import acordes as ac

diccionario, inverso = cdn(2, 9)

class Nebulosa:
    def __init__(self, game, tonalidad, octave, mode):
        self.game = game
        self.tonalidad = tonalidad
        self.octave = octave
        self.mode = mode
        self.notes = smv(tonalidad, mode, inverso)
        self.font = pygame.font.Font(os.path.join(BASE_DIR, "assets", "fonts", "nasaf.ttf"), 40)
        self.background_image = pygame.image.load(os.path.join(BASE_DIR, "assets", "images", "nebula.png"))
        self.note_radius = 40
        self.in_transition = True
        self.transition = TransitionEffect(self.game)
        self.delete_mode = False
        self.v_eliminate = False
        self.vr_eliminate = False
        self.v_eliminate = False
        self.vr_eliminate = False
        self.s_eliminate = False
        self.sr_eliminate = False
        self.q_eliminate = False
        self.qr_eliminate = False
        self.d_eliminate = False
        self.dr_eliminate = False
        self.q_eliminate = False
        self.qr_eliminate = False
        self.h_eliminate = False
        self.hr_eliminate = False
        self.b_eliminate = False
        self.br_eliminate = False
        self.dl_eliminate = False  
        self.dlr_eliminate = False
        self.sll_eliminate = False
        self.sllr_eliminate = False  
        self.tur_eliminate = False
        self.tu_eliminate = False
        self.har_eliminate = False
        self.ha_eliminate = False
        self.avl_eliminate = False
        self.avlr_eliminate = False
        self.gr_eliminate= False
        self.g_eliminate= False

        
        
        # 🔥 Generar colores complementarios aleatorios para cada nota
        self.color_pairs = []
        for _ in self.notes:
            base_hue = random.random()  # Valor entre 0 y 1
            comp_hue = (base_hue + 0.5) % 1.0  # Complementario en HSL
            
            base_lightness = 0.6
            comp_lightness = 0.55  # Ligera diferencia para contraste

            base_color = self.hls_to_platinado(base_hue, base_lightness)
            comp_color = self.hls_to_platinado(comp_hue, comp_lightness)
            
            self.color_pairs.append((base_color, comp_color))
            
    def handle_events(self, events):
        """Maneja los eventos, incluyendo clic en notas y teclas."""
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if self.delete_button_rect and self.delete_button_rect.collidepoint(mouse_pos):
                    # Cambiar el estado de 'delete_mode'
                    self.delete_mode = not self.delete_mode
                    print(self.delete_mode)
                else: 
                    self.check_note_click(mouse_pos)
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.game.change_scene("menu") 

                elif event.key == pygame.K_SPACE and hasattr(self, "selected_note_index"):
                    self.game.change_scene("nebuchord", self.tonalidad, self.octave, self.mode)

    def check_note_click(self, mouse_pos):
        """Verifica si se hizo clic en alguna nota y dispara el evento."""
        for note_info in self.get_current_note_positions():
            x = note_info['x']
            y = note_info['y']
            radius = note_info['radius']
            position = note_info['position']
            
            # Calcular distancia del click al centro de la nota
            distance = math.sqrt((mouse_pos[0] - x)**2 + (mouse_pos[1] - y)**2)
            
            if distance <= radius:
                self.selected_note_index = position 
                self.on_note_clicked(position)
                print(self.get_current_note_positions())
                break  # Solo procesa el primer clic

    def get_current_note_positions(self):
        """Devuelve las posiciones actuales de las notas con sus propiedades."""
        screen = self.game.screen
        screen_width, screen_height = screen.get_size()
        note_data = []
        
        # Replicar lógica de posicionamiento del draw()
        num_notas = len(self.notes)
        start_x = 100
        end_x = screen_width - 100
        spacing = (end_x - start_x) / (num_notas - 1) if num_notas > 1 else 0
        ARC_HEIGHT = 100
        
        for i, (freq, note) in enumerate(self.notes):
            angle = (i / (num_notas - 1)) * math.pi
            x = start_x + (i * spacing)
            y = (screen_height // 2) - ARC_HEIGHT * math.sin(angle)
            
            # Calcular radio actual (con hover)
            current_radius = self.note_radius
            note_rect = pygame.Rect(
                x - current_radius, y - current_radius, 
                current_radius * 2, current_radius * 2
            )
            is_hover = note_rect.collidepoint(pygame.mouse.get_pos())
            
            if is_hover:
                current_radius = int(self.note_radius * 1.4)
                note_data.append({
                'x': x,
                'y': y,
                'radius': current_radius,
                'position': i,
                'freq': freq,
                'note': note
            })
                
        
        return note_data
        
    """def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                transicion"""
                
    def on_note_clicked(self, index):
        prom=random.random()
        tetra1= ac.gen_tetrachords_random()
        tetra2= ac.gen_tetrachords_random()
        print(self.delete_mode)
        if self.mode == 7:
            if prom<0.09:
                if self.vr_eliminate == False and self.delete_mode == True:
                    print("Eliminando universos VECTOR...")
                    nrp.play_scale_vector(tetra1, tetra2, inverso, index)
                    self.vr_eliminate=True
                elif self.vr_eliminate == True:
                    print("Se intento acceder a un universo VECTOR pero han sido eliminados")
                elif self.vr_eliminate == False and self.delete_mode == True:
                    nrp.play_scale_vector(tetra1, tetra2, inverso, index)
                
            elif prom>=0.08 and prom<0.16:
                if self.sr_eliminate == False and self.delete_mode == True:
                    print("Eliminando universos STACK...")
                    nrp.play_scale_stack(tetra1, tetra2, inverso, index)
                    self.sr_eliminate=True
                elif self.sr_eliminate == True:
                    print("Se intento acceder a un universo STACK pero han sido eliminados")
                elif self.sr_eliminate == False:
                    nrp.play_scale_stack(tetra1, tetra2, inverso, index)
            elif prom>=0.16 and prom<0.24:
                if self.qr_eliminate == False and self.delete_mode == True:
                    print("Eliminando universos QUEUE...")
                    nrp.play_scale_queue(tetra1, tetra2, inverso, index)
                    self.qr_eliminate=True
                elif self.qr_eliminate == True:
                    print("Se intento acceder a un universo QUEUE pero han sido eliminados")
                elif self.qr_eliminate == False:
                    nrp.play_scale_queue(tetra1, tetra2, inverso, index)
            elif prom>=0.24 and prom<0.32:
                if self.dr_eliminate == False and self.delete_mode == True:
                    print("Eliminando universos DEQUE...")
                    nrp.play_scale_deque(tetra1, tetra2, inverso, index)
                    self.dr_eliminate=True
                elif self.dr_eliminate == True:
                    print("Se intento acceder a un universo DEQUE pero han sido eliminados")
                elif self.dr_eliminate == False:
                    nrp.play_scale_deque(tetra1, tetra2, inverso, index)
            elif prom>=0.32 and prom<0.40:
                if self.hr_eliminate == False and self.delete_mode == True:
                    print("Eliminando universos HEAP...")
                    nrp.play_scale_heap(tetra1, tetra2, inverso, index)
                    self.hr_eliminate=True
                elif self.hr_eliminate == True:
                    print("Se intento acceder a un universo HEAP pero han sido eliminados")
                elif self.hr_eliminate == False:
                    nrp.play_scale_heap(tetra1, tetra2, inverso, index)
            elif prom>=0.40 and prom<0.48:
                if self.br_eliminate == False and self.delete_mode == True:
                    print("Eliminando universos BST...")
                    nrp.play_scale_bst(tetra1, tetra2, inverso, index)
                    self.br_eliminate=True
                elif self.br_eliminate == True:
                    print("Se intento acceder a un universo BST pero han sido eliminados")
                elif self.br_eliminate == False:
                    nrp.play_scale_bst(tetra1, tetra2, inverso, index)
            elif prom>=0.48 and prom<0.56:
                if self.br_eliminate == False and self.delete_mode == True:
                    print("Eliminando universos AVL...")
                    nrp.play_scale_avl(tetra1, tetra2, inverso, index)
                    self.br_eliminate=True
                elif self.br_eliminate == True:
                    print("Se intento acceder a un universo AVL pero han sido eliminados")
                elif self.br_eliminate == False:
                    nrp.play_scale_avl(tetra1, tetra2, inverso, index)
            elif prom>=0.56 and prom<0.64:
                if self.br_eliminate == False and self.delete_mode == True:
                    print("Eliminando universos SLlist...")
                    nrp.play_scale_sllist(tetra1, tetra2, inverso, index)
                    self.br_eliminate=True
                elif self.br_eliminate == True:
                    print("Se intento acceder a un universo SLlist pero han sido eliminados")
                elif self.br_eliminate == False:
                    nrp.play_scale_sllist(tetra1, tetra2, inverso, index)
            elif prom>=0.64 and prom<0.72:
                if self.br_eliminate == False and self.delete_mode == True:
                    print("Eliminando universos DLlist...")
                    nrp.play_scale_dlist(tetra1, tetra2, inverso, index)
                    self.br_eliminate=True
                elif self.br_eliminate == True:
                    print("Se intento acceder a un universo DLlist pero han sido eliminados")
                elif self.br_eliminate == False:
                    nrp.play_scale_dlist(tetra1, tetra2, inverso, index)
            elif prom>=0.72 and prom<0.8:
                if self.br_eliminate == False and self.delete_mode == True:
                    print("Eliminando universos TUPLA...")
                    nrp.play_scale_tupla(tetra1, tetra2, inverso, index)
                    self.br_eliminate=True
                elif self.br_eliminate == True:
                    print("Se intento acceder a un universo TUPLA pero han sido eliminados")
                elif self.br_eliminate == False:
                    nrp.play_scale_tupla(tetra1, tetra2, inverso, index)
            elif prom>=0.8 and prom<0.88:
                if self.br_eliminate == False and self.delete_mode == True:
                    print("Eliminando universos HASH...")
                    nrp.play_scale_hash(tetra1, tetra2, inverso, index)
                    self.br_eliminate=True
                elif self.br_eliminate == True:
                    print("Se intento acceder a un universo HASH pero han sido eliminados")
                elif self.br_eliminate == False:
                    nrp.play_scale_hash(tetra1, tetra2, inverso, index)
            elif prom>=0.88 and prom<1:
                if self.br_eliminate == False and self.delete_mode == True:
                    print("Eliminando universos GRAFO...")
                    nrp.play_scale_graph(tetra1, tetra2, inverso, index)
                    self.br_eliminate=True
                elif self.br_eliminate == True:
                    print("Se intento acceder a un universo GRAFO pero han sido eliminados")
                elif self.br_eliminate == False:
                    nrp.play_scale_graph(tetra1, tetra2, inverso, index)
        else:
            if prom<0.08:
                if self.v_eliminate == False and self.delete_mode == True:
                    print("Eliminando universos VECTOR...")
                    rp.play_scale_vector(self.tonalidad, self.mode, inverso, index)
                    self.v_eliminate=True
                elif self.v_eliminate == True:
                    print("Se intento acceder a un universo VECTOR pero han sido eliminados")
                elif self.v_eliminate == False:
                    rp.play_scale_vector(self.tonalidad, self.mode, inverso, index)
            elif prom>=0.08 and prom<0.16:
                if self.s_eliminate == False and self.delete_mode == True:
                    print("Eliminando universos STACK...")
                    rp.play_scale_stack(self.tonalidad, self.mode, inverso, index)
                    self.s_eliminate=True
                elif self.s_eliminate == True:
                    print("Se intento acceder a un universo STACK pero han sido eliminados")
                elif self.s_eliminate == False:
                    rp.play_scale_stack(self.tonalidad, self.mode, inverso, index)
            elif prom>=0.16 and prom<0.24:
                if self.q_eliminate == False and self.delete_mode == True:
                    print("Eliminando universos QUEUE...")
                    rp.play_scale_queue(self.tonalidad, self.mode, inverso, index)
                    self.q_eliminate=True
                elif self.q_eliminate == True:
                    print("Se intento acceder a un universo QUEUE pero han sido eliminados")
                elif self.q_eliminate == False:
                    rp.play_scale_queue(self.tonalidad, self.mode, inverso, index)
            elif prom>=0.24 and prom<0.32:
                if self.d_eliminate == False and self.delete_mode == True:
                    print("Eliminando universos DEQUE...")
                    rp.play_scale_deque(self.tonalidad, self.mode, inverso, index)
                    self.d_eliminate=True
                elif self.d_eliminate == True:
                    print("Se intento acceder a un universo DEQUE pero han sido eliminados")
                elif self.d_eliminate == False:
                    rp.play_scale_deque(self.tonalidad, self.mode, inverso, index)
            elif prom>=0.32 and prom<0.40:
                if self.h_eliminate == False and self.delete_mode == True:
                    print("Eliminando universos HEAP...")
                    rp.play_scale_heap(self.tonalidad, self.mode, inverso, index)
                    self.h_eliminate=True
                elif self.h_eliminate == True:
                    print("Se intento acceder a un universo HEAP pero han sido eliminados")
                elif self.h_eliminate == False:
                    rp.play_scale_heap(self.tonalidad, self.mode, inverso, index)
            elif prom>=0.40 and prom<0.48:
                if self.b_eliminate == False and self.delete_mode == True:
                    print("Eliminando universos BST...")
                    rp.play_scale_bst(self.tonalidad, self.mode, inverso, index)
                    self.b_eliminate=True
                elif self.b_eliminate == True:
                    print("Se intento acceder a un universo BST pero han sido eliminados")
                elif self.b_eliminate == False:
                    rp.play_scale_bst(self.tonalidad, self.mode, inverso, index)
            elif prom>=0.48 and prom<0.56:
                if self.br_eliminate == False and self.delete_mode == True:
                    print("Eliminando universos AVL...")
                    rp.play_scale_avl(self.tonalidad, self.mode, inverso, index)
                    self.br_eliminate=True
                elif self.br_eliminate == True:
                    print("Se intento acceder a un universo AVL pero han sido eliminados")
                elif self.br_eliminate == False:
                    rp.play_scale_avl(self.tonalidad, self.mode, inverso, index)
            elif prom>=0.56 and prom<0.64:
                if self.br_eliminate == False and self.delete_mode == True:
                    print("Eliminando universos SLlist...")
                    rp.play_scale_sllist(self.tonalidad, self.mode, inverso, index)
                    self.br_eliminate=True
                elif self.br_eliminate == True:
                    print("Se intento acceder a un universo SLlist pero han sido eliminados")
                elif self.br_eliminate == False:
                    rp.play_scale_sllist(self.tonalidad, self.mode, inverso, index)
            elif prom>=0.64 and prom<0.72:
                if self.br_eliminate == False and self.delete_mode == True:
                    print("Eliminando universos DLlist...")
                    rp.play_scale_dlist(self.tonalidad, self.mode, inverso, index)
                    self.br_eliminate=True
                elif self.br_eliminate == True:
                    print("Se intento acceder a un universo DLlist pero han sido eliminados")
                elif self.br_eliminate == False:
                    rp.play_scale_dlist(self.tonalidad, self.mode, inverso, index)
            elif prom>=0.72 and prom<0.80:
                if self.br_eliminate == False and self.delete_mode == True:
                    print("Eliminando universos TUPLA...")
                    rp.play_scale_tupla(self.tonalidad, self.mode, inverso, index)
                    self.br_eliminate=True
                elif self.br_eliminate == True:
                    print("Se intento acceder a un universo TUPLA pero han sido eliminados")
                elif self.br_eliminate == False:
                    rp.play_scale_tupla(self.tonalidad, self.mode, inverso, index)
            elif prom>=0.80 and prom<0.88:
                if self.br_eliminate == False and self.delete_mode == True:
                    print("Eliminando universos HASH...")
                    rp.play_scale_hash(self.tonalidad, self.mode, inverso, index)
                    self.br_eliminate=True
                elif self.br_eliminate == True:
                    print("Se intento acceder a un universo HASH pero han sido eliminados")
                elif self.br_eliminate == False:
                    rp.play_scale_hash(self.tonalidad, self.mode, inverso, index)
            elif prom>=0.88 and prom<1:
                if self.br_eliminate == False and self.delete_mode == True:
                    print("Eliminando universos GRAFO...")
                    rp.play_scale_graph(self.tonalidad, self.mode, inverso, index)
                    self.br_eliminate=True
                elif self.br_eliminate == True:
                    print("Se intento acceder a un universo GRAFO pero han sido eliminados")
                elif self.br_eliminate == False:
                    rp.play_scale_graph(self.tonalidad, self.mode, inverso, index)
        

    def update(self):
        """Actualiza la transición y la lógica interna."""
        self.transition.update()
        if self.transition.transition_done and self.in_transition:
            self.in_transition = False

    def hls_to_platinado(self, hue, lightness=0.7):
        """hue (float): Tono en el rango [0, 1]
        lightness (float): Luminosidad (0.5-0.7 para efecto metalizado)"""
        saturation = 0.4  # Saturación moderada para mantener tonos vivos pero no pastel
        metal_intensity = 0.9  # Factor de mezcla con gris (0-1)
        gray_base = 50       # Base gris para efecto metálico
        
        # Convertir HLS a RGB base
        r, g, b = hls_to_rgb(hue, lightness, saturation)
        
        # Mezclar con componente grisáceo para efecto metalizado
        metallic_r = int((r * 255 * metal_intensity) + gray_base)
        metallic_g = int((g * 255 * metal_intensity) + gray_base)
        metallic_b = int((b * 255 * metal_intensity) + gray_base)
        
        return (
            max(0, min(255, metallic_r)),
            max(0, min(255, metallic_g)),
            max(0, min(255, metallic_b))
        )

    def draw(self, screen):
        screen.blit(pygame.transform.scale(self.background_image, screen.get_size()), (0, 0))
        
        if self.in_transition:
            self.transition.draw(screen)
        else:
            screen_width = screen.get_width()
            screen_height = screen.get_height()
            num_notas = len(self.notes)
            start_x = 100
            end_x = screen_width - 100
            spacing = (end_x - start_x) / (num_notas - 1) if num_notas > 1 else 0
            ARC_HEIGHT = 100

            for i, (freq, note) in enumerate(self.notes):
                # Posición en arco
                angle = (i / (num_notas - 1)) * math.pi
                x = start_x + (i * spacing)
                y = (screen_height // 2) - ARC_HEIGHT * math.sin(angle)

                # Detectar hover
                current_radius = self.note_radius
                note_rect = pygame.Rect(x - current_radius, y - current_radius, 
                                       current_radius * 2, current_radius * 2)
                is_hover = note_rect.collidepoint(pygame.mouse.get_pos())

                # Escalado
                scale_factor = 1.4 if is_hover else 1
                scaled_radius = int(current_radius * scale_factor)

                # 🔥 Colores dinámicos
                circle_color, text_color = self.color_pairs[i]
                if is_hover:
                    circle_color = (255, 255, 255)  # Blanco
                    text_color = (255, 255, 255)    # Blanco

                # Dibujar círculo
                pygame.draw.circle(screen, circle_color, (x, y), scaled_radius)

                # 🔥 Renderizar texto con contorno negro siempre
                note_surface = render_text_with_outline(note, self.font, text_color, (0,0,0), 2)
                if is_hover:
                    note_surface = pygame.transform.smoothscale(
                        note_surface, 
                        (int(note_surface.get_width() * scale_factor), 
                        int(note_surface.get_height() * scale_factor))
                    )
                
                text_rect = note_surface.get_rect(center=(x, y))
                
                # Dibujar botón 'Eliminar'
                button_text = "Eliminar"
                # Definir colores para el botón dependiendo de si está activo
                if self.delete_mode:
                    button_color = (200, 50, 50)  # Rojo más intenso si está activo
                else:
                    button_color = (150, 20, 20)  # Rojo opaco platinado base

                # Crear el texto del botón
                delete_surface = render_text_with_outline(button_text, self.font, (255,255,255), (0,0,0), 2)
                # Definir posición (por ejemplo, esquina superior derecha)
                self.delete_button_rect = delete_surface.get_rect(topright=(screen_width - 50, 50))
                
                # Crear un rectángulo un poco más grande para el fondo
                bigger_rect = self.delete_button_rect.inflate(20, 10)
                bigger_rect.center = self.delete_button_rect.center
                
                # Dibuja el rectángulo del botón
                pygame.draw.rect(screen, button_color, bigger_rect, border_radius=10)
                
                # Dibuja el texto dentro
                screen.blit(note_surface, text_rect)
                screen.blit(delete_surface, self.delete_button_rect)