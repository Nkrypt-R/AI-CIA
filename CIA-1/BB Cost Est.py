import pandas as pd
import networkx as nx
import math
import heapq

# Load node coordinates and path details
node_df = pd.read_csv('C:/Users/rlnar/Desktop/VSCODE/CIA-1/DATA/node_positions.csv')
edge_df = pd.read_csv('C:/Users/rlnar/Desktop/VSCODE/CIA-1/DATA/path_details.csv')
graph_structure = nx.Graph()

# Add nodes along with their coordinates to the graph
for _, node_data in node_df.iterrows():
    graph_structure.add_node(node_data['Node'], coordinates=(node_data['X'], node_data['Y']))

# Define bidirectional edges with weights
for _, edge_data in edge_df.iterrows():
    graph_structure.add_edge(edge_data['Source Node'], edge_data['Target Node'], weight=edge_data['Weight'])
    graph_structure.add_edge(edge_data['Target Node'], edge_data['Source Node'], weight=edge_data['Weight'])

# Heuristic function (Euclidean distance)
def compute_heuristic(node, goal):
    node_position = graph_structure.nodes[node]['coordinates']
    goal_position = graph_structure.nodes[goal]['coordinates']
    return math.dist(node_position, goal_position)  # Using math.dist for the Euclidean distance

# Branch and Bound with Cost and Heuristic Estimation
def branch_and_bound_with_estimation(graph, start, goal):
    explored = set()
    priority_queue = []
    heapq.heappush(priority_queue, (0, start, [start], 0))  # (f-cost, current_node, path, total_cost)
    optimal_cost = float('inf')
    operation_log = []

    print("============================ OPERATIONS LOG ============================")

    while priority_queue:
        f_cost, current_node, current_path, total_path_cost = heapq.heappop(priority_queue)

        if current_node in explored:
            continue

        explored.add(current_node)

        if current_node == goal:
            if total_path_cost < optimal_cost:
                optimal_cost = total_path_cost
                best_path = current_path
            continue

        for neighbor in graph.neighbors(current_node):
            if neighbor not in explored:
                edge_cost = graph[current_node][neighbor]['weight']
                updated_cost = total_path_cost + edge_cost
                heuristic_value = compute_heuristic(neighbor, goal)
                estimated_f_cost = updated_cost + heuristic_value
                heapq.heappush(priority_queue, (estimated_f_cost, neighbor, current_path + [neighbor], updated_cost))
                operation_log.append(f"Transition: ||{current_node}||---{edge_cost:.2f}--->||{neighbor}||")

    if optimal_cost < float('inf'):
        print("\n".join(operation_log))
        print("====================================================================================")
        print(f"\nOptimal Path: {' -> '.join(map(str, best_path))}")
        print("====================================================================================")
        print(f"Total Cost: {optimal_cost:.2f}")
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
explored_nodes = branch_and_bound_with_estimation(graph_structure, start_point,goal_point)