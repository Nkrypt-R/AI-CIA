import pandas as pd
import networkx as nx
from collections import deque

# Load node coordinates and path details
node_df = pd.read_csv('C:/Users/rlnar/Desktop/VSCODE/CIA-1/DATA/node_positions.csv')
edge_df = pd.read_csv('C:/Users/rlnar/Desktop/VSCODE/CIA-1/DATA/path_details.csv')
graph_structure = nx.Graph()

# Add nodes with coordinates to the graph
for _, node_data in node_df.iterrows():
    graph_structure.add_node(node_data['Node'], coordinates=(node_data['X'], node_data['Y']))

# Define bidirectional edges with weights
for _, edge_data in edge_df.iterrows():
    graph_structure.add_edge(edge_data['Source Node'], edge_data['Target Node'], weight=edge_data['Weight'])
    graph_structure.add_edge(edge_data['Target Node'], edge_data['Source Node'], weight=edge_data['Weight'])

# Breadth-First Search (BFS) Algorithm
def bfs_with_cost(graph, start, goal):
    explored = set()
    search_queue = deque([(start, [start], 0)])  # Queue stores (current_node, path, current_cost)
    final_cost = 0
    operation_log = []
    optimal_path = None

    print("============================ OPERATIONS LOG ============================")

    while search_queue:
        current_node, current_path, current_cost = search_queue.popleft()

        if current_node not in explored:
            explored.add(current_node)

            if current_node == goal:
                optimal_path = current_path
                final_cost = current_cost
                break

            # Traverse through neighbors
            for neighbor in graph.neighbors(current_node):
                if neighbor not in explored:  # Avoid revisiting explored nodes
                    edge_weight = graph[current_node][neighbor]['weight']
                    updated_cost = current_cost + edge_weight
                    extended_path = current_path + [neighbor]
                    search_queue.append((neighbor, extended_path, updated_cost))
                    operation_log.append(f"Transition: ||{current_node}||---{edge_weight:.2f}--->||{neighbor}||")

    if optimal_path:
        print("\n".join(operation_log))
        print("====================================================================================")
        print(f"\nOptimal Path: {' -> '.join(map(str, optimal_path))}")
        print("====================================================================================")
        print(f"Total Cost: {final_cost:.2f}")
        print("====================================================================================")
    else:
        print(f"Goal Node ({goal}) not reached.")
        print("====================================================================================")

    formatted_explored = [int(node) for node in explored]
    print(f"All Explored Nodes: {formatted_explored}")
    print("====================================================================================")
    return formatted_explored

# Define start and goal nodes
start_point = 1  # Starting node
goal_point = 5   # Target node
explored_nodes = bfs_with_cost(graph_structure, start_point,goal_point)