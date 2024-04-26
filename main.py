import numpy as np
from puzzle import EightPuzzle

def main():
    ## Set the initial state and goal state
    initialState = np.array(
        [
            [1, 2, 3], 
            [8, 0, 4], 
            [7, 6, 5]
        ]
    )
    goalState = np.array(
        [
            [2, 8, 1], 
            [0, 4, 3], 
            [7, 6, 5]
        ]
    )

    ## Index of state and goal
    stateIndex = (1, 1)
    goalIndex = (1, 0)

    p = EightPuzzle(initialState, stateIndex, goalState, goalIndex)
    p.solve()
    # print("\nTree:")
    # print(p.tree)
    print("\n")
    p.print()
    p.print("output.txt")


main()
