import numpy as np
from puzzle import EightPuzzle

def main():
    ## Set the initial state and goal state
    initialState = np.array(
        [
            [3, 1, 5], 
            [2, 0, 4], 
            [6, 7, 8]
        ]
    )
    goalState = np.array(
        [
            [0, 1, 2], 
            [3, 4, 5], 
            [6, 7, 8]
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
