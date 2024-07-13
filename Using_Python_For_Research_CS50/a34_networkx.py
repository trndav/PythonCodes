import networkx as nx

# G = nx.Graph()
# G.add_node(1) # add single node

# G.add_nodes_from([2,3]) # Add multiple nodes names as list
# G.add_nodes_from(["Tim","Bob"]) 
# print("G is:", G)
# print("G.nodes is:", G.nodes())

# G.add_edge(1, 2)
# G.add_edge("Tim", "Bob")

# G.add_edges_from([(1,3), (1,4), (1,5), (1,6)])

# G.add_edge("A", "B")
# print("All edges G.edges()", G.edges())

# # Remove nodes:
# G.remove_node("Bob")
# print("All edges G.edges()", G.edges())

# G.remove_nodes_from([4, 5])
# print("All edges G.edges()", G.edges())

# #Remove edges
# G.remove_edge(1,3)
# print(G.edges())

# # Remove multiple edges
# G.remove_edges_from([(1,2), (1,6)])
# print("G.edges():", G.edges())

# print(G.number_of_nodes())
# print(G.number_of_edges())

# A = nx.Graph()
# A.add_nodes_from(1,2,3,4)
# A.add_edges_from((1,2),(3,4))
# print(A.number_of_nodes(), A.number_of_edges())


# Random graph generators
# Dataset karate club graph

G = nx.karate_club_graph()
import matplotlib.pyplot as plt

nx.draw(G, with_labels=True, node_color="lightblue", edge_color="gray")
#plt.savefig("karate_club_graph.pdf")
#plt.show()

# Degrees of nodes
print(G.degree())
print(G.degree()[33])
print(G.degree(0) is G.degree()[0])