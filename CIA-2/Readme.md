# Game Tree Algorithms: Minimax and Alpha-Beta Pruning

This repository contains implementations of two essential game tree search algorithms: Minimax and Alpha-Beta Pruning. These algorithms are widely used in artificial intelligence for decision-making in two-player games.

## Table of Contents
- [Game Tree Algorithms: Minimax and Alpha-Beta Pruning](#game-tree-algorithms-minimax-and-alpha-beta-pruning)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Min-max Pruning](#min-max-pruning)
    - [Description](#description)
    - [Implementation](#implementation)
  - [Alpha-beta Pruning](#alpha-beta-pruning)
    - [Description](#description-1)
    - [Implementation](#implementation-1)
  - [Minmax Algorithm](#minmax-algorithm)
  - [Alpha-Beta Pruning Algorithm](#alpha-beta-pruning-algorithm)

## Overview

This repository contains implementations of the Minimax and Alpha-Beta Pruning algorithms, which are both used for decision-making in two-player games by searching a game tree to identify the best possible move. 

## Min-max Pruning

### Description

The Minimax Algorithm is a recursive decision-making strategy used in two-player games, where players take turns making moves. The main goal is to minimize the possible loss for the worst-case scenario while maximizing potential gains. The algorithm assumes that both players are playing optimally and aims to find the best move for the player who is about to move (the maximizer).

Here's how it works:

1. Game Tree: The algorithm represents the game as a tree, where each node corresponds to a game state, and edges represent possible moves.
   
2. Leaf Nodes: The algorithm evaluates the leaf nodes (end states) of the game tree, assigning values based on the desirability of those states for the maximizing player (higher values are better).
   
3. Backtracking:
During the backtracking phase, the algorithm evaluates non-leaf nodes:
For the maximizer, it chooses the highest value from its children nodes.
For the minimizer, it chooses the lowest value from its children nodes.

4. Optimal Move: The algorithm propagates values up the tree until it reaches the root node, where the optimal move for the maximizer can be determined.

### Implementation

1. Function Definition: Define a recursive function that takes parameters like the current depth, the index of the node, whether it's the maximizer's turn, the list of values (leaf nodes), and the maximum depth of the game tree.

2. Base Case: If the current depth is equal to the maximum depth, return the value of the node from the list of leaf values.

3. Maximizer's Logic: If it’s the maximizer’s turn:

Initialize a variable to keep track of the maximum value (starting with negative infinity).
Iterate through the possible child nodes, recursively calling the function and updating the maximum value.

4. Minimizer's Logic: If it’s the minimizer’s turn:

Initialize a variable to keep track of the minimum value (starting with positive infinity).
Similarly, iterate through the possible child nodes, recursively calling the function and updating the minimum value.

5. Return Values: After evaluating the tree, return the maximum or minimum value up the recursion stack to find the optimal move.
   
## Alpha-beta Pruning

### Description 

Alpha-Beta Pruning is an optimization technique for the Minimax algorithm used in decision-making for two-player games, such as chess or tic-tac-toe. The goal of Alpha-Beta Pruning is to reduce the number of nodes evaluated in the game tree without affecting the final decision. This is achieved by "pruning" branches that are not relevant to the decision-making process—i.e., branches that cannot influence the outcome of the game.

The algorithm works by maintaining two values, Alpha and Beta:

Alpha: The best (highest) value that the maximizer can guarantee so far.
Beta: The best (lowest) value that the minimizer can guarantee so far.

As the tree is traversed, the algorithm updates these values:

- If it finds a move that is worse than the current Alpha for the maximizer or Beta for the minimizer, the branch is pruned, meaning further exploration of that branch is unnecessary.
  
The pruning occurs when:

- The maximizer's best option (alpha) becomes greater than or equal to the minimizer's best option (beta), meaning the minimizer would not allow the maximizer to reach that branch.

### Implementation

1. Start at the Root: Begin at the root node of the game tree, where it's the maximizer's turn to choose the best move.

2. Track Alpha and Beta: Keep track of two values:

- Alpha: The highest value that the maximizer can guarantee so far.
- Beta: The lowest value that the minimizer can guarantee so far.
  
3. Maximizer's Turn:

- The maximizer explores all possible moves.
- At each node, if the value of the move is higher than the current alpha, update alpha.
- If beta is less than or equal to alpha (i.e., the minimizer wouldn't allow reaching that move), prune the remaining branches—meaning, stop exploring further down that path.
  
4. Minimizer's Turn:

- The minimizer explores its options.
- At each node, if the value of the move is lower than the current beta, update beta.
- If alpha becomes greater than or equal to beta, prune the remaining branches.

5. Recursive Process: Continue this process recursively, alternating between the maximizer and minimizer, updating alpha and beta as you go deeper in the tree.

6. Return the Best Move: When the tree is fully explored (or pruned), the algorithm returns the optimal move for the maximizer, using the minimized search space thanks to pruning.

## Minmax Algorithm

**Test Case 1:**

Tree Depth: 2
Leaf Node Values: [3, 5, 6, 9]
Expected Output: 5
Explanation:
Max chooses between the minimum of its two branches.
Left subtree: MIN(3, 5) = 3
Right subtree: MIN(6, 9) = 6
Max chooses the maximum: MAX(3, 6) = 5

**Test Case 2:**

Tree Depth: 3
Leaf Node Values: [2, 9, 1, 4, 6, 8, 3, 7]
Expected Output: 7
Explanation:
First, evaluate all min nodes at depth 2:
Left subtree:
MAX(2, 9) = 9
MAX(1, 4) = 4
MIN(9, 4) = 4
Right subtree:
MAX(6, 8) = 8
MAX(3, 7) = 7
MIN(8, 7) = 7
Max chooses between 4 and 7: MAX(4, 7) = 7.

## Alpha-Beta Pruning Algorithm

**Test Case 1:**

Tree Depth: 2
Leaf Node Values: [3, 5, 6, 9]
Expected Output: 5
Pruned Branches: None
Explanation:
Alpha-Beta Pruning doesn't prune any branches in this simple example, and the output is the same as the Minmax result: 5.

**Test Case 2:**

Tree Depth: 3
Leaf Node Values: [2, 9, 1, 4, 6, 8, 3, 7]
Expected Output: 7
Pruned Branches: Left subtree of the right MIN node (i.e., 3 is not evaluated).
Explanation:
The algorithm begins similarly to Minmax:
In the left subtree:
MAX(2, 9) = 9
MAX(1, 4) = 4
MIN(9, 4) = 4
Alpha-Beta sets alpha = 4.
In the right subtree:
MAX(6, 8) = 8
Pruning occurs as beta = 8 and alpha = 4, so the remaining branch with 3 is not evaluated.
MAX(3, 7) = 7
MIN(8, 7) = 7
Max chooses between 4 and 7: MAX(4, 7) = 7.

