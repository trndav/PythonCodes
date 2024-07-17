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

# G = nx.karate_club_graph()
import matplotlib.pyplot as plt

# nx.draw(G, with_labels=True, node_color="lightblue", edge_color="gray")
#plt.savefig("karate_club_graph.pdf")
#plt.show()

# Degrees of nodes
# print(G.degree())
# print(G.degree()[33])
# print(G.degree(0) is G.degree()[0])


# Random graph Erdős-Rényi
# build ER model
from scipy.stats import bernoulli
# bernoulli.rvs(p=0.2) #p-probability

# N = 20
# p = 0.2
# # create empty graph
# # add all N nodes in graph
# # loop over all pairs of nodes
#     # add an edge with probability p
# G = nx.Graph()
# G.add_nodes_from(range(N))
# for node1 in G.nodes():
#     for node2 in G.nodes():
#         if node1 < node2 and bernoulli.rvs(p=p): # == True:
#             G.add_edge(node1, node2)

# print(G.number_of_nodes())

# # Draw above graph
# nx.draw(G)
# plt.show()

# Turn to a function
def er_graph(N, p):
    '''Generate ER graph.
    '''
    G = nx.Graph()
    G.add_nodes_from(range(N))
    for node1 in G.nodes():
        for node2 in G.nodes():
            if node1 < node2 and bernoulli.rvs(p=p): # == True:
                G.add_edge(node1, node2)
    return G

#nx.draw(er_graph(10, 0), node_size=30, node_color="gray")
# plt.savefig("erdos_renyi_graph.pdf")
# plt.show()



def plot_degree_distribution(G):
    degrees = [d for n, d in G.degree()]
    plt.hist(degrees, histtype="step")
    plt.xlabel("Degree")
    plt.ylabel("P")
    plt.title("Degree distribution")

# # G = er_graph(500, 0.08)
# # plot_degree_distribution(G)
# # plt.savefig("hist1_plot_degree_distribution.pdf")
# # plt.show()

# G1 = er_graph(500, 0.08)
# plot_degree_distribution(G1)
# G2 = er_graph(500, 0.08)
# plot_degree_distribution(G2)
# G3 = er_graph(500, 0.08)
# plot_degree_distribution(G3)
# plt.savefig("hist2_plot_degree_distribution.pdf")
# plt.show()



# adjacency matrix
import numpy as np

A1 = np.loadtxt("adj_allVillageRelationships_vilno_1.csv", delimiter=",")
A2 = np.loadtxt("adj_allVillageRelationships_vilno_2.csv", delimiter=",")

G1 = nx.to_networkx_graph(A1)
G2 = nx.to_networkx_graph(A2)

def basic_net_stats(G):
    print("G.number_of_nodes()", G.number_of_nodes())
    print("G.number_of_edges()", G.number_of_edges())
    #print("Average degree", np.mean(list(G.degree().values())))

# basic_net_stats(G1)
# basic_net_stats(G2)
# plot_degree_distribution(G1)
# plot_degree_distribution(G2)
# plt.savefig("village.hist.pdf")
# plt.show()




# Finding the Largest Connected Component
gen = nx.connected_components(G1) #connected_component_subgraphs(G1) # use nx.connected_components
g = gen.__next__() # generates component
print(type(g))

subgraphs = [G1.subgraph(component).copy() for component in gen]

# Primer kako da radite sa podgrafovima
for subgraph in subgraphs:
    print(type(subgraph))  # Ovo će biti <class 'networkx.classes.graph.Graph'>
    print(subgraph.number_of_nodes())
    print(subgraph.nodes())
    print(subgraph.edges())

print(len(G1))

G1_LCC_nodes = max(nx.connected_components(G1), key=len)
G2_LCC_nodes = max(nx.connected_components(G2), key=len)

G1_LCC = G1.subgraph(G1_LCC_nodes).copy()
G2_LCC = G2.subgraph(G2_LCC_nodes).copy()

print(len(G1_LCC))
print(len(G2_LCC))

plt.figure()
nx.draw(G1_LCC, node_color="red", edge_color="gray", node_size=20)
plt.savefig("village1.pdf")
plt.show()

