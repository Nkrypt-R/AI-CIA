import pandas as pd
import networkx as nx
import math
import heapq

# Load data for nodes and edges
node_data_frame = pd.read_csv('C:/Users/rlnar/Desktop/VSCODE/CIA-1/DATA/node_positions.csv')
edge_data_frame = pd.read_csv('C:/Users/rlnar/Desktop/VSCODE/CIA-1/DATA/path_details.csv')
graph_structure = nx.DiGraph()  # Directed graph for AO* algorithm

# Add nodes along with their coordinates
for _, node_info in node_data_frame.iterrows():
    graph_structure.add_node(node_info['Node'], coordinates=(node_info['X'], node_info['Y']))

# Define edges with associated weights
for _, edge_info in edge_data_frame.iterrows():
    graph_structure.add_edge(edge_info['Source Node'], edge_info['Target Node'], weight=edge_info['Weight'])

# Euclidean heuristic function to estimate the cost between two nodes
def compute_heuristic(current, goal):
    current_coords = graph_structure.nodes[current]['coordinates']
    goal_coords = graph_structure.nodes[goal]['coordinates']
    return math.dist(current_coords, goal_coords)  # Simplified using math.dist()

# AO* search implementation
def ao_star(graph, source, goal):
    processed_nodes = set()
    cost_tracker = {source: 0}
    actions_taken = []
    priority_list = [(0, source)]  # Min-heap for selecting the lowest-cost node

    print("============================ PROCESS TRACE ============================")

    while priority_list:
        present_cost, current_node = heapq.heappop(priority_list)

        if current_node in processed_nodes:
            continue

        processed_nodes.add(current_node)

        for next_node in graph.neighbors(current_node):
            transition_cost = graph[current_node][next_node]['weight']
            accumulated_cost = present_cost + transition_cost
            
            if next_node not in processed_nodes:
                if next_node not in cost_tracker or accumulated_cost < cost_tracker[next_node]:
                    cost_tracker[next_node] = accumulated_cost
                    estimated_cost = compute_heuristic(next_node, goal)
                    heapq.heappush(priority_list, (accumulated_cost + estimated_cost, next_node))
                    actions_taken.append(f"Transition: ||{current_node}||---{transition_cost:.2f}--->||{next_node}||")
                    
                    if next_node == goal:
                        print("\n".join(actions_taken))
                        print("====================================================================================")
                        print(f"\nPath Identified: {' -> '.join(map(str, processed_nodes))} -> {goal}")
                        print("====================================================================================")
                        print(f"Final Cost: {accumulated_cost:.2f}")
                        print("====================================================================================")
                        return processed_nodes

    print(f"Goal Node ({goal}) unreachable.")
    print("====================================================================================")
    
    formatted_processed_nodes = [int(node) for node in processed_nodes]
    print(f"All Processed Nodes: {formatted_processed_nodes}")
    print("====================================================================================")
    return formatted_processed_nodes

# Source and target nodes initialization
origin_node = 1  # Starting node
destination_node = 5  # Goal node
processed = ao_star(graph_structure, origin_node, destination_node)