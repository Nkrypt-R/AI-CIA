# Search Algorithms Demonstration

This project implements 12 search algorithms in Python, showcasing their functionality and comparing their performance on a graph. The project is designed for educational purposes and can serve as a foundational reference for understanding various search strategies in artificial intelligence.

## Table of Contents
- [Algorithms Overview](#algorithms-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Algorithms](#algorithms)
  - [1. British Museum Search](#1-british-museum-search)
  - [2. Depth First Search (DFS)](#2-depth-first-search-dfs)
  - [3. Breadth First Search (BFS)](#3-breadth-first-search-bfs)
  - [4. Hill Climbing](#4-hill-climbing)
  - [5. Beam Search](#5-beam-search)
  - [6. Oracle Search](#6-oracle-search)
  - [7. Branch and Bound](#7-branch-and-bound)
  - [8. Dead Horse Search](#8-dead-horse-search)
  - [9. Branch and Bound + Cost + Estimate](#9-branch-and-bound-cost-estimate)
  - [10. A* Search](#10-a-search)
  - [11. AO* Search](#11-ao-search)
  - [12. Best First Search](#12-best-first-search)
- [Contributing](#contributing)
- [License](#license)

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


This `README.md` structure provides clear instructions on the purpose of the project, installation, usage, and a detailed description of each algorithm. Feel free to add more details to the "Output" sections as you finalize the implementation of the algorithms.
