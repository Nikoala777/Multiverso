class BSTNode:
    def __init__(self, freq, nombre):
        self.freq = freq
        self.nombre = nombre
        self.left = None
        self.right = None

def insertar_bst(raiz, freq, nombre):
    if raiz is None:
        return BSTNode(freq, nombre)
    if freq < raiz.freq:
        raiz.left = insertar_bst(raiz.left, freq, nombre)
    else:
        raiz.right = insertar_bst(raiz.right, freq, nombre)
    return raiz

class AVLNode:
    def __init__(self, frecuencia, nombre):
        self.frecuencia = frecuencia
        self.nombre = nombre
        self.left = None
        self.right = None
        self.height = 1

def altura(nodo):
    return nodo.height if nodo else 0

def balance_factor(nodo):
    return altura(nodo.left) - altura(nodo.right) if nodo else 0

def rotacion_derecha(y):
    x = y.left
    T2 = x.right
    
    x.right = y
    y.left = T2
    
    y.height = 1 + max(altura(y.left), altura(y.right))
    x.height = 1 + max(altura(x.left), altura(x.right))
    
    return x

def rotacion_izquierda(x):
    y = x.right
    T2 = y.left
    
    y.left = x
    x.right = T2
    
    x.height = 1 + max(altura(x.left), altura(x.right))
    y.height = 1 + max(altura(y.left), altura(y.right))
    
    return y

def insertar_avl(raiz, frecuencia, nombre):
    if not raiz:
        return AVLNode(frecuencia, nombre)
    
    if frecuencia < raiz.frecuencia:
        raiz.left = insertar_avl(raiz.left, frecuencia, nombre)
    else:
        raiz.right = insertar_avl(raiz.right, frecuencia, nombre)
    
    raiz.height = 1 + max(altura(raiz.left), altura(raiz.right))
    
    balance = balance_factor(raiz)
    
    # Casos de desbalance
    # Left-Left
    if balance > 1 and frecuencia < raiz.left.frecuencia:
        return rotacion_derecha(raiz)
    # Right-Right
    if balance < -1 and frecuencia >= raiz.right.frecuencia:
        return rotacion_izquierda(raiz)
    # Left-Right
    if balance > 1 and frecuencia >= raiz.left.frecuencia:
        raiz.left = rotacion_izquierda(raiz.left)
        return rotacion_derecha(raiz)
    # Right-Left
    if balance < -1 and frecuencia < raiz.right.frecuencia:
        raiz.right = rotacion_derecha(raiz.right)
        return rotacion_izquierda(raiz)
    
    return raiz

def altura(nodo):
    return nodo.height if nodo else 0

def actualizar_altura(nodo):
    nodo.height = 1 + max(altura(nodo.left), altura(nodo.right))

def escala_grafo(escala_notas, diccionario):
    grafo = {}
    for i in range(len(escala_notas)-1):
        nota_actual = diccionario[escala_notas[i]][0]
        nota_siguiente = diccionario[escala_notas[i+1]][0]
        grafo.setdefault(nota_actual, []).append(nota_siguiente)
    return grafo


class HashScale:
    """
    Implementación sencilla de una tabla hash con encadenamiento.
    Las llaves serán frecuencias (float) y los valores, nombres de las notas (str).
    """

    def __init__(self, size=16):
        # Cantidad de buckets (lista de listas)
        self.size = size
        self.buckets = [[] for _ in range(size)]
        self.count = 0  # Para llevar seguimiento de cuántos elementos tenemos

    def _hash(self, key):
        """
        Devuelve un índice en el rango [0, self.size)
        a partir del hash de la llave.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Inserta un par (key, value) en la tabla hash.
        Si la llave ya existe, se sobreescribe el valor.
        """
        index = self._hash(key)
        bucket = self.buckets[index]

        # Buscar si la llave ya existe
        for i, (k, v) in enumerate(bucket):
            if k == key:
                # Reemplaza el valor y termina
                bucket[i] = (key, value)
                return
        
        # Si la llave no existe, insertar un nuevo par
        bucket.append((key, value))
        self.count += 1

        # (Opcional) Comprobar factor de carga para rehash
        if self.count / self.size > 0.75:
            self._rehash()

    def get(self, key):
        """
        Retorna el valor asociado a la llave, o None si no existe.
        """
        index = self._hash(key)
        bucket = self.buckets[index]

        for (k, v) in bucket:
            if k == key:
                return v
        return None

    def delete(self, key):
        """
        Elimina la llave de la tabla si existe. Retorna True si elimina, False si no la encuentra.
        """
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.count -= 1
                return True
        return False

    def items(self):
        """
        Generador que retorna todos los pares (key, value) en la tabla.
        """
        for bucket in self.buckets:
            for (k, v) in bucket:
                yield (k, v)

    def _rehash(self):
        """
        Duplica el tamaño de la tabla y reubica todos los elementos.
        """
        old_buckets = self.buckets
        self.size *= 2
        self.buckets = [[] for _ in range(self.size)]
        self.count = 0  # Se reinicia y se recalculará en insert

        for bucket in old_buckets:
            for (k, v) in bucket:
                self.insert(k, v)
