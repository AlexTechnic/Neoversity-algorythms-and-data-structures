""" Програма для візуалізації обходу бінарного дерева в глибину та в ширину, побудованого з бінарної купи. """


import uuid
import networkx as nx
import matplotlib.pyplot as plt
import heapq
import colorsys


class Node:
    """Клас для представлення вузла бінарного дерева."""
    def __init__(self, key):
        self.left = None  # Лівий дочірній вузол
        self.right = None  # Правий дочірній вузол
        self.val = key  # Значення вузла (ключ)
        self.color = "#000000"  # Початковий колір вузла - чорний
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """Рекурсивна функція для додавання вузлів і ребер до графа на основі бінарного дерева."""
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, title="Binary Tree"):
    """Функція для візуалізації дерева."""
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def color_gradient(steps, start_color=(0.0, 0.0, 0.3), end_color=(0.6, 1.0, 0.9)):
    """Генерує градієнт кольорів від темного до світлого відтінку."""
    gradient = []
    for i in range(steps):
        ratio = i / (steps - 1) if steps > 1 else 1
        hue = start_color[0] + ratio * (end_color[0] - start_color[0])
        saturation = start_color[1] + ratio * (end_color[1] - start_color[1])
        brightness = start_color[2] + ratio * (end_color[2] - start_color[2])
        rgb = colorsys.hsv_to_rgb(hue, saturation, brightness)
        hex_color = '#%02x%02x%02x' % (int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))
        gradient.append(hex_color)
    return gradient

def dfs(tree_root):
    """Алгоритм обходу дерева в глибину (DFS) з використанням стеку."""
    stack = [tree_root]  # Ініціалізуємо стек коренем дерева
    order = []  # Для збереження порядку обходу
    while stack:
        node = stack.pop()  # Отримуємо вузол зі стеку
        if node:
            order.append(node)
            stack.append(node.right)  # Додаємо правий дочірній вузол
            stack.append(node.left)  # Додаємо лівий дочірній вузол
    return order

def bfs(tree_root):
    """Алгоритм обходу дерева в ширину (BFS) з використанням черги."""
    queue = [tree_root]  # Ініціалізуємо чергу коренем дерева
    order = []  # Для збереження порядку обходу
    while queue:
        node = queue.pop(0)  # Отримуємо вузол із черги
        if node:
            order.append(node)
            queue.append(node.left)  # Додаємо лівий дочірній вузол
            queue.append(node.right)  # Додаємо правий дочірній вузол
    return order

def apply_colors(order):
    """Застосовує градієнт кольорів до вузлів дерева згідно порядку обходу."""
    colors = color_gradient(len(order))
    for i, node in enumerate(order):
        node.color = colors[i]  # Присвоюємо вузлу колір

def build_heap_tree(heap):
    """Функція для побудови дерева з масиву, що представляє бінарну купу."""
    nodes = [Node(val) for val in heap]
    for i in range(len(nodes) // 2):
        if 2 * i + 1 < len(nodes):
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < len(nodes):
            nodes[i].right = nodes[2 * i + 2]
    return nodes[0] if nodes else None

# Створюємо масив, що представляє бінарну купу
heap = [10, 7, 9, 5, 6, 8, 4]
heapq.heapify(heap)

# Побудова дерева з купи
heap_tree_root = build_heap_tree(heap)

# Візуалізація обходу в глибину (DFS)
dfs_order = dfs(heap_tree_root)
apply_colors(dfs_order)
draw_tree(heap_tree_root, title="DFS обхід")

# Візуалізація обходу в ширину (BFS)
bfs_order = bfs(heap_tree_root)
apply_colors(bfs_order)
draw_tree(heap_tree_root, title="BFS обхід")


""" В результаті виконання програми відобразиться спершу вікно з візуалізації обходу дерева в глибину (DFS), 
а потім вікно з візуалізації обходу дерева в ширину (BFS). 
Градієнт кольорів відтінків розподілений за вузлами дерева відповідно до порядку обходу (від темного до світлого).
"""
