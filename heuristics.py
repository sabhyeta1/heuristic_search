def hamming(state, goal):
    """
    Count tiles that are not in the correct position.
    """
    return sum(1 for i in range(9) if state[i] != 0 and state[i] != goal[i])

def manhattan(state, goal):
    """
    Sums the Manhattan distance of each tile from its target positon.
    """
    goal_pos = {tile: (i // 3, i % 3) for i, tile in enumerate(goal)}
    dist = 0
    for i, tile in enumerate(state):
        if tile == 0:
            continue
        r, c = i // 3, i % 3
        gr, gc = goal_pos[tile]
        dist += abs(r - gr) + abs(c - gc)
    return dist