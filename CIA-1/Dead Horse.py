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

# Dead Horse Search Algorithm
def dead_horse_search(graph, start_node, goal_node):
    visited = set()
    stack = [(start_node, [start_node])]  
    operation_log = []

    print("============================ OPERATIONS PERFORMED ============================")

    while stack:
        current_node, path = stack.pop()

        if current_node in visited:
            continue

        visited.add(current_node)

        # Explore neighbors
        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                edge_weight = graph[current_node][neighbor]['weight']
                stack.append((neighbor, path + [neighbor]))
                operation_log.append(f"Operation: ||{current_node}||---{edge_weight:.2f}--->||{neighbor}||")

                # Check if the goal node is reached
                if neighbor == goal_node:
                    total_cost = sum(graph[path[i]][path[i + 1]]['weight'] for i in range(len(path) - 1)) + edge_weight
                    print("\n".join(operation_log))
                    print("====================================================================================")
                    print(f"\nPath Found: {' -> '.join(map(str, path + [neighbor]))}")
                    print("====================================================================================")
                    print(f"Total Cost: {total_cost:.2f}")
                    print("====================================================================================")
                    visited_formatted = [int(node) for node in visited]
                    print(f"All Visited Nodes: {visited_formatted}")
                    print("====================================================================================")
                    return visited_formatted
    
    print(f"Goal Node ({goal_node}) not reached.")
    print("====================================================================================")
    visited_formatted = [int(node) for node in visited]
    print(f"All Visited Nodes: {visited_formatted}")
    print("====================================================================================")
    return visited_formatted

# Define the start and goal nodes and execute the Dead Horse Search algorithm
start_node = 1  # Source
goal_node = 5   # Goal
visited_nodes = dead_horse_search(G, start_node,goal_node)