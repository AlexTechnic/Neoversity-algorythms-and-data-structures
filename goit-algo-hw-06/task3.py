import networkx as nx
from collections import deque
import heapq

G = nx.Graph()

# Додавання вершин
places = ["Хата", "Ларьок", "Робота", "Парк", "Метро", "ТЦК"]
G.add_nodes_from(places)

# Додавання ребер з вагами для кожного ребра щоб потім знайти найкоротший шлях за допомогою алгоритму Дейкстри
edges_with_weights = [
    ("Хата", "Ларьок", 1),
    ("Хата", "Метро", 1),
    ("Хата", "Парк", 1),
    ("Ларьок", "Метро", 1),
    ("Ларьок", "Парк", 1),
    ("Метро", "Робота", 1),
    ("ТЦК", "Метро", 1),
    ("ТЦК", "Ларьок", 1),
    ("ТЦК", "Парк", 1),
]

G.add_weighted_edges_from(edges_with_weights)

# Реалізація алгоритму DFS (Depth-First Search, пошук в глибину)
def dfs(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


# Реалізація алгоритму BFS (Breadth-First Search, пошук в ширину)
def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    while queue:
        (vertex, path) = queue.popleft()
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


# Знаходження всіх шляхів між "Хата" і "Робота" за допомогою DFS
dfs_paths = list(dfs(G, "Хата", "Робота"))

# Знаходження всіх шляхів між "Хата" і "Робота" за допомогою BFS
bfs_paths = list(bfs(G, "Хата", "Робота"))


# Виведення результатів
print("Шляхи від Хата до Робота за допомогою DFS:")
for path in dfs_paths:
    print(path)

print("\nШляхи від Хата до Робота за допомогою BFS:")
for path in bfs_paths:
    print(path)

# Реалізація алгоритму Дейкстри для знаходження найкоротшого шляху, використовуючи бібліотеку heapq (heap queue)
def dijkstra(graph, start):
    """ Знаходження найкоротших шляхів від початкової вершини до всіх інших вершин графа
    :param graph: граф у форматі словника
    :param start: початкова вершина
    :return: відстані та найкоротші шляхи до кожної вершини
    """
    queue = []
    heapq.heappush(queue, (0, start))
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    shortest_path = {}

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight['weight']

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
                shortest_path[neighbor] = current_vertex

    return distances, shortest_path


# Знаходження найкоротших шляхів від кожної вершини до всіх інших
shortest_paths = {}
for place in places:
    distances, _ = dijkstra(G, place)
    shortest_paths[place] = distances

# Виведення результатів
print("Найкоротші шляхи між усіма вершинами графа:")
for start, paths in shortest_paths.items():
    print(f"\nВід {start}:")
    for destination, distance in paths.items():
        print(f"  до {destination}: {distance}")

"""
Результат:

Найкоротші шляхи між усіма вершинами графа:

Від Хата:
  до Хата: 0
  до Ларьок: 1
  до Робота: 2
  до Парк: 1
  до Метро: 1
  до ТЦК: 2

Від Ларьок:
  до Хата: 1
  до Ларьок: 0
  до Робота: 2
  до Парк: 1
  до Метро: 1
  до ТЦК: 1

Від Робота:
  до Хата: 2
  до Ларьок: 2
  до Робота: 0
  до Парк: 3
  до Метро: 1
  до ТЦК: 2

Від Парк:
  до Хата: 1
  до Ларьок: 1
  до Робота: 3
  до Парк: 0
  до Метро: 2
  до ТЦК: 1

Від Метро:
  до Хата: 1
  до Ларьок: 1
  до Робота: 1
  до Парк: 2
  до Метро: 0
  до ТЦК: 1

Від ТЦК:
  до Хата: 2
  до Ларьок: 1
  до Робота: 2
  до Парк: 1
  до Метро: 1
  до ТЦК: 0

Результат відображає найкоротші шляхи між вершинами в графі, 
де всі ваги ребер встановлені рівними (вага = 1). 
Це призвело до того, що всі шляхи між вершинами мають довжину, яка відповідає кількості ребер між ними."""