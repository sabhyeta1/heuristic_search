"""
Contains the 8-puzzle logic, including the solvability check
"""

def count_inversions(state):
    """
    Counts the number of inversions made in the 8-puzzle state
    Input:
        state (list[int]): 9 elements, 0 = empty tile
    Output:
        int: number of inversions
    """
    count = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if state[i] != 0 and state[j] != 0 and state[i] > state[j]:
                count += 1
    return count

def is_solvable(state):
    """
    Checks if the 8-puzzle state is solvable
    """
    inversions = count_inversions(state)
    return inversions % 2 == 0

def get_neighbors(state):
    """
    Generates all valid neighbors of the 8-puzzle state by moving the blank tile (0) up, down, left or right.
    Input:
        state (list[int]): 9 elements, 0 = empty tile
    Output:
        list[list[int]]: list of new states after valid moves
    """
    neighbors = []

    #to find the position of 0
    zero_index = state.index(0)
    row = zero_index // 3
    col = zero_index % 3

    #These are the possible Directions to move
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for r_offset, c_offset in moves:
        new_row = row + r_offset
        new_col = col + c_offset

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_state = state.copy()
            new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
            neighbors.append(new_state)

    return neighbors