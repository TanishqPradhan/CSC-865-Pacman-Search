Name - Tanishq Pradhan

SFSU ID - 922243982

Question 1:
For the DFS, I implemented a stack. The stack stores the start state along with an empty list of actions to reach that particular state.
I have used a set to keep track of the already visited states in the stack. The main while condition checks whether the stack is empty or not.
If not empty the current state is checked for already visited states and goal state. If both conditions not passed, the successor nodes for the current state are calculated.
This keeps on iterating till we reach goal state.

Question 2:
Similar to question 1, the only difference is that a queue has been implemented as the frontier.

Question 3:
For uniform cost search, a priority queue has been implemented. The queue holds the current state, list of actions and cost.
Similar to the first two questions the successors nodes are calculated and iterated till we reach goal state.

Question 4:
Similar to question 3 we use a priority queue, the only added point is the use of the heuristic value which has been calculated.
and appended to the cost of the state.

Question 5:
For this, we store the location and the corners not visited as x and y coordinates, we calculate the new x and y coordinates by appending the cost of the next state to the previous coordinates.
Check if the current state have hit a wall, and calculate the next state coordinates and corners. This is iterated till we reach the goal state.

Question 6:
Similar to the previous question, the manhattan distance is calulated and added to the x and y coordinates.
The maximum of the list of distances is selected as the heuristic value.

Question 7:
The location of pacman and food of the current state is stored. Iterating for all food, we create a new problem state with the current location as the start state and the location of the food as the goal state.
we implement bfs on this new problem and calulate the length of the solution path as the distance. For each distance between pacman and the food we take the maximum value as the heuristic.

Question 8:
Based on the hint given by professor BFS is implemented on the problem state. I was not able to find an optimal solution for the shortest path.


It took me approximately 28~30 hours to complete this project.