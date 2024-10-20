import pandas as pd
import networkx as nx

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

# Depth First Search (DFS) Algorithm
def depth_first_search(graph, start, goal):
    visited = set()
    stack = [(start, [start], 0)]  # (current_node, path_taken, cost)
    path_found = None
    operation_log = []

    print("============================ OPERATIONS LOG ============================")
    
    while stack:
        current_node, path, cost = stack.pop()

        if current_node in visited:
            continue

        visited.add(current_node)

        # Goal reached
        if current_node == goal:
            path_found = path
            total_cost = cost
            break

        # Explore neighbors
        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                edge_weight = graph[current_node][neighbor]['weight']
                new_cost = cost + edge_weight
                new_path = path + [neighbor]
                stack.append((neighbor, new_path, new_cost))
                operation_log.append(f"Operation: ||{current_node}||---{edge_weight:.2f}--->||{neighbor}||")

    # Output the results
    if path_found:
        print("\n".join(operation_log))
        print("====================================================================================")
        print(f"\nPath Found: {' -> '.join(map(str, path_found))}")
        print("====================================================================================")
        print(f"Total Cost: {total_cost:.2f}")
        print("====================================================================================")
    else:
        print(f"Goal Node ({goal}) not reached.")
        print("====================================================================================")

    formatted_visited_nodes = [int(node) for node in visited]
    print(f"All Explored Nodes: {formatted_visited_nodes}")
    print("====================================================================================")
    return formatted_visited_nodes

# Define the start and goal nodes and execute the DFS algorithm
start_node = 1  # Source
goal_node = 5   # Goal
visited_nodes = depth_first_search(G, start_node,goal_node)