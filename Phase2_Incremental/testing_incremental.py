
from implementation_incremental import A_star_map_coloring
from testCases_incremental import scenarios


for name, graph in scenarios.items():
    solution = A_star_map_coloring(graph)
    print(f"{name}: {'Solution found with colors' if solution else 'No solution'}")
    if solution:
        print(f"{solution}\n")

