# Implementación de Árboles Binarios en Python usando listas

# Cada nodo se representa como: [valor, hijo_izquierdo, hijo_derecho]

def crear_arbol(valor):
    # Crea un nuevo nodo raíz con el valor dado y sin hijos
    return [valor, [], []]

def insertar_izquierda(nodo, nuevo_valor):
    # Inserta un nuevo nodo como hijo izquierdo del nodo actual
    subarbol_izq = nodo[1]
    if subarbol_izq:
        # Si ya hay un hijo izquierdo, lo convierte en hijo del nuevo nodo
        nodo[1] = [nuevo_valor, subarbol_izq, []]
    else:
        # Si no hay hijo izquierdo, lo agrega directamente
        nodo[1] = [nuevo_valor, [], []]

def insertar_derecha(nodo, nuevo_valor):
    # Inserta un nuevo nodo como hijo derecho del nodo actual
    subarbol_der = nodo[2]
    if subarbol_der:
        # Si ya hay un hijo derecho, lo convierte en hijo del nuevo nodo
        nodo[2] = [nuevo_valor, [], subarbol_der]
    else:
        # Si no hay hijo derecho, lo agrega directamente
        nodo[2] = [nuevo_valor, [], []]

def preorden(arbol):
    # Recorre el árbol en orden: raíz → izquierda → derecha
    if arbol:
        print(arbol[0], end=' ')         # Imprime la raíz
        preorden(arbol[1])               # Recorre el subárbol izquierdo
        preorden(arbol[2])               # Recorre el subárbol derecho

def inorden(arbol):
    # Recorre el árbol en orden: izquierda → raíz → derecha
    if arbol:
        inorden(arbol[1])                # Recorre el subárbol izquierdo
        print(arbol[0], end=' ')         # Imprime la raíz
        inorden(arbol[2])                # Recorre el subárbol derecho

def postorden(arbol):
    # Recorre el árbol en orden: izquierda → derecha → raíz
    if arbol:
        postorden(arbol[1])              # Recorre el subárbol izquierdo
        postorden(arbol[2])              # Recorre el subárbol derecho
        print(arbol[0], end=' ')         # Imprime la raíz

def imprimir_arbol(arbol, nivel=0):
    # Imprime el árbol rotado 90°, para verlo jerárquicamente en consola
    if arbol:
        imprimir_arbol(arbol[2], nivel + 1)           # Imprime primero el subárbol derecho (arriba)
        print('   ' * nivel + str(arbol[0]))          # Imprime el nodo con indentación según el nivel
        imprimir_arbol(arbol[1], nivel + 1)           # Imprime el subárbol izquierdo (abajo)

# -----------------------
# Ejemplo de uso
# -----------------------

if __name__ == '__main__':
    # Crear el árbol con la raíz 'A'
    arbol = crear_arbol('A')

    # Insertar hijos izquierdo y derecho de 'A'
    insertar_izquierda(arbol, 'B')
    insertar_derecha(arbol, 'C')

    # Insertar hijos de 'B'
    insertar_izquierda(arbol[1], 'D')
    insertar_derecha(arbol[1], 'E')

    # Insertar hijos de 'C'
    insertar_izquierda(arbol[2], 'F')
    insertar_derecha(arbol[2], 'G')

    # Mostrar el árbol rotado (C a la derecha, B a la izquierda)
    print("Árbol visualizado (rotado 90°):")
    imprimir_arbol(arbol)

    # Realizar los tres tipos de recorrido
    print("\nRecorrido Preorden:")
    preorden(arbol)  # A B D E C F G

    print("\nRecorrido Inorden:")
    inorden(arbol)   # D B E A F C G

    print("\nRecorrido Postorden:")
    postorden(arbol) # D E B F G C A
