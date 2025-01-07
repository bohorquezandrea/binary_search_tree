
# Creacion del primer nodo 

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None 
        self.right = None 

# Creacion del arbol binario de busqueda
# Se empieza por la raiz 

class BST: 
    def __init__(self):
        self.root = None 

# Para insertar un nodo 

    def insert(self, key, value):
        if self.root is None: 
            self.root = Node(key, value)
        else: 
            self._insert(self.root, key, value)
    
    def _insert(self, current, key, value):
        if key < current.key:
            if current.left is None: 
                current.left = Node(key, value)
            else: 
                self._insert(current.left, key, value)
        elif key > current.key: 
            if current.right is None:
                current.right = Node(key, value)
            else: 
                self._insert(current.right, key, value)
        else:
            raise ValueError("Duplicate keys are not allowed")

# Funcion de busqueda 
 
    def search(self, key):
        return self._search(self.root, key)
    
    def _search(self, current, key):
        if current is None: 
            return None
        if key == current.key:
            return current.value
        elif key < current.key:
            return self._search(current.left, key)
        else: 
            return self._search(current.right, key)
        
#  Aca un print pero no hace falta 

    def print_tree(self):
        # Prints the tree structure in an in-order transversal 
        if self.root is None: 
            print("El arbol esta vacio")
        else: 
            print("Estado actual del arbol (in-order);")
            self._print_in_order(self.root)
    
    def _print_in_order(self, current):
        if current is not None: 
            self._print_in_order(current.left)
            print(f"Clave: {current.key}, Valor: {current.value}")
            self._print_in_order(current.right)

#  Demostracion del BST con impresion 
bst = BST()
bst.insert(10, "Producto A")
bst.insert(20, "Producto B")
bst.insert(5, "Producto C")
bst.insert(15, "Producto D")

# Imprimir el estado del arbol
bst.print_tree()

# Buscar nodos 
print("Buscar clave 10:", bst.search(10)) #Output: Producto A
print("Buscar clave 15:", bst.search(15)) #Output: Producto D 
print("Buscar clave 30:", bst.search(30)) #Output: None 
