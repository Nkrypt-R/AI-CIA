import math
import random

def minimax(depth, nodeIndex, isMaximizingPlayer, values, maxDepth, alpha, beta):
    # Base case: leaf node
    if depth == maxDepth:
        print(f"Leaf node reached at depth {depth}, returning value: {values[nodeIndex]}")
        return values[nodeIndex]

    if isMaximizingPlayer:
        best = -math.inf
        print(f"\nMaximizer at depth {depth}")
        print("====================================================================================")

        for i in range(2):
            value = minimax(depth + 1, nodeIndex * 2 + i, False, values, maxDepth, alpha, beta)
            print(f"Maximizer at depth {depth}, comparing value: {value} with best: {best}")
            best = max(best, value)
            alpha = max(alpha, best)

            # Beta cut-off
            if beta <= alpha:
                print(f"Beta cut-off at Maximizer depth {depth} with alpha: {alpha} and beta: {beta}")
                break

        print(f"Maximizer at depth {depth}, selected best: {best}")
        print("====================================================================================")
        return best
    else:
        best = math.inf
        print(f"\nMinimizer at depth {depth}")
        print("====================================================================================")

        for i in range(2):
            value = minimax(depth + 1, nodeIndex * 2 + i, True, values, maxDepth, alpha, beta)
            print(f"Minimizer at depth {depth}, comparing value: {value} with best: {best}")
            best = min(best, value)
            beta = min(beta, best)

            # Alpha cut-off
            if beta <= alpha:
                print(f"Alpha cut-off at Minimizer depth {depth} with alpha: {alpha} and beta: {beta}")
                break

        print(f"Minimizer at depth {depth}, selected best: {best}")
        return best

def generate_leaf_node_values(num_leaf_nodes):
    return [random.randint(-10, 10) for _ in range(num_leaf_nodes)]

def main():
    # Get user input for maximum depth
    maxDepth = int(input("Enter the maximum depth of the game tree: "))
    
    # Generate random leaf node values
    num_leaf_nodes = 2 ** maxDepth
    values = generate_leaf_node_values(num_leaf_nodes)
    
    print(f"Generated leaf node values: {values}\n")

    # Initialize alpha and beta values for minimax algorithm
    alpha = -math.inf
    beta = math.inf

    # Calculate the optimal value using Minimax
    optimalValue = minimax(0, 0, True, values, maxDepth, alpha, beta)

    print("====================================================================================")
    print("The optimal value is:", optimalValue)
    print("====================================================================================")

if __name__ == "_main_":
    main()