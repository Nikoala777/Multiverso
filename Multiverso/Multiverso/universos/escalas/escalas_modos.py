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


def scale_modo_vector(base_freq, modo, inverso):
    intervalos = fe.get_intervals_mode(modo)
    escala = []

    current_freq = fe.nota_mas_cercana(base_freq, inverso)  

    for intervalo in intervalos:
        if current_freq not in inverso:
            print(f"❌ ERROR: {current_freq} no está en inverso")
            print(f"Claves en inverso: {list(inverso.keys())[:10]}")  # Debug

        nota_actual = inverso.get(current_freq, "???")  
        escala.append((current_freq, nota_actual))  

        nueva_freq = current_freq * 2 ** (intervalo / 12)  
        current_freq = fe.nota_mas_cercana(nueva_freq, inverso) 

    escala.append((current_freq, inverso.get(current_freq, "???")))  
    return escala


def scale_modo_dlist(base_freq, modo, inverso):
    return l.dllist(scale_modo_vector(base_freq, modo, inverso))

def scale_modo_sllist(base_freq, modo, inverso):
    escala = l.sllist()
    for nota in scale_modo_vector(base_freq, modo, inverso):
        escala.append(nota)
    return escala

def scale_modo_tupla(base_freq, modo, inverso):
    return tuple(scale_modo_vector(base_freq, modo, inverso))

def scale_modo_queue(base_freq, modo, inverso):
    q_escala = q.Queue()
    for nota in scale_modo_vector(base_freq, modo, inverso):
        q_escala.put(nota)
    return q_escala

def scale_modo_stack(base_freq, modo, inverso):
    pila = q.LifoQueue()
    for nota in (scale_modo_vector(base_freq, modo, inverso)):
        pila.put(nota)
    return pila

def scale_modo_deque(base_freq, modo, inverso):
    return deque(scale_modo_vector(base_freq, modo, inverso))

def scale_modo_bst(base_freq, modo, inverso):
    escala = scale_modo_vector(base_freq, modo, inverso)
    raiz = None
    for freq, nombre in escala:
        raiz = ed.insertar_bst(raiz, freq, nombre)
    return raiz

def scale_modo_avl(base_freq, modo, inverso):
    escala = scale_modo_vector(base_freq, modo, inverso)
    raiz = None
    for freq, nombre in escala:
        raiz = ed.insertar_avl(raiz, freq, nombre)
    return raiz

def construir_min_heap_modo(base_freq, modo, inverso):
    heap = []
    for nota in scale_modo_vector(base_freq, modo, inverso):
        heapq.heappush(heap, nota)
    return heap

def construir_max_heap_modo(base_freq, modo, inverso):
    heap = []
    for freq, nombre in scale_modo_vector(base_freq, modo, inverso):
        heapq.heappush(heap, (-freq, nombre))
    return heap

def construir_grafo_modo(base_freq, modo, inverso):
    escala = scale_modo_vector(base_freq, modo, inverso)
    grafo = {}
    for i in range(len(escala) - 1):
        nodo_actual = escala[i][0]
        nodo_siguiente = escala[i + 1][0]
        grafo.setdefault(nodo_actual, []).append(nodo_siguiente)
        grafo.setdefault(nodo_siguiente, [])
    return grafo

def scale_modo_hash(base_freq, modo, inverso):
    escala = scale_modo_vector(base_freq, modo, inverso)
    tabla = ed.HashScale(size=16)
    
    for freq, nombre in escala:
        tabla.insert(freq, nombre)

    return tabla

