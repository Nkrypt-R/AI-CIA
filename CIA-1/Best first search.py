import pandas as pd
import networkx as nx
import math
import heapq

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

# Heuristic generation using Euclidean distance
def calculate_heuristic(node, goal):
    node_position = network_graph.nodes[node]['coordinates']
    goal_position = network_graph.nodes[goal]['coordinates']
    return math.sqrt((node_position[0] - goal_position[0]) ** 2 + (node_position[1] - goal_position[1]) ** 2)

# Best First Search Algorithm
def best_first_search(graph, start, goal):
    explored_nodes = set()
    min_heap = []
    heapq.heappush(min_heap, (calculate_heuristic(start, goal), start, [start]))  # Push (heuristic, node, path)
    operation_log = []

    print("============================ OPERATIONS LOG ============================")

    while min_heap:
        heuristic_value, current_node, path = heapq.heappop(min_heap)

        if current_node in explored_nodes:
            continue

        explored_nodes.add(current_node)

        # If goal is reached, output the path and cost
        if current_node == goal:
            print("\n".join(operation_log))
            print("====================================================================================")
            print(f"\nOptimal Path: {' -> '.join(map(str, path))}")
            print("====================================================================================")
            total_cost = sum(graph[path[i]][path[i+1]]['weight'] for i in range(len(path) - 1))
            print(f"Total Cost: {total_cost:.2f}")
            print("====================================================================================")
            return [int(node) for node in explored_nodes]

        # Explore neighbors and add to the heap
        for neighbor in graph.neighbors(current_node):
            if neighbor not in explored_nodes:
                edge_weight = graph[current_node][neighbor]['weight']
                extended_path = path + [neighbor]
                heapq.heappush(min_heap, (calculate_heuristic(neighbor, goal), neighbor, extended_path))
                operation_log.append(f"Exploration: ||{current_node}||---{edge_weight:.2f}--->||{neighbor}||")

    # If goal not reached
    print(f"Goal Node ({goal}) not reached.")
    print("====================================================================================")

    formatted_explored_nodes = [int(node) for node in explored_nodes]
    print(f"All Explored Nodes: {formatted_explored_nodes}")
    print("====================================================================================")
    return formatted_explored_nodes


# Define the start, goal, and run the Best First Search algorithm
starting_node = 1  # Starting node
destination_node = 5  # Target node
visited_nodes = best_first_search(network_graph, starting_node, destination_node)