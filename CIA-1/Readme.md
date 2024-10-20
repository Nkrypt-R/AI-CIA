# Search Algorithms Demonstration

This project implements 12 search algorithms in Python, showcasing their functionality and comparing their performance on a graph. The project is designed for educational purposes and can serve as a foundational reference for understanding various search strategies in artificial intelligence.

## Table of Contents
- [Algorithms Overview](#algorithms-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Algorithms](#algorithms)
  - [A Star](#a-star)
  - [AO Star](#ao-star)
  - [BB Cost Est](#bb-cost-est)
  - [Beam Search](#beam-search)
  - [Best First Search](#best-first-search)
  - [BFS](#bfs)
  - [BMS](#bms)
  - [Branch and Bound](#branch-and-bound)
  - [Dead Horse](#dead-horse)
  - [DFS](#dfs)
  - [Hill Climbing](#hill-climbing)
  - [Oracle](#oracle)
    
## Algorithms Overview
This project includes various search algorithms, each with unique strategies for exploring a graph to find the optimal path from a start node to a goal node.

## Installation
To run this project, make sure you have Python installed along with the required libraries. You can install the necessary packages using pip:

```bash
pip install pandas networkx
```


### Algorithms
1. British Museum Search
Description: This search algorithm is inspired by the British Museum's way of organizing knowledge, focusing on systematic exploration and coverage.

Output:![alt text](OUTPUT/BMS.png)

2. Depth First Search (DFS)
Description: A graph traversal algorithm that explores as far as possible along each branch before backtracking.

Output:![alt text](OUTPUT/DFS.png)

3. Breadth First Search (BFS)
Description: An algorithm for traversing or searching tree or graph data structures, exploring all of a node's neighbors before moving on to the next level neighbors.

Output:![alt text](OUTPUT/BFS.png)

4. Hill Climbing
Description: A local search algorithm that continuously moves in the direction of increasing elevation or value to find the peak.

Output:![alt text](<OUTPUT/Hill climbing.png>)

5. Beam Search
Description: A search algorithm that explores a graph by expanding the most promising nodes at each level, keeping only a specified number of best nodes.

Output:![alt text](<OUTPUT/Beam Search.png>)

6. Oracle Search
Description: An informed search algorithm that chooses the best neighbor based on the combined cost and heuristic to find the goal efficiently.

Output:![alt text](OUTPUT/Oracle.png)

7. Branch and Bound
Description: A general algorithm for finding optimal solutions by systematically enumerating candidate solutions while avoiding those that are not feasible.

Output:![alt text](<OUTPUT/Branch and Bound.png>)

8. Dead Horse Search
Description: An unconventional approach that repeatedly explores nodes in a specific pattern until a goal is found or all nodes are exhausted.

Output:![alt text](<OUTPUT/Dead Horse.png>)

9. Branch and Bound + Cost + Estimate
Description: An enhanced version of Branch and Bound that uses both cost and heuristic estimates to optimize the search process.

Output:![alt text](<OUTPUT/BB Cost Est.png>)

10. A* Search
Description: A popular pathfinding algorithm that combines features of Dijkstra's Algorithm and greedy best-first search, using a heuristic to guide its search.

Output:![alt text](<OUTPUT/A Star.png>)

11. AO* Search
Description: An extension of A* that can handle search problems with multiple goals or paths, optimizing the search process accordingly.

Output:![alt text](<OUTPUT/AO Star.png>)

12. Best First Search
Description: An algorithm that explores paths based on their estimated cost to the goal, always selecting the most promising node to expand.

Output:![alt text](<OUTPUT/Best First Search.png>)

