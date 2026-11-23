
# Alpha-Beta Pruning Algorithm

# Step 1: Define Alpha-Beta function
def alphabeta(depth, node, maximizing,
              values, alpha, beta):

    # Step 2: Check leaf node
    if depth == 3:
        return values[node]

    if maximizing:
        best = float('-inf')

        # Check child nodes
        for i in range(2):
            value = alphabeta(depth + 1,
                              node * 2 + i,
                              False, values,
                              alpha, beta)

            best = max(best, value)
            alpha = max(alpha, best)

            # Pruning condition
            if alpha >= beta:
                break

        return best

    else:
        best = float('inf')

        # Check child nodes
        for i in range(2):
            value = alphabeta(depth + 1,
                              node * 2 + i,
                              True, values,
                              alpha, beta)

            best = min(best, value)
            beta = min(beta, best)

            # Pruning condition
            if alpha >= beta:
                break

        return best


# Step 3: Leaf node values
values = [3, 5, 6, 9, 1, 2, 0, -1]

# Step 4: Call the function
result = alphabeta(0, 0, True, values,
                   float('-inf'), float('inf'))

# Step 5: Display result
print("Optimal value:", result)
 