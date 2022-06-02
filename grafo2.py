import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()  # nuevo grafo

G.add_weighted_edges_from(
    [
        (0, 1, 16),
        (0, 2, 86),
        (0, 3, 34),
        (0, 5, 11),
        (0, 7, 21),
        (0, 8, 21),
        (0, 10, 29),
        (1, 3, 19),
        (1, 4, 36),
        (1, 6, 61),
        (1, 7, 60),
        (1, 8, 82),
        (1, 9, 74),

        (2, 3, 96),
        (2, 4, 91),
        (2, 5, 70),
        (2, 7, 88),
        (2, 8, 59),
        (2, 9,19 ),
        (2, 10, 16),
        
        (3, 5, 32),
        (3, 6, 36),
        (3, 7, 64),
        (3, 8, 55),
        (3, 9, 74),
        (4, 10, 96),
        (5, 4, 1.0),
    ]
)
H = nx.get_edge_attributes(G, "weight")  # Devuelve un diccionario con los valores


# subax1 = plt.subplot(121)
nx.draw(G, with_labels=True, font_weight="bold")
subax2 = plt.subplot(111)
nx.draw_shell(G, nlist=[range(0, 11), range(5)], with_labels=True, font_weight="bold")
plt.show()
