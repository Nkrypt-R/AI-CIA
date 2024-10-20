import pandas as pd
import networkx as nx
import math

# Load node positions and path details
nodes_df = pd.read_csv('C:/Users/rlnar/Desktop/VSCODE/CIA-1/DATA/node_positions.csv')
paths_df = pd.read_csv('C:/Users/rlnar/Desktop/VSCODE/CIA-1/DATA/path_details.csv')
G = nx.Graph()

# Add nodes to the graph
for index, row in nodes_df.iterrows():
    G.add_node(row['Node'], pos=(row['X'], row['Y']))

# Define bidirectional edges with weights
for index, row in paths_df.iterrows():
    G.add_edge(row['Source Node'], row['Target Node'], weight=row['Weight'])
    G.add_edge(row['Target Node'], row['Source Node'], weight=row['Weight'])  

# Heuristic generation (Euclidean distance)
def generate_heuristic(node, goal):
    node_pos = G.nodes[node]['pos']
    goal_pos = G.nodes[goal]['pos']
    return math.sqrt((node_pos[0] - goal_pos[0]) ** 2 + (node_pos[1] - goal_pos[1]) ** 2)

# Hill Climbing Algorithm
def hill_climbing(graph, start_node, goal_node):
    visited = set()
    current_node = start_node
    total_cost = 0
    path = [start_node]
    output = []

    print("============================ OPERATIONS PERFORMED ============================")
    while current_node != goal_node:
        visited.add(current_node)

        # Get neighbors and their weights
        neighbors = [(neighbor, graph[current_node][neighbor]['weight']) for neighbor in graph.neighbors(current_node)]
        if not neighbors:
            break
        
        # Sort neighbors by heuristic value
        neighbors.sort(key=lambda x: generate_heuristic(x[0], goal_node))
        
        best_neighbor, best_weight = neighbors[0]

        # If the best neighbor has already been visited, break
        if best_neighbor in visited:
            break

        # Update path and total cost
        path.append(best_neighbor)
        total_cost += best_weight
        output.append(f"Operation: ||{current_node}||---{best_weight:.2f}--->||{best_neighbor}||")

        current_node = best_neighbor

    # Output results
    if current_node == goal_node:
        print("\n".join(output))
        print("====================================================================================")
        print(f"\nPath Found: {' -> '.join(map(str, path))}")
        print("====================================================================================")
        print(f"Total Cost: {total_cost:.2f}")
        print("====================================================================================")
    else:
        print(f"Goal Node ({goal_node}) not reached.")
        print("====================================================================================")

    # Print all visited nodes
    visited_formatted = [int(node) for node in visited]
    print(f"All Visited Nodes: {visited_formatted}")
    print("====================================================================================")
    return visited_formatted

# Define the start and goal nodes and execute the Hill Climbing algorithm
start_node = 1  # Source
goal_node = 5   # Goal
visited_nodes = hill_climbing(G, start_node,goal_node)