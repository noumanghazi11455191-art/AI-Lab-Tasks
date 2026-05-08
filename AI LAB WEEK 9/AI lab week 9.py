# Min-Max Algorithm Implementation

import math

def minimax(depth, index, isMaxPlayer, values, maxDepth):

    if depth == maxDepth:
        return values[index]
    if isMaxPlayer:
        left = minimax(depth + 1, index * 2, False, values, maxDepth)
        right = minimax(depth + 1, index * 2 + 1, False, values, maxDepth)
        return max(left, right)
    else:
        left = minimax(depth + 1, index * 2, True, values, maxDepth)
        right = minimax(depth + 1, index * 2 + 1, True, values, maxDepth)
        return min(left, right)

values = [4, 6, 1, 7, 3, 8, 2, 5]

maxDepth = int(math.log2(len(values)))

result = minimax(0, 0, True, values, maxDepth)

print("Optimal value is:", result)