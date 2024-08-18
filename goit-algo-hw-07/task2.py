""" Додавання алгоритму пошуку найменшого значення у двійковому дереві пошуку (BST) """

# Вузол двійкового дерева пошуку (Binary Search Tree)
class Node:
    """ Клас для представлення вузла BST дерева
    :param key: ключ вузла дерева
    :param left: лівий нащадок вузла
    :param right: правий нащадок вузла 
    """
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        """ Метод для представлення дерева у вигляді рядка для візуалізації """
        # Базовий відступ для рівнів дерева
        ret = " " * (level * 4) + prefix + str(self.val) + "\n"
        # Відображення лівого нащадка (якщо є)
        if self.left:
            ret += self.left.__str__(level + 1, "|---L: ")
        else:
            ret += " " * (level + 1) * 4 + "|---L: None\n"
        # Відображення правого нащадка (якщо є)
        if self.right:
            ret += self.right.__str__(level + 1, "|---R: ")
        else:
            ret += " " * (level + 1) * 4 + "|---R: None\n"
        return ret

# Вставка нового ключа в дерево
def insert(root, key):
    """ Вставка нового ключа у BST дерево
    :param root: корінь дерева 
    :param key: ключ для вставки у дерево
    """
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

# Функція для пошуку найбільшого значення у двійковому дереві пошуку
def find_max_in_bst(root):
    """ Пошук найбільшого значення у BST дереві
    :param root: корінь дерева 
    :return: найбільше значення у дереві 
    """
    current = root
    while current.right:
        current = current.right
    return current.val

# Функція для пошуку найменшого значення у двійковому дереві пошуку
def find_min_in_bst(root):
    """ Пошук найменшого значення у BST дереві
    :param root: корінь дерева 
    :return: найменше значення у дереві 
    """
    current = root
    while current.left:
        current = current.left
    return current.val

# Тестування алгоритму пошуку найменшого значення
root_bst = None
keys_bst = [20, 8, 22, 4, 12, 10, 14]

for key in keys_bst:
    root_bst = insert(root_bst, key)

print("Двійкове дерево пошуку (BST):\n")
print(root_bst)

min_value_bst = find_min_in_bst(root_bst)
print("Найменше значення у двійковому дереві пошуку:", min_value_bst)

""" Результат:

Двійкове дерево пошуку (BST):

Root: 20
    |---L: 8
        |---L: 4       
            |---L: None
            |---R: None
        |---R: 12      
            |---L: 10  
                |---L: None
                |---R: None
            |---R: 14
                |---L: None
                |---R: None
    |---R: 22
        |---L: None
        |---R: None

Найменше значення у двійковому дереві пошуку: 4
"""