"""
Main script for the 8-Puzzle A* Heuristic Search project.
Demonstrates:
1. Solvability check
2. Neighbor generation
3. Heuristic comparison (Hamming vs. Manhattan)
4. A* pathfinding demonstration
5. Experimental performance evaluation
"""

from puzzle import count_inversions, is_solvable, get_neighbors
from heuristics import hamming, manhattan
from search import a_star
from experiments import run_experiments, summarize_results


def demo_basic_functions():
    """
    Simple tests for solvability and neighbor generation.
    """
    test_state = [1, 2, 3,
                  4, 0, 5,
                  6, 7, 8]

    print("=== BASIC FUNCTION TEST ===")
    print("State:", test_state)
    print("Inversions:", count_inversions(test_state))
    print("Solvable:", is_solvable(test_state))

    neighbors = get_neighbors(test_state)
    print("\nPossible moves:")
    for n in neighbors:
        print(n)
    print(f"Total neighbors: {len(neighbors)}\n")


def demo_heuristics():
    """
    Compares heuristic values for the same state.
    """
    state = [1, 2, 3, 4, 5, 6, 0, 7, 8]
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    print("=== HEURISTIC TEST ===")
    print("State:", state)
    print("Goal :", goal)
    print("Hamming distance :", hamming(state, goal))
    print("Manhattan distance:", manhattan(state, goal))
    print()


def demo_a_star():
    """
    Runs a single A* search example.
    """
    start = [1, 2, 3,
             4, 0, 6,
             7, 5, 8]
    goal = [1, 2, 3,
            4, 5, 6,
            7, 8, 0]

    print("=== A* SEARCH DEMO (Manhattan) ===")
    path, expanded = a_star(start, goal, manhattan)
    if path:
        print("Solution found!")
        print("Steps needed :", len(path) - 1)
        print("Nodes expanded:", expanded)
    else:
        print("No solution found.")
    print()


def run_full_experiment():
    """
    Runs 100 random puzzles and compares heuristic performance.
    """
    print("=== EXPERIMENT: 100 Random Solvable States ===")
    results = run_experiments(100)
    summarize_results(results)
    print()


if __name__ == "__main__":
    demo_basic_functions()
    demo_heuristics()
    demo_a_star()
    run_full_experiment()
