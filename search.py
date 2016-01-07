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

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    # Initialize variables
    fringe = util.Stack()
    explored = []
    fringeStates = []   # Keeps track of current states on fringe

    # Expand starting state
    startNode = problem.getStartState()
    # Push first node onto fringe
    #Each entry on fringe is tuple of form (state, [actions taken])
    fringe.push((startNode, []))
    fringeStates.append(startNode)
    # Search loop
    while(1):
        if fringe.isEmpty():# If no more nodes in fringe there is no solution
            return False 
        # Pop a node from fringe and extract the state and action
        node = fringe.pop()
        fringeState = node[0]
        actions = node[1]
        # Remove state from current states check
        fringeStates.remove(fringeState)
        # Return if a goal state
        if problem.isGoalState(fringeState):
            return actions
        # Add to explored
        explored.append(fringeState)
        # Generate children of node
        for child in problem.getSuccessors(fringeState):
            # Extract state and action
            state = child[0]
            action = child[1]
            act = [x for x in actions]
            # Check that node is not explored
            if state not in explored: 
                # Add action and push node onto fringe
                act.append(action)
                fringe.push((state, act))
                fringeStates.append(state)

                    

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # Initialize variables
    fringe = util.Queue()
    explored = []
    fringeStates = []   # Keeps track of current states on fringe

    # Expand starting state
    startNode = problem.getStartState()
    # Push first node onto fringe
    #Each entry on fringe is tuple of form (state, [actions taken])
    fringe.push((startNode, []))
    fringeStates.append(startNode)
    # Search loop
    while(1):
        if fringe.isEmpty():# If no more nodes in fringe there is no solution
            return False 
        # Pop a node from fringe and extract the state and action
        node = fringe.pop()
        fringeState = node[0]
        actions = node[1]
        # Remove state from current states check
        fringeStates.remove(fringeState)
        # Return if a goal state
        if problem.isGoalState(fringeState):
            return actions
        # Add to explored
        explored.append(fringeState)
        # Generate children of node
        for child in problem.getSuccessors(fringeState):
            # Extract state and action
            state = child[0]
            action = child[1]
            act = [x for x in actions]
            # Check that node is not explored
            if state not in explored and state not in fringeStates: 
                # Add action and push node onto fringe
                act.append(action)
                fringe.push((state, act))
                fringeStates.append(state)

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # Initialize variables
    fringe = util.PriorityQueue()
    explored = []
    fringeStates = dict()

    # Expand starting state
    startNode = problem.getStartState()
    # Push first node onto fringe
    #Each entry on fringe is tuple of form (state, [actions taken]), costOfActions
    fringe.push((startNode, []), 0)
    fringeStates[startNode] = 0
    # Search loop
    while(1):
        if fringe.isEmpty():# If no more nodes in fringe there is no solution
            return False 
        # Pop a node from fringe and extract the state and action
        node = fringe.pop()
        fringeState = node[0]
        actions = node[1]

        # Return if a goal state
        if problem.isGoalState(fringeState):
            return actions

        # Add to explored
        explored.append(fringeState)

        # Generate children of node
        for child in problem.getSuccessors(fringeState):
            # print "Child: ", child
            # Extract state and action
            state = child[0]
            action = child[1]
            # print "Action: ", action
            act = [x for x in actions]
            act.append(action)
            # print "Extracted actions: ", act
            # Check that node is not explored
            if state not in explored and state not in fringeStates.keys():
                fringe.push((state, act), problem.getCostOfActions(act))
                fringeStates[state] = problem.getCostOfActions(act)
            elif state in fringeStates.keys():
                if problem.getCostOfActions(act) < fringeStates[state]:
                    # There is a lower cost path for a node. Must make a new
                    # fringe with the proper node
                    temp = util.PriorityQueue()   # Create temporary pq
                    while not fringe.isEmpty():     # Cycle through fringe
                        item = fringe.pop() 
                        if item[0][0] == state:     # find replacement
                            temp.push((state, act),problem.getCostOfActions(act))
                        else:
                            temp.push(item)
                    fringe = temp   # Renew fringe
                                    


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
