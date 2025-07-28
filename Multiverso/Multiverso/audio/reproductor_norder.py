import collections
import sys
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(BASE_DIR)

import random
import pygame
import numpy as np
import universos.escalas.escalas_random as er
import heapq

def generate_wave(freq, duration=0.5, sample_rate=44100):
    """Genera una onda sinusoidal para el sonido"""
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = 0.5 * np.sin(2 * np.pi * freq * t)
    wave = (wave * 32767).astype(np.int16)
    return pygame.sndarray.make_sound(np.column_stack((wave, wave)))

def play_scale_vector(tetra1, tetra2, invers, index, play_mode="full"):
    print("Este universo es un vector")
    pygame.mixer.init()
    escala = er.scale_random_vector(tetra1, tetra2, invers)
    
    if random.random() < 0.5:
        play_mode = "single"

    try:
        if play_mode == "full":
            for i, (freq, nombre) in enumerate(escala[:index+1]):
                print(f'Reproduciendo: {nombre} ({freq} Hz)')
                generate_wave(freq).play()
                pygame.time.delay(500)
        elif play_mode == "single":
            freq, nombre = escala[index]
            print(f'Reproduciendo: {nombre} ({freq} Hz)')
            generate_wave(freq).play()
            pygame.time.delay(500)
    finally:
        pygame.mixer.quit()

# ─────────────────────────────────────────────────────────────────────
# Reproductor para DList (lista doblemente enlazada)
def play_scale_dlist(tetra1, tetra2, invers, index):
    print("Este universo es una lista doblemente enlazada (DList).")
    pygame.mixer.init()
    dlist = er.scale_random_dlist(tetra1, tetra2, invers)

    # Modo de reproducción: full o single
    play_mode = "full" if random.random() < 0.5 else "single"

    try:
        if play_mode == "full":
            i = 0
            node = dlist.first
            while node and i <= index:
                freq, nombre = node.value
                print(f'[DLIST] Reproduciendo: {nombre} ({freq} Hz)')
                generate_wave(freq).play()
                pygame.time.delay(500)
                node = node.next
                i += 1
        else:
            # Single: solo la nota en 'index'
            # Recorremos hasta llegar a index
            node = dlist.first
            i = 0
            while node and i < index:
                node = node.next
                i += 1
            if node:
                freq, nombre = node.value
                print(f'[DLIST SINGLE] Reproduciendo: {nombre} ({freq} Hz)')
                generate_wave(freq).play()
                pygame.time.delay(500)
    finally:
        pygame.mixer.quit()


# ─────────────────────────────────────────────────────────────────────
# Reproductor para SList (lista simplemente enlazada)
def play_scale_sllist(tetra1, tetra2, invers, index):
    print("Este universo es una lista simplemente enlazada (SList).")
    pygame.mixer.init()
    sll = er.scale_random_sllist(tetra1, tetra2, invers)

    play_mode = "full" if random.random() < 0.5 else "single"

    try:
        if play_mode == "full":
            i = 0
            node = sll.first
            while node and i <= index:
                freq, nombre = node.value
                print(f'[SLLIST] Reproduciendo: {nombre} ({freq} Hz)')
                generate_wave(freq).play()
                pygame.time.delay(500)
                node = node.next
                i += 1
        else:
            # single
            node = sll.first
            i = 0
            while node and i < index:
                node = node.next
                i += 1
            if node:
                freq, nombre = node.value
                print(f'[SLLIST SINGLE] Reproduciendo: {nombre} ({freq} Hz)')
                generate_wave(freq).play()
                pygame.time.delay(500)
    finally:
        pygame.mixer.quit()


# ─────────────────────────────────────────────────────────────────────
# Reproductor para tupla
def play_scale_tupla(tetra1, tetra2, invers, index):
    print("Este universo es una tupla (inmutable).")
    pygame.mixer.init()
    tupla_escala = er.scale_random_tupla(tetra1, tetra2, invers)

    # Reproducir todo (hasta index) o solo la nota en 'index'
    play_mode = "full" if random.random() < 0.5 else "single"

    try:
        if play_mode == "full":
            for i, (freq, nombre) in enumerate(tupla_escala[:index+1]):
                print(f'[TUPLA] Reproduciendo: {nombre} ({freq} Hz)')
                generate_wave(freq).play()
                pygame.time.delay(500)
        else:
            freq, nombre = tupla_escala[index]
            print(f'[TUPLA SINGLE] Reproduciendo: {nombre} ({freq} Hz)')
            generate_wave(freq).play()
            pygame.time.delay(500)
    finally:
        pygame.mixer.quit()


# ─────────────────────────────────────────────────────────────────────
# Reproductor para Stack (LIFO)
def play_scale_stack(tetra1, tetra2, invers, index):
    print("Este universo es un stack (LIFO: Último en entrar, primero en salir).")
    pygame.mixer.init()
    pila = er.scale_random_stack(tetra1, tetra2, invers)
    
    try:
        # Reproducir hasta 'index' elementos de la pila
        i = 0
        while not pila.empty() and i <= index:
            freq, nombre = pila.get()  # LIFO: saca el último ingresado
            print(f'[STACK] Reproduciendo: {nombre} ({freq} Hz)')
            generate_wave(freq).play()
            pygame.time.delay(500)
            i += 1
    finally:
        pygame.mixer.quit()


# ─────────────────────────────────────────────────────────────────────
# Reproductor para Queue (FIFO)
def play_scale_queue(tetra1, tetra2, invers, index):
    print("Este universo es una cola (FIFO: Primero en entrar, primero en salir).")
    pygame.mixer.init()
    cola = er.scale_random_queue(tetra1, tetra2, invers)
    
    try:
        i = 0
        while not cola.empty() and i <= index:
            freq, nombre = cola.get()  # FIFO
            print(f'[QUEUE] Reproduciendo: {nombre} ({freq} Hz)')
            generate_wave(freq).play()
            pygame.time.delay(500)
            i += 1
    finally:
        pygame.mixer.quit()


# ─────────────────────────────────────────────────────────────────────
# Reproductor para Deque
def play_scale_deque(tetra1, tetra2, invers, index, play_mode="left_to_right"):
    print("Este universo es un deque (doble terminación).")
    pygame.mixer.init()
    escala = er.scale_random_deque(tetra1, tetra2, invers)
    
    # Elección aleatoria de dirección
    play_mode = random.choice(["left_to_right", "right_to_left"])
    print(f"Recorrido: {'Front → Back' if play_mode == 'left_to_right' else 'Back → Front'}")

    try:
        elements = list(escala)
        if play_mode == "left_to_right":
            elements = elements[:index+1]
        else:
            elements = elements[-(index+1):][::-1]  # Toma los últimos 'index+1' y los invierte

        for freq, nombre in elements:
            print(f'[DEQUE] Reproduciendo: {nombre} ({freq} Hz)')
            generate_wave(freq).play()
            pygame.time.delay(500)
    finally:
        pygame.mixer.quit()


# ─────────────────────────────────────────────────────────────────────
# Reproductor para BST
def play_scale_bst(tetra1, tetra2, invers, index):
    print("Este universo es un Árbol Binario de Búsqueda (BST).")
    pygame.mixer.init()
    raiz = er.scale_random_bst(tetra1, tetra2, invers)
    play_mode = random.choice(["inorder", "preorder", "postorder"])
    print(f"Recorrido BST: {play_mode.upper()}")

    class Counter:
        def __init__(self):
            self.count = 0

    def traverse(node, counter, order):
        if node and counter.count <= index:
            if order == "preorder":
                play_node(node, counter)
                traverse(node.left, counter, order)
                traverse(node.right, counter, order)
            elif order == "inorder":
                traverse(node.left, counter, order)
                play_node(node, counter)
                traverse(node.right, counter, order)
            elif order == "postorder":
                traverse(node.left, counter, order)
                traverse(node.right, counter, order)
                play_node(node, counter)

    def play_node(node, counter):
        print(f'[BST {play_mode.upper()}] Reproduciendo: {node.nombre} ({node.freq} Hz)')
        generate_wave(node.freq).play()
        pygame.time.delay(500)
        counter.count += 1

    try:
        counter = Counter()
        traverse(raiz, counter, play_mode)
    finally:
        pygame.mixer.quit()


# ─────────────────────────────────────────────────────────────────────
# Reproductor para AVL
def play_scale_avl(tetra1, tetra2, invers, index):
    print("Este universo es un Árbol AVL (balanceado).")
    pygame.mixer.init()
    raiz = er.scale_random_avl(tetra1, tetra2, invers)
    play_mode = random.choice(["inorder", "preorder", "postorder"])
    print(f"Recorrido AVL: {play_mode.upper()}")

    class Counter:
        def __init__(self):
            self.count = 0

    def traverse(node, counter, order):
        if node and counter.count <= index:
            if order == "preorder":
                play_node(node, counter)
                traverse(node.left, counter, order)
                traverse(node.right, counter, order)
            elif order == "inorder":
                traverse(node.left, counter, order)
                play_node(node, counter)
                traverse(node.right, counter, order)
            elif order == "postorder":
                traverse(node.left, counter, order)
                traverse(node.right, counter, order)
                play_node(node, counter)

    def play_node(node, counter):
        print(f'[AVL {play_mode.upper()}] Reproduciendo: {node.nombre} ({node.frecuencia} Hz)')
        generate_wave(node.frecuencia).play()
        pygame.time.delay(500)
        counter.count += 1

    try:
        counter = Counter()
        traverse(raiz, counter, play_mode)
    finally:
        pygame.mixer.quit()


# ─────────────────────────────────────────────────────────────────────
# Reproductor para Heap
def play_scale_heap(tetra1, tetra2, invers, index):
    pygame.mixer.init()
    is_min_heap = random.random() < 0.5
    print(f"Este universo es un {'min' if is_min_heap else 'max'} heap.")
    
    heap = (er.construir_min_heap if is_min_heap else er.construir_min_heap)(tetra1, tetra2, invers)
    
    try:
        for i in range(min(index + 1, len(heap))):
            if is_min_heap:
                freq, nombre = heapq.heappop(heap)
            else:
                freq, nombre = heapq.heappop(heap)
                freq = -freq  # Revertir para max heap
                
            print(f'[HEAP] Reproduciendo: {nombre} ({freq} Hz)')
            generate_wave(freq).play()
            pygame.time.delay(500)
    finally:
        pygame.mixer.quit()


# ─────────────────────────────────────────────────────────────────────
# Reproductor para Hash
def play_scale_hash(tetra1, tetra2, invers, index):
    print("Este universo es un Hash (tabla hash con encadenamiento).")
    pygame.mixer.init()
    tabla_hash = er.scale_modo_hash(tetra1, tetra2, invers)

    # Decidir si reproducimos un subconjunto (hasta index) o una sola
    if random.random() < 0.5:
        play_mode = "full"
    else:
        play_mode = "single"

    # Extraemos todos los pares (freq, nombre) de la tabla
    items_list = list(tabla_hash.items())  # Devuelve pares (k, v)
    # Ordenar por freq para reproducir en orden asc, solo como ejemplo
    items_list.sort(key=lambda x: x[0])

    try:
        if play_mode == "full":
            # Reproducimos hasta 'index' en orden ascendente
            subset = items_list[:index+1]
            for freq, nombre in subset:
                print(f'[HASH] Reproduciendo: {nombre} ({freq} Hz)')
                generate_wave(freq).play()
                pygame.time.delay(500)
        else:
            # Reproducir solo la 'index'-ésima nota (si existe)
            if index < len(items_list):
                freq, nombre = items_list[index]
                print(f'[HASH SINGLE] Reproduciendo: {nombre} ({freq} Hz)')
                generate_wave(freq).play()
                pygame.time.delay(500)
    finally:
        pygame.mixer.quit()


# ─────────────────────────────────────────────────────────────────────
# Reproductor para Acordes (ejemplo)
def play_scale_chords(tetra1, tetra2, invers, index):
    print("Este universo reproducirá acordes (raíz, tercera y quinta).")
    pygame.mixer.init(frequency=44100, size=-16, channels=2)

    scale = er.scale_random_vector(tetra1, tetra2, invers)  # Lista con las notas de la escala
    
    def play_chord(i):
        """ Reproduce el acorde de la nota en i con su tercera y quinta """
        if i >= len(scale):
            return

        # Nota raíz
        root_freq, root_name = scale[i]
        # Tercera
        third_freq, third_name = scale[(i + 2) % len(scale)]
        # Quinta
        fifth_freq, fifth_name = scale[(i + 4) % len(scale)]

        print(f'[CHORD] Acorde de {root_name}: {root_freq} Hz, {third_freq} Hz, {fifth_freq} Hz')

        root_sound = generate_wave(root_freq)
        third_sound = generate_wave(third_freq)
        fifth_sound = generate_wave(fifth_freq)

        root_sound.play()
        third_sound.play()
        fifth_sound.play()
        pygame.time.delay(700)

    play_chord(index)

    pygame.mixer.quit()

def play_scale_graph(tetra1, tetra2, invers, index):
    print("Este universo es un Grafo (GRAPH). Realizaremos un recorrido BFS.")
    pygame.mixer.init()
    grafo = er.construir_grafo_escala(tetra1, tetra2, invers)
    escala = er.scale_random_vector(tetra1, tetra2, invers)
    freq_to_name = {freq: nombre for freq, nombre in escala}

    #Nodo inicial
    start_freq = escala[0][0]

    # Bfs
    visited = set()
    queue = collections.deque([start_freq])
    visited.add(start_freq)

    count = 0  # Contador de nodos

    try:
        while queue and count <= index:
            current = queue.popleft()
            nombre_nota = freq_to_name.get(current, "???")
            
            print(f'[GRAPH BFS] Visitando nodo #{count+1}: Reproduciendo {nombre_nota} ({current} Hz)')

            generate_wave(current).play()
            pygame.time.delay(500)

            count += 1

            for neighbor in grafo.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    finally:
        pygame.mixer.quit()
