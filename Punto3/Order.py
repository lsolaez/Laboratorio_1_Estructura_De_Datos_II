#clase que representa cada orden
class Order:
    def __init__(self, order_number, product_name, category, delivery_date):
        self.order_number = order_number
        self.product_name = product_name
        self.category = category
        self.delivery_date = delivery_date

#representa nuestro árbol B+ para organizar los pedidos según la fecha de entrega
class BPlusTree:
    def __init__(self, order):
        self.root = BPlusNode(order)
        self.order = order

    def insert(self, key, value):
        self.root.insert(key, value)

    def search(self, key):
        return self.root.search(key)

#representa un nodo del árbol B+. Cada nodo tiene un orden, que determina el número máximo de claves y valores que puede contener
class BPlusNode:
    def __init__(self, order, parent=None):
        self.keys = []
        self.values = []
        self.children = []
        self.order = order
        self.parent = parent


  
  # _insert_into_leaf, _find_index y _find_child_index se utilizan para insertar una nueva orden en una hoja del árbol.
    def is_leaf(self):
      #este método determina si un nodo es una hoja o no
        return len(self.children) == 0

    def insert(self, key, value):
        if self.is_leaf():
            self._insert_into_leaf(key, value)
        else:
            child_index = self._find_child_index(key)
            child = self.children[child_index]
            if child.is_full():
                self._split_child(child_index)
                if key > self.keys[child_index]:
                    child_index += 1
                    child = self.children[child_index]
            child.insert(key, value)
 
    def search(self, key):
        if self.is_leaf():
            for i in range(len(self.keys)):
                if self.keys[i] == key:
                    return self.values[i]
            return None
        else:
            child_index = self._find_child_index(key)
            child = self.children[child_index]
            return child.search(key)

    def _insert_into_leaf(self, key, value):
        index = self._find_index(key)
        self.keys.insert(index, key)
        self.values.insert(index, value)

    def _find_index(self, key):
        for i in range(len(self.keys)):
            if self.keys[i] > key:
                return i
        return len(self.keys)

    def _find_child_index(self, key):
        for i in range(len(self.keys)):
            if self.keys[i] > key:
                return i
        return len(self.children)

    #determina si un nodo está lleno
    def is_full(self):
        return len(self.keys) == self.order - 1

 #se utiliza para dividir un nodo en dos cuando se alcanza su capacidad máxima
    def _split_child(self, child_index):
        left_child = self.children[child_index]
        right_child = BPlusNode(self.order, parent=self)
        mid = left_child.order // 2
        right_child.keys = left_child.keys[mid:]
        right_child.values = left_child.values[mid:]
        left_child.keys = left_child.keys[:mid]
        left_child.values = left_child.values[:mid]
        if not left_child.is_leaf():
            right_child.children = left_child.children[mid:]
            left_child.children = left_child.children[:mid]
            for child in right_child.children:
                child.parent = right_child
        self.keys.insert(child_index, right_child.keys[0])