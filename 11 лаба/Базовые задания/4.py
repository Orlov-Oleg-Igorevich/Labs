from networkx.algorithms import bipartite
import matplotlib.pyplot as plt
import networkx as nx
import pylab

B = nx.Graph()
B.add_nodes_from([1, 2, 3, 4], bipartite=0)
B.add_nodes_from(["a", "b", "c"], bipartite=1)
B.add_edges_from([(1, "a"), (1, "b"), (2, "b"), (2, "c"), (3, "c"), (4, "a")])

nx.draw(B,with_labels=True)

pylab.figure ()
plt.show()