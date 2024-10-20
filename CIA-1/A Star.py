import pandas as pd
import networkx as nx
import math
import heapq

# Load node coordinates and edge data
node_dataframe = pd.read_csv('C:/Users/rlnar/Desktop/VSCODE/CIA-1/DATA/node_positions.csv')
edge_dataframe = pd.read_csv('C:/Users/rlnar/Desktop/VSCODE/CIA-1/DATA/path_details.csv')
undirected_graph = nx.Graph()

# Add nodes with their positions to the graph
for _, node_row in node_dataframe.iterrows():
    undirected_graph.add_node(node_row['Node'], coordinates=(node_row['X'], node_row['Y']))

# Define bidirectional edges with weights
for _, edge_row in edge_dataframe.iterrows():
    undirected_graph.add_edge(edge_row['Source Node'], edge_row['Target Node'], weight=edge_row['Weight'])
    undirected_graph.add_edge(edge_row['Target Node'], edge_row['Source Node'], weight=edge_row['Weight'])

# Heuristic based on Euclidean distance
def calculate_heuristic(current_node, goal_node):
    current_pos = undirected_graph.nodes[current_node]['coordinates']
    goal_pos = undirected_graph.nodes[goal_node]['coordinates']
    return math.dist(current_pos, goal_pos)  # Using math.dist for Euclidean distance

# A* Search Algorithm
def a_star_algorithm(graph, start, goal):
    explored = set()
    priority_queue = []
    heapq.heappush(priority_queue, (0, start, [start], 0))  # (f-score, current_node, path, g-score)
    final_cost = float('inf')
    operation_trace = []

    print("============================ SEARCH OPERATIONS ============================")

    while priority_queue:
        f_score, active_node, active_path, g_score = heapq.heappop(priority_queue)

        if active_node in explored:
            continue

        explored.add(active_node)

        # If goal node is reached, terminate search
        if active_node == goal:
            final_cost = g_score
            solution_path = active_path
            break

        # Explore neighbors
        for adjacent_node in graph.neighbors(active_node):
            if adjacent_node not in explored:
                edge_cost = graph[active_node][adjacent_node]['weight']
                updated_g_score = g_score + edge_cost
                estimated_heuristic = calculate_heuristic(adjacent_node, goal)
                updated_f_score = updated_g_score + estimated_heuristic
                
                heapq.heappush(priority_queue, (updated_f_score, adjacent_node, active_path + [adjacent_node], updated_g_score))
                operation_trace.append(f"Transition: ||{active_node}||---{edge_cost:.2f}--->||{adjacent_node}||")

    if final_cost < float('inf'):
        print("\n".join(operation_trace))
        print("====================================================================================")
        print(f"\nOptimal Path: {' -> '.join(map(str, solution_path))}")
        print("====================================================================================")
        print(f"Path Cost: {final_cost:.2f}")
        print("====================================================================================")
    else:
        print(f"Goal Node ({goal}) not reached.")
        print("====================================================================================")

    formatted_explored = [int(node) for node in explored]
    print(f"All Explored Nodes: {formatted_explored}")
    print("====================================================================================")
    return formatted_explored

# Initialize start and goal nodes
start_point = 1  # Starting node
goal_point = 5   # Target node
explored_nodes = a_star_algorithm(undirected_graph, start_point, goal_point)