# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    frontier = util.Stack() #create a Frontier Stack
    startState = problem.getStartState() #store the Start State and Print it
    print(startState)

    frontier.push((startState,[])) #Push the Start state and an empty list of moves in the frontier.

    alreadyVisited = set() #create an empty set of already vistied states.

    while not frontier.isEmpty(): #check if frontier is not empty.

        currentNodeState, currentNodeActions = frontier.pop() #store the current state and the list of actions of the last node in the stack.
        
        if(currentNodeState in alreadyVisited): #check if current state has already been visited.
            continue

        if problem.isGoalState(currentNodeState): #check if current state is the goal state.
            return currentNodeActions

        alreadyVisited.add(currentNodeState) #append the current state to the set of already visited states.

        for state, action, cost in problem.getSuccessors(currentNodeState): #Iterate for the successor states.

            if(state in alreadyVisited): #check if state has already been visited.
                continue

            frontier.push((state, currentNodeActions+[action])) #push the state and appended action to the frontier.

    #util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    frontier = util.Queue() #create a queue for the frontier.
 
    frontier.push((problem.getStartState(),[])) #push the start state and the empty list of actions to the forntier.
    
    alreadyVisited = set() #create and empty set of already visited states.

    while not frontier.isEmpty(): #check if frontier is not empty.

        currentNodeState, currentNodeActions = frontier.pop() #store the state and actions of the first node in the queue.

        if(currentNodeState in alreadyVisited): #check if current state is already visited
            continue

        if problem.isGoalState(currentNodeState): #check if cuurent state is goal state, if yes return the list of actions to reach this state.
            return currentNodeActions

        alreadyVisited.add(currentNodeState) #append current state to already visited set.

        for state, action, cost in problem.getSuccessors(currentNodeState): #Iterate for the successor states.

            if(state in alreadyVisited): #check if state is already visited.
                continue

            frontier.push((state, currentNodeActions+[action])) #push the successor states and appended actions to the queue.
    #util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    frontier = util.PriorityQueue() #Create a Priority Queue for the frontier.

    frontier.push((problem.getStartState(),[],0),0)  #push the start state, the empty list of actions and the cost in the frontier.

    alreadyVisited = set() #create an empty set of already visited states.

    while not frontier.isEmpty(): #check if frontier is not empty.

        currentNodeState, currentNodeActions, currentCost = frontier.pop() #store the current state, list of actions and cost of the node from frontier,
        
        if(currentNodeState in alreadyVisited): #check if already visited state.
            continue
        
        if problem.isGoalState(currentNodeState): #Check if goal state.
            return currentNodeActions
        
        alreadyVisited.add(currentNodeState) #append to already visited set.
        
        for state, action, cost in problem.getSuccessors(currentNodeState): #iterate for the successsor states.
        
            if(state in alreadyVisited): #check if state is already visited.
                continue
        
            frontier.push((state, currentNodeActions+[action], currentCost+cost),currentCost+cost) #store the successor states, appended actions and the appended cost in the queue.
            
    #util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    frontier = util.PriorityQueue() #Create a Priority Queue for frontier.
    
    frontier.push((problem.getStartState(),[],0),0) #push the start state, the empty list of actions, and the cost into the frontier.

    alreadyVisited = set() #create an empty set of already visited states.

    while not frontier.isEmpty(): #Check if frontier is not empty.
        
        currentNodeState, currentNodeActions, currentCost = frontier.pop() #store current state, list of actions and cost of the node from the queue.
        
        if(currentNodeState in alreadyVisited): #check if already visited.
            continue
        
        if problem.isGoalState(currentNodeState): #check if goal state is reached.
            return currentNodeActions
        
        alreadyVisited.add(currentNodeState) #append to set of already visited states.
        
        for state, action, cost in problem.getSuccessors(currentNodeState): #iterate for successor nodes, actions and cost.
        
            if(state in alreadyVisited): #check if already visited.
                continue
        
            heuristicValue = heuristic(state, problem) #calculate the heurestic
        
            frontier.push((state, currentNodeActions+[action], currentCost+cost),currentCost+cost+heuristicValue) #push the successor state, appended actions and cost with the heuristic to frontier.
    
    #util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
