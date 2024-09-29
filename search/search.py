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
from game import Directions
from typing import List

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




def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
  """
    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))
  
    "*** YOUR CODE HERE ***"
    # Stack to store the nodes to be visited, DFS is LIFO
    stack = util.Stack()
    # Set to store the visited nodes
    visited_Nodes = set()
    # Start state of the first node
    starting_State = problem.getStartState()
    # Stack cannot be null, so we need to add the starting state and null list of directions to the stack
    stack.push((starting_State,[]))
    while not stack.isEmpty():
        # pop the top node from the stack, separating the state and directions
        state_curr, directions  = stack.pop()
        if problem.isGoalState(state_curr):
            return directions # return the directions of the goal state
        # if the state is not visited before
        if state_curr not in visited_Nodes:
            # mark the state as visited
            visited_Nodes.add(state_curr)
            # get the successors of the current state
            successors = problem.getSuccessors(state_curr)
            # for each successor
            for successor, action, _ in successors: 
                # push the successor to the stack, need to add in action as well
                if successor not in visited_Nodes:
                    stack.push((successor, directions + [action])) # adding the action to the directions list
    return []
    #util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # Queue to store the nodes to be visited, BFS is FIFO
    queue = util.Queue()
    # Set to store the visited nodes
    visited_Nodes = set()
    # Start state of the first node
    starting_State = problem.getStartState()
    # Queue cannot be null, so we need to add the starting state and null list of directions to the queue
    queue.push((starting_State,[]))
    while not queue.isEmpty():
        # dequeue the top node from the queue, separating the state and directions
        state_curr, directions  = queue.pop()
        if problem.isGoalState(state_curr):
            return directions # return the directions of the goal state
        # if the state is not visited before
        if state_curr not in visited_Nodes:
            # mark the state as visited
            visited_Nodes.add(state_curr)
            # get the successors of the current state
            successors = problem.getSuccessors(state_curr)
            # for each successor
            for successor, action, _ in successors:
                #enqueue the successor to the queue, need to add in action as well
                if successor not in visited_Nodes:
                    queue.push((successor, directions + [action])) # adding the action to the directions list
    return []

    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # Priority Queue for the uniform cost 
    pq = util.PriorityQueue()
    # Set to store the visited nodes
    visited_Nodes = set()
    # Start state of the first node
    starting_State = problem.getStartState()
    # Queue cannot be null, so we need to add the starting state and null list of directions and cost to the queue
    pq.push((starting_State, [], 0), 0)
    while not pq.isEmpty(): 
        # dequeue the top node from the pq, separating the state, directions and cost
        state_curr, directions, cost = pq.pop()
        if problem.isGoalState(state_curr):
            return directions # return the directions of the goal state
        if state_curr not in visited_Nodes:
            # mark the state as visited
            visited_Nodes.add(state_curr)
            # get the successors of the current state
            successors = problem.getSuccessors(state_curr)
            # for each successor
            for successor, action, cost_of_step in successors:
                #e nqueue the successor to the queue, need to add in action as well
                if successor not in visited_Nodes:
                    total_cost = cost_of_step+ cost 
                    pq.push((successor, directions + [action], total_cost), total_cost) # adding the action to the direction, and save the total cost

    return []
    util.raiseNotDefined()

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # A* search is similar to uniform cost search but with a heuristic function
    # Priority Queue for the uniform cost
    pq = util.PriorityQueue()
    # Set to store the visited nodes
    visited_Nodes = set()
    # Dictionary to store the best cost (g()) to reach each state
    best_cost = {}
    # Start state of the first node
    starting_State = problem.getStartState()
    # Best cost of Start State
    best_cost[starting_State] = 0 # g() = 0
    # Queue cannot be null, so we need to add the starting state and null list of directions and cost to the queue
    pq.push((starting_State, [], 0), 0)
    while not pq.isEmpty():
        # dequeue the top node from the pq, separating the state, directions and cost
        state_curr, directions, cost = pq.pop()
        if problem.isGoalState(state_curr):
            return directions  # return the directions of the goal state
        if state_curr in visited_Nodes and cost > best_cost[state_curr]:
            continue
        # mark the state as visited
        visited_Nodes.add(state_curr)
        # get the successors of the current state
        successors = problem.getSuccessors(state_curr)
        # for each successor
        for successor, action, cost_of_step in successors:
            new_cost = cost + cost_of_step  # UCS -> g() = current path cost + cost of step
            # enqueue the successor to the queue, need to add in action as well
            if successor not in best_cost or new_cost < best_cost[successor]: # if the new cost is less than the best cost or not visited before
                heuristic_cost = heuristic(successor, problem) # h() = heuristic cost
                total_cost = new_cost + heuristic_cost  # f() = g() + h() (new cost + heuristic)
                best_cost[successor] = new_cost
                pq.push((successor, directions + [action], new_cost), total_cost) # adding the action to the direction, and save the total cost
    return []
    #util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
