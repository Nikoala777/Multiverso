import sys
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(BASE_DIR)

from universos.estructuras_datos import thg as ed


import heapq
import llist as l
from collections import deque
import queue as q
import universos.estructuras_datos.thg as ed
import universos.escalas.fund_escalas as fe

def scale_random_vector(tetra1, tetra2, inverso):
    escala = []
    current_freq = fe.frequency
    intervalos = {"T": 2, "st": 1, "T1/2": 3}
    print(tetra1, tetra2)
    
    for intervalo in tetra1:
        escala.append((current_freq, inverso[current_freq]))
        current_freq *= 2 ** (intervalos[intervalo] / 12)
        current_freq = fe.nota_mas_cercana(current_freq, inverso)
    
    escala.append((current_freq, inverso[current_freq]))
    
    for intervalo in tetra2:
        current_freq *= 2 ** (intervalos[intervalo] / 12)
        current_freq = fe.nota_mas_cercana(current_freq, inverso)
        escala.append((current_freq, inverso[current_freq]))
    
    return escala

def scale_random_dlist(tetra1, tetra2, inverso):
    escala = l.dllist(scale_random_vector(tetra1, tetra2, inverso))
    return escala

def scale_random_sllist(tetra1, tetra2, inverso):
    escala = l.sllist()
    for nota in scale_random_vector(tetra1, tetra2, inverso):
        escala.append(nota)
    return escala

def scale_random_tupla(tetra1, tetra2, inverso):
    return tuple(scale_random_vector(tetra1, tetra2, inverso))

def scale_random_queue(tetra1, tetra2, inverso):
    q_escala = q.Queue()
    for nota in scale_random_vector(tetra1, tetra2, inverso):
        q_escala.put(nota)
    return q_escala

def scale_random_stack(tetra1, tetra2, inverso):
    pila = q.LifoQueue()
    for nota in (scale_random_vector(tetra1, tetra2, inverso)):
        pila.put(nota)
    return pila

def scale_random_deque(tetra1, tetra2, inverso):
    dq = deque(scale_random_vector(tetra1, tetra2, inverso))
    return dq

def scale_random_bst(tetra1, tetra2, inverso):
    escala = scale_random_vector(tetra1, tetra2, inverso)
    raiz = None
    for freq, nombre in escala:
        raiz = ed.insertar_bst(raiz, freq, nombre)
    return raiz

def scale_random_avl(tetra1, tetra2, inverso):
    escala = scale_random_vector(tetra1, tetra2, inverso)
    raiz = None
    for freq, nombre in escala:
        raiz = ed.insertar_avl(raiz, freq, nombre)
    return raiz

def construir_min_heap(tetra1, tetra2, inverso):
    heap = []
    for nota in scale_random_vector(tetra1, tetra2, inverso):
        heapq.heappush(heap, nota)
    return heap

def construir_max_heap(tetra1, tetra2, inverso):
    heap = []
    for freq, nombre in scale_random_vector(tetra1, tetra2, inverso):
        heapq.heappush(heap, (-freq, nombre))
    return heap

def construir_grafo_escala(tetra1, tetra2, inverso):
    escala = scale_random_vector(tetra1, tetra2, inverso)
    grafo = {}
    for i in range(len(escala) - 1):
        nodo_actual = escala[i][0]
        nodo_siguiente = escala[i + 1][0]
        grafo.setdefault(nodo_actual, []).append(nodo_siguiente)
        grafo.setdefault(nodo_siguiente, [])
    return grafo

def scale_modo_hash(base_freq, modo, inverso):
    escala = scale_random_vector(base_freq, modo, inverso)
    tabla = ed.HashScale(size=16)
    
    for freq, nombre in escala:
        tabla.insert(freq, nombre)

    return tabla

