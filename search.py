import heapq #Priority Queue
from heuristics import hamming, manhattan
from puzzle import get_neighbors, is_solvable

def a_star(start, goal, heuristic):
    """
    A* search for the 8-puzzle.
    heuristic: function(state, goal) -> int
    """
    if is_solvable(start) == False:
        return None, 0

    open_set = []
    #g = cost so far, h = heuristic, f = g +h
    heapq.heappush(open_set, (heuristic(start,goal), start, 0, [start]))
    closed_set = set()

    while open_set:
        f, state, g, path = heapq.heappop(open_set)

        if state == goal:
            return path, len(closed_set)

        closed_set.add(tuple(state))

        for neighbor in get_neighbors(state):
            if tuple(neighbor) in closed_set:
                continue

            g_new = g + 1
            f_new = g_new + heuristic(neighbor, goal)
            heapq.heappush(open_set, (f_new, neighbor, g_new, path + [neighbor]))

    return None, len(closed_set)