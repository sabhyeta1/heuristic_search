import random
import time
import statistics
from puzzle import is_solvable
from search import a_star
from heuristics import hamming, manhattan

def random_state():
    """
    Generates a random solvable 8-puzzle state
    """
    while True:
        state = list(range(9))
        random.shuffle(state)
        if is_solvable(state):
            return state

def run_experiments(n=100):
    """
    Runs A* with both heuristics on n random solvable puzzles.
    Measures Runtime and expanded nodes
    """
    goal = [0,1,2,3,4,5,6,7,8]

    results = {"hamming": [], "manhattan": []}

    for _ in range(n):
        start = random_state()

        #Hamming
        t1 = time.perf_counter()
        _, expanded_h = a_star(start, goal, hamming)
        t2 = time.perf_counter()
        results["hamming"].append((expanded_h, t2 -t1))

        #Manhattan
        t3 = time.perf_counter()
        _, expanded_m = a_star(start, goal, manhattan)
        t4 = time.perf_counter()
        results["manhattan"].append((expanded_m, t4 - t3))

    return results

def summarize_results(results):
    """
    Computes mean and standard deviation for each heuristic
    Input:
        results (dict): {"hamming": [(nodes, time), ... ], "manhattan": [nodes, time), ...]}
    Output:
        Prints summary statistics
    """

    for name, data in results.items():
        nodes = [x[0] for x in data]
        times = [x[1] for x in data]

        mean_nodes = statistics.mean(nodes)
        std_nodes = statistics.stdev(nodes)
        mean_time = statistics.mean(times)
        std_time = statistics.stdev(times)

        print(f"\nHeuristic: {name}")
        print(f" AVG expanded nodes: {mean_nodes:.2f} +/- {std_nodes:.2f}")
        print(f" AVG runtime (s): {mean_time:.4f} +/- {std_time:.4f}")