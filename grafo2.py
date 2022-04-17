import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()  # nuevo grafo

G.add_weighted_edges_from(
    [
        (1, 2, 0.5),
        (3, 1, 0.75),
        (4, 1, 0.75),
        (2, 3, 2.0),
        (2, 4, 3.0),
        (3, 4, 1.0),
        # undirected graph
        (2, 1, 0.5),
        (1, 3, 0.75),
        (1, 4, 0.75),
        (3, 2, 2.0),
        (4, 2, 3.0),
        (4, 3, 1.0),
    ]
)
H = nx.get_edge_attributes(G, "weight")  # Devuelve un diccionario con los valores
print(H[(1, 2)])

# subax1 = plt.subplot(121)
nx.draw(G, with_labels=True, font_weight="bold")
subax2 = plt.subplot(111)
nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight="bold")
plt.show()
