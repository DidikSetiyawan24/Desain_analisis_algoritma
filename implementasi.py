import random
import time
from typing import Optional, List

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root: Optional[Node], key: int) -> Node:
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def delete(self, root: Optional[Node], key: int) -> Optional[Node]:
        if not root:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp_val = self.min_value_node(root.right)
            root.key = temp_val.key
            root.right = self.delete(root.right, temp_val.key)
        return root

    def min_value_node(self, node: Node) -> Node:
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, root: Optional[Node], key: int) -> bool:
        if not root:
            return False
        if key == root.key:
            return True
        elif key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

class AVLTree(BST):
    def insert(self, root: Optional[Node], key: int) -> Node:
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root

    def delete(self, root: Optional[Node], key: int) -> Optional[Node]:
        root = super().delete(root, key)
        if not root:
            return root
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root

    def left_rotate(self, z: Node) -> Node:
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z: Node) -> Node:
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def get_height(self, root: Optional[Node]) -> int:
        if not root:
            return 0
        return root.height

    def get_balance(self, root: Optional[Node]) -> int:
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

def generate_data(n: int) -> List[int]:
    random.seed(230403010045)
    return random.sample(range(1000000, 9999999), n)


# Experiment function
def run_experiment(tree_class, data: List[int]) -> dict:
    tree = tree_class()
    root = None

    start_time = time.time()
    for key in data:
        root = tree.insert(root, key)
    insert_time = time.time() - start_time

    search_keys = random.sample(data, 100)
    start_time = time.time()
    for key in search_keys:
        tree.search(root, key)
    search_time = time.time() - start_time

    delete_keys = random.sample(data, 100)
    start_time = time.time()
    for key in delete_keys:
        root = tree.delete(root, key)
    delete_time = time.time() - start_time

    return {
        "insert_time": insert_time,
        "search_time": search_time,
        "delete_time": delete_time
    }

data_1000 = generate_data(1000)
bst_result = run_experiment(BST, data_1000)
avl_result = run_experiment(AVLTree, data_1000)

bst_result, avl_result
print("BST Result:", bst_result)
print("AVL Result:", avl_result)


