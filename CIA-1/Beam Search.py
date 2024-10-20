import pandas as pd
import networkx as nx
import math

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

# Heuristic calculation using Euclidean distance
def calculate_heuristic(node, goal):
    node_position = network_graph.nodes[node]['coordinates']
    goal_position = network_graph.nodes[goal]['coordinates']
    return math.sqrt((node_position[0] - goal_position[0]) ** 2 + (node_position[1] - goal_position[1]) ** 2)

# Beam Search Algorithm
def beam_search(graph, start, goal, beam_width):
    explored_nodes = set()
    queue = [(start, [start], 0)]  # Each element is (node, path, cost)
    operation_log = []
    optimal_path = None
    cumulative_cost = 0

    print("============================ OPERATIONS LOG ============================")

    while queue:
        # Sort the queue based on heuristic values (best nodes first)
        queue.sort(key=lambda x: calculate_heuristic(x[0], goal))
        
        # Prune the queue to the specified beam width
        queue = queue[:beam_width]
        
        new_queue = []
        for current_node, current_path, current_cost in queue:
            if current_node == goal:
                optimal_path = current_path
                cumulative_cost = current_cost
                break

            if current_node not in explored_nodes:
                explored_nodes.add(current_node)

                # Explore neighbors
                for neighbor in graph.neighbors(current_node):
                    if neighbor not in explored_nodes:
                        edge_weight = graph[current_node][neighbor]['weight']
                        new_total_cost = current_cost + edge_weight
                        extended_path = current_path + [neighbor]
                        new_queue.append((neighbor, extended_path, new_total_cost))
                        operation_log.append(f"Exploration: ||{current_node}||---{edge_weight:.2f}--->||{neighbor}||")
        
        if optimal_path:
            break

        queue = new_queue

    # Output the results
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


# Define start, goal, and beam width
starting_node = 1  # Starting node
destination_node = 5  # Target node
beam_width_setting = 2  
visited_nodes = beam_search(network_graph, starting_node, destination_node, beam_width_setting)