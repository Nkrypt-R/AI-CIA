import pandas as pd
import networkx as nx
import math
import heapq

# Load node coordinates and path details
node_data = pd.read_csv('C:/Users/rlnar/Desktop/VSCODE/CIA-1/DATA/node_positions.csv')
edge_data = pd.read_csv('C:/Users/rlnar/Desktop/VSCODE/CIA-1/DATA/path_details.csv')
graph_network = nx.Graph()

# Add nodes to the graph
for _, node_row in node_data.iterrows():
    graph_network.add_node(node_row['Node'], pos=(node_row['X'], node_row['Y']))

# Define bidirectional edges with weights
for _, edge_row in edge_data.iterrows():
    graph_network.add_edge(edge_row['Source Node'], edge_row['Target Node'], weight=edge_row['Weight'])
    graph_network.add_edge(edge_row['Target Node'], edge_row['Source Node'], weight=edge_row['Weight'])

# Heuristic generation (Euclidean distance)
def calculate_heuristic(node, goal):
    node_pos = graph_network.nodes[node]['pos']
    goal_pos = graph_network.nodes[goal]['pos']
    return math.sqrt((node_pos[0] - goal_pos[0]) ** 2 + (node_pos[1] - goal_pos[1]) ** 2)

# Branch and Bound Algorithm
def branch_and_bound(graph, start, goal):
    explored_nodes = set()
    priority_queue = []
    heapq.heappush(priority_queue, (0, start, [start]))  # Push (cost, node, path)
    minimum_cost = float('inf')
    operation_log = []

    print("============================ OPERATIONS LOG ============================")
    
    while priority_queue:
        current_cost, current_node, path = heapq.heappop(priority_queue)

        if current_node in explored_nodes:
            continue

        explored_nodes.add(current_node)

        # If goal is reached and the path is optimal, update the minimum cost
        if current_node == goal:
            if current_cost < minimum_cost:
                minimum_cost = current_cost
                optimal_path = path
            continue
        
        # Explore neighbors
        for neighbor in graph.neighbors(current_node):
            if neighbor not in explored_nodes:
                edge_weight = graph[current_node][neighbor]['weight']
                new_cost = current_cost + edge_weight
                new_path = path + [neighbor]
                heuristic = calculate_heuristic(neighbor, goal)
                heapq.heappush(priority_queue, (new_cost + heuristic, neighbor, new_path))
                operation_log.append(f"Exploration: ||{current_node}||---{edge_weight:.2f}--->||{neighbor}||")

    # Output the results
    if minimum_cost < float('inf'):
        print("\n".join(operation_log))
        print("====================================================================================")
        print(f"\nOptimal Path: {' -> '.join(map(str, optimal_path))}")
        print("====================================================================================")
        print(f"Total Cost: {minimum_cost:.2f}")
        print("====================================================================================")
    else:
        print(f"Goal Node ({goal}) not reached.")
        print("====================================================================================")

    formatted_explored_nodes = [int(node) for node in explored_nodes]
    print(f"All Explored Nodes: {formatted_explored_nodes}")
    print("====================================================================================")
    return formatted_explored_nodes

# Define the start, goal, and run the Branch and Bound algorithm
start_node = 1  # Starting node
goal_node = 5   # Target node
visited_nodes = branch_and_bound(graph_network, start_node,goal_node)