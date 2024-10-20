import pandas as pd
import networkx as nx
from collections import deque

# Load node coordinates and path details
node_data = pd.read_csv('C:/Users/rlnar/Desktop/VSCODE/CIA-1/DATA/node_positions.csv')
edge_data = pd.read_csv('C:/Users/rlnar/Desktop/VSCODE/CIA-1/DATA/path_details.csv')
network_graph = nx.Graph()

# Add nodes to the graph
for _, node_row in node_data.iterrows():
    network_graph.add_node(node_row['Node'], coordinates=(node_row['X'], node_row['Y']))

# Define bidirectional edges with weights
for _, edge_row in edge_data.iterrows():
    network_graph.add_edge(edge_row['Source Node'], edge_row['Target Node'], weight=edge_row['Weight'])
    network_graph.add_edge(edge_row['Target Node'], edge_row['Source Node'], weight=edge_row['Weight'])

# British Museum Search Algorithm
def exhaustive_search(graph, start, goal):
    explored_nodes = set()
    search_queue = deque([(start, [start], 0)])  # Queue stores (current_node, path_taken, cumulative_cost)
    cumulative_cost = 0
    operation_log = []
    optimal_path = None

    print("============================ OPERATIONS LOG ============================")

    while search_queue:
        current_node, current_path, current_cost = search_queue.popleft()

        if current_node not in explored_nodes:
            explored_nodes.add(current_node)

            if current_node == goal:
                optimal_path = current_path
                cumulative_cost = current_cost
                break

            # Explore neighbors
            for neighbor in graph.neighbors(current_node):
                edge_weight = graph[current_node][neighbor]['weight']
                new_total_cost = current_cost + edge_weight
                extended_path = current_path + [neighbor]
                search_queue.append((neighbor, extended_path, new_total_cost))
                operation_log.append(f"Exploration: ||{current_node}||---{edge_weight:.2f}--->||{neighbor}||")

    # Output results
    if optimal_path:
        print("\n".join(operation_log))
        print("====================================================================================")
        print(f"\nOptimal Path: {' -> '.join(map(str, optimal_path))}")
        print("====================================================================================")
        print(f"Total Cost: {cumulative_cost:.2f}")
        print("====================================================================================")
    else:
        print(f"Goal Node ({goal}) not reached.")
        print("====================================================================================")

    formatted_explored_nodes = [int(node) for node in explored_nodes]
    print(f"All Explored Nodes: {formatted_explored_nodes}")
    print("====================================================================================")
    return formatted_explored_nodes

# Define start and goal nodes
starting_node = 1  # Starting node
destination_node = 5  # Target node
visited_nodes = exhaustive_search(network_graph, starting_node, destination_node)