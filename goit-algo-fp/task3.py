""" Реалізація алгоритм Дейкстри для пошуку найкоротших шляхів в графі"""


import heapq


# Клас для представлення графа (список вершин, список ребер та відстані між вершинами)
class Graph:
    """ Клас для представлення графа (список вершин, список ребер та відстані між вершинами) """
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)
        self.edges[value] = []

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)  # Якщо граф неорієнтований
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance  # Якщо граф неорієнтований


# Алгоритм Дейкстри (пошук найкоротших шляхів в графі)
def dijkstra(graph, start):
    """ Функція для пошуку найкоротших шляхів в графі 
    :param graph: граф (об'єкт класу Graph)
    :param start: початкова вершина
    :return: словник найкоротших шляхів та словник попередніх вершин
    """  
    # Ініціалізація
    queue = []
    heapq.heappush(queue, (0, start))
    shortest_paths = {node: float('inf') for node in graph.nodes}
    shortest_paths[start] = 0
    previous_nodes = {node: None for node in graph.nodes}

    while queue:
        (current_distance, current_node) = heapq.heappop(queue)

        for neighbor in graph.edges[current_node]:
            distance = graph.distances[(current_node, neighbor)]
            new_distance = current_distance + distance

            if new_distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = new_distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (new_distance, neighbor))

    return shortest_paths, previous_nodes

# Функція для відтворення шляху від початкової вершини до заданої
def reconstruct_path(previous_nodes, start, end):
    """ Функція для відтворення шляху від початкової вершини до заданої
    :param previous_nodes: словник попередніх вершин
    :param start: початкова вершина
    :param end: кінцева вершина
    :return: список вершин шляху
    """
    path = []
    current_node = end
    while current_node != start:
        path.insert(0, current_node)
        current_node = previous_nodes[current_node]
    path.insert(0, start)
    return path

# Приклад використання
if __name__ == "__main__":
    graph = Graph()

    # Додавання вершин
    nodes = ['A', 'B', 'C', 'D', 'E', 'F']
    for node in nodes:
        graph.add_node(node)

    # Додавання ребер з вагами (відстанями між вершинами)
    graph.add_edge('A', 'B', 7)
    graph.add_edge('A', 'C', 9)
    graph.add_edge('A', 'F', 14)
    graph.add_edge('B', 'C', 10)
    graph.add_edge('B', 'D', 15)
    graph.add_edge('C', 'D', 11)
    graph.add_edge('C', 'F', 2)
    graph.add_edge('D', 'E', 6)
    graph.add_edge('E', 'F', 9)

    # Знаходження найкоротших шляхів від початкової вершини 'A'
    start_node = 'A'
    shortest_paths, previous_nodes = dijkstra(graph, start_node)

    # Виведення результатів
    print(f"Найкоротші шляхи від вершини {start_node}:")
    for node in graph.nodes:
        print(f"До вершини {node}: {shortest_paths[node]} (Шлях: {reconstruct_path(previous_nodes, start_node, node)})")


""" Результат виконання:

Найкоротші шляхи від вершини A:
До вершини A: 0 (Шлях: ['A'])
До вершини F: 11 (Шлях: ['A', 'C', 'F'])     
До вершини D: 20 (Шлях: ['A', 'C', 'D'])     
До вершини C: 9 (Шлях: ['A', 'C'])
До вершини B: 7 (Шлях: ['A', 'B'])
До вершини E: 20 (Шлях: ['A', 'C', 'F', 'E'])
"""
