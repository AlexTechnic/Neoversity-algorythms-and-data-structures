import networkx as nx
import matplotlib.pyplot as plt

# Список вершин (місць) графу які відображають місця відвідування жителя зі спального району Виноградар
places = ["Хата", "Ларьок", "Робота", "Парк", "Метро", "ТЦК"]
G = nx.Graph()
G.add_nodes_from(places)

# Додавання ребер (шляхів)
edges = [
    ("Хата", "Ларьок"),
    ("Хата", "Метро"),
    ("Хата", "Парк"),
    ("Ларьок", "Метро"),
    ("Ларьок", "Парк"),
    ("Метро", "Робота"),
    ("ТЦК", "Метро"),
    ("ТЦК", "Ларьок"),
    ("ТЦК", "Парк"),
]

G.add_edges_from(edges)

# Візуалізація графу за допомогою бібліотеки matplotlib та networkx
pos = nx.spring_layout(G)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="lightcoral",
    node_size=2500,
    edge_color="gray",
    font_size=12,
    font_color="black",
)

plt.title("Найбільш відвідувані місця жителя зі спального району Виноградар")
plt.show()

# Аналіз характеристик графу
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_centrality = nx.degree_centrality(G)

# Виведення результатів аналізу 
print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступінь вершин:")
for node, degree in degree_centrality.items():
    print(f"{node}: {degree:.2f}")

"""
Результат:

Кількість вершин: 6
Кількість ребер: 9
Ступінь вершин:   
Хата: 0.60
Ларьок: 0.80
Робота: 0.20
Парк: 0.60
Метро: 0.80
ТЦК: 0.60
"""