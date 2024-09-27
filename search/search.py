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
    #defininign my variables
    # Create a stack to store the nodes to be visited
    stack = util.Stack()
    # Create a set to store the visited nodes
    visited_Nodes = set()
    starting_State = problem.getStartState() #getting the start state of the first node
    #Cannot pop anthing from the stack unless there is anything in the start state 
    stack.push((starting_State,[])) #seeting an empty array to add it in  
    empty_arr = []
    #if the stack is not empty
    while not stack.isEmpty():
        #pop the top node from the stack
        state_curr, direction  = stack.pop()
        if problem.isGoalState(state_curr):
            return direction
        #returning the direction of the goal state 
        #if the state is not visited before
        if state_curr not in visited_Nodes:
            #mark the state as visited
            visited_Nodes.add(state_curr)
            #get the successors of the current state
            successors = problem.getSuccessors(state_curr)
            #for each successor
            for successor, action, _ in successors: 
                #push the successor to the stack, need to add in action as well
                if successor not in visited_Nodes:
                    stack.push((successor, direction + [action]))

    return empty_arr


    
    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue = util.Queue()
    visited_Nodes = set()

    #adding it in queue
    starting_State = problem.getStartState() #getting the start state of the problem
    queue.push((starting_State,[])) #seeting an empty array to add it in
    empty_arr = []
    #if the queue is not empty
    while not queue.isEmpty():
        #dequeue the top node from the queue
        state_curr, direction  = queue.pop()
        if problem.isGoalState(state_curr):
            return direction
        #returning the direction of the goal state
        #if the state is not visited before
        if state_curr not in visited_Nodes:
            #mark the state as visited
            visited_Nodes.add(state_curr)
            #get the successors of the current state
            successors = problem.getSuccessors(state_curr)
            #for each successor
            for successor, action, _ in successors:
                #enqueue the successor to the queue, need to add in action as well
                if successor not in visited_Nodes:
                    queue.push((successor, direction + [action]))
    return empty_arr

    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #making a pq for the uniform cost 
    pq = util.PriorityQueue()
    #adding the start state to the pq
    #making a visited notes set 
    visited_Nodes = set()
    #adding the start state to the visited nodes
    starting_State = problem.getStartState()
    pq.push((starting_State, [], 0), 0)
    #making a dictionary to store the cost of each node
    empty_arr =[]
    #if the pq is not empty
    while not pq.isEmpty(): 
        #dequeue the top node from the pq
        state_curr, direction, cost = pq.pop()
        #if the state is the goal state
        if problem.isGoalState(state_curr):
            return direction
        if state_curr not in visited_Nodes:
            #mark the state as visited
            visited_Nodes.add(state_curr)
            #get the successors of the current state
            successors = problem.getSuccessors(state_curr)
            #for each successor
            for successor, action, cost_of_step in successors:
                #enqueue the successor to the queue, need to add in action as well
                if successor not in visited_Nodes:
                    total_cost = cost_of_step+ cost 
                    pq.push((successor, direction + [action], total_cost), total_cost)

    return empty_arr
   


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
    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
