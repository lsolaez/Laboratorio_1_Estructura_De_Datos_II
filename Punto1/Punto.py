class Node:
    def __init__(self, user_id):
        self.user_id = user_id
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, user_id):
        self.root = self._insert(self.root, user_id)

    def _insert(self, node, user_id):
        if not node:
            return Node(user_id)

        if user_id < node.user_id:
            node.left = self._insert(node.left, user_id)
        else:
            node.right = self._insert(node.right, user_id)

        node.height = 1 + max(self._height(node.left), self._height(node.right))

        balance = self._get_balance(node)

        if balance > 1 and user_id < node.left.user_id:
            return self._rotate_right(node)

        if balance < -1 and user_id > node.right.user_id:
            return self._rotate_left(node)

        if balance > 1 and user_id > node.left.user_id:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1 and user_id < node.right.user_id:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def search(self, user_id):
        return self._search(self.root, user_id)

    def _search(self, node, user_id):
        if not node:
            return False

        if node.user_id == user_id:
            return True

        if user_id < node.user_id:
            return self._search(node.left, user_id)

        return self._search(node.right, user_id)

    def delete(self, user_id):
        self.root = self._delete(self.root, user_id)

    def _delete(self, node, user_id):
        if not node:
            return node

        if user_id < node.user_id:
            node.left = self._delete(node.left, user_id)
        elif user_id > node.user_id:
            node.right = self._delete(node.right, user_id)
        else:
            if not node.left:
                temp = node.right
                node = None
                return temp

            elif not node.right:
                temp = node.left
                node = None
                return temp

            temp = self._get_min_value_node(node.right)
            node.user_id = temp.user_id
            node.right = self._delete(node.right, temp.user_id)

        if not node:
            return node

        node.height = 1 + max(self._height(node.left), self._height(node.right))

        balance = self._get_balance(node)

        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._rotate_right(node)

        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._rotate_left(node)

        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _height(self, node):
        if not node:
            return 0

        return node.height

    def _get_balance(self, node):
        if not node:
            return 0

        return self._height(node.left) - self._height(node.right)

    def _rotate_right(self, node):
        left_child = node.left
        node.left = left_child.right
        left_child.right = node

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        left_child.height = 1 + max(self._height(left_child.left), self._height(left_child.right))

        return left_child

    def _rotate_left(self, node):
        right_child = node.right
        node.right = right_child.left
        right_child.left = node

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        right_child.height = 1 + max(self._height(right_child.left), self._height(right_child.right))

        return right_child

    def _get_min_value_node(self, node):
        if not node or not node.left:
            return node

        return self._get_min_value_node(node.left)

    def level_order_traversal(self):
        if not self.root:
            return []

        result = []
        height = self.get_height(self.root)

        for i in range(1, height + 1):
            level = []
            self._level_order_traversal(self.root, i, level)
            result.append(level)

        return result

    def _level_order_traversal(self, node, level, level_list):
        if not node:
            return

        if level == 1:
            level_list.append(node.user_id)
        elif level > 1:
            self._level_order_traversal(node.left, level - 1, level_list)
            self._level_order_traversal(node.right, level - 1, level_list)

    def get_height(self, node):
        if not node:
            return 0

        return max(self.get_height(node.left), self.get_height(node.right)) + 1
    
    def get_node_height(self, user_id):
        node = self.search(user_id)
        if node is not None and isinstance(node, Node):  # Agrega esta comprobación
            return node.height
        else:
            return None



