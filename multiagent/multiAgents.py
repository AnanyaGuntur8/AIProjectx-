# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent
from pacman import GameState

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState: GameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState: GameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        #gettingthe new food list for new food 
        listOfFood = newFood.asList()
        
     #the influence of the mod state
# so keeping track of the score
        scoreMod = 0
         #if for wanting ot move closer to food 
         #this wil see if food exists in the listOfFood 
         #and use the min rom the manhat distance
         #then add 1 over the manhattan distance to make sure htat it's effience
         #want hte highest food score for the shortest distance
         #using the new position and food
        if listOfFood:
            
            #findng the min food distance 
            minFoodDistance = min([util.manhattanDistance(newPos, food) for food in listOfFood])
            #doing the last sptep
            scoreMod += 1.0 / (minFoodDistance + 1)

    # being too close to the ghost which is super bad
    #if the ghost is scared then it's good to be close to it
    #if the ghost is not scared then it's bad to be close to it
    #so we will use the scared time to determine the score
    #if the ghost is active then there is STRONG PENATLTY like 100 for being to close 
     #if ur neear it by a lil then it's a small penaly-.> sjust to make sure that the model knows the penalties
        for ghost, scaredTime in zip(newGhostStates, newScaredTimes):

#make a variable for the distance of the ghosts to keep track 
#this is going to the basis of the penalies 
#using the manahtidstance is easier. 

            distanceOfGhost = util.manhattanDistance(newPos, ghost.getPosition())
            if scaredTime == 0:  # If the ghost is active
                if distanceOfGhost < 2:
                    #so the strong penalty 
                    scoreMod -= 100  
                else:
                    #make sure taht's like it's like 1-10 and ALSO SUBTRACTION 
                    #DO NOT ADD
                    #small penarlty of like 10 if you are near the ghost 
                    scoreMod -= 10 / (distanceOfGhost + 1) 
            else:
                # Reward for moving closer to scared ghosts
                scoreMod += 10.0 / (distanceOfGhost + 1)
#making sure that the the pacman will recieve penalty if there is a stop 
#this is to make sure that the model knows that it's bad to stop
        if action == Directions.STOP:
            scoreMod -= 10
            #out of the function 
        #modScore  = hte oritifoonal score +the new score

        modScore = successorGameState.getScore() + scoreMod
        return modScore

def scoreEvaluationFunction(currentGameState: GameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
#definiton from: https://brilliant.org/wiki/minimax/ 


# minimax is a decision rule used to minimize the worst-case potential loss; in other words, 
# a player considers all of the best opponent responses to his strategies, and 
# selects the strategy such that the opponent's best strategy gives a payoff as large as possible.

#so i have ot find the state, depth, and agentindex
# agentIndex = 0 means Pacman, ghosts are >= 1

        def minimaxFunction(state, depth, indOfPac):
            if state.isWin() or state.isLose() or depth == self.depth:
                #returning th esel f funciton for th state


                #can you check this because im not so sure. 

                #it's good, I just fixed the state lose. make sure tht the state is losign 

                return self.evaluationFunction(state)

#this is a lost of legal acitoan that take in the agent's indext
            action = state.getLegalActions(indOfPac)
            if not action:
                #if the 
                return self.evaluationFunction(state)

#next stepts of the pacman which is agent 
#want to find the remainder of the next step so indOfAPc+1 bcuase it's one less and mod it by the number of agents

            nexAgent = (indOfPac + 1) % state.getNumAgents()
            nexDep = depth + 1 if nexAgent == 0 else depth
#so this is pacman's turn to maximize the scoreboard

#Do the ghost tunr which is to minimize it , 
#it's the same thing but min insetead of max
            if indOfPac == 0: 
                return max(minimaxFunction(state.generateSuccessor(indOfPac, action), nexDep, nexAgent) for action in action)
            else:  
                #returning the min funciton from the minimax 
                #through each action 

                return min(minimaxFunction(state.generateSuccessor(indOfPac, action), nexDep, nexAgent) for action in action)

        legalMoves = gameState.getLegalActions(0)

        #the best
        optScore = float('-inf')
        #accoding to the bestscore meka the bestAction
        optAction = None

        for action in legalMoves:
            score = minimaxFunction(gameState.generateSuccessor(0, action), 0, 1)
            if score > optScore:
                optScore = score
                optAction = action

        return optAction
        util.raiseNotDefined()
#DONE WITH 2 WOOooo

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """
    #i dont like alphabeta pruing 

#def: https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/
#optimization technique for the minimax algorithm. It reduces the computation time

#pseudo code: 
# function minimax(node, depth, isMaximizingPlayer, alpha, beta):

#     if node is a leaf node :
#         return value of the node
    
#     if isMaximizingPlayer :
#         bestVal = -INFINITY 
#         for each child node :
#             value = minimax(node, depth+1, false, alpha, beta)
#             bestVal = max( bestVal, value) 
#             alpha = max( alpha, bestVal)
#             if beta <= alpha:
#                 break
#         return bestVal

#     else :
#         bestVal = +INFINITY 
#         for each child node :
#             value = minimax(node, depth+1, true, alpha, beta)
#             bestVal = min( bestVal, value) 
#             beta = min( beta, bestVal)
#             if beta <= alpha:
#                 break
#         return bestVal

#ref for the project-> taken by the geeks for geeks website
    def getAction(self, gameState: GameState):

#ok for this follow the spusodoode
        def alphaBeta(state, depth, agentIndex, alpha, beta):
            if state.isWin() or state.isLose() or depth == self.depth:
                #i updated the isWin and isLose function 
                #retun the eval of the state which you did already 

                return self.evaluationFunction(state)#
            #FIX QUESTION 2 thn misundersttod q

            Leg_actions = state.getLegalActions(agentIndex)
            if not Leg_actions:
                return self.evaluationFunction(state)
#hahah get it nexus LMAO
            nexusAgent = (agentIndex + 1) % state.getNumAgents()

            #
            
            if nexusAgent == 0:
                 nexusDepth = depth + 1 
            else:
                nexusDepth = depth


            if agentIndex == 0:  
                value = float('-inf')


                for action in Leg_actions:
                    #in every legal action then run the max vlaue funciton 
                    value = max(value, alphaBeta(state.generateSuccessor(agentIndex, action), nexusDepth, nexusAgent, alpha, beta))
                    if value > beta:
                        #returnt the value if val is greater
                        return value
                    
                    #alpsh wuld be the max of either the alpha value or the value 

                    alpha = max(alpha, value)

                return value
            else:  
                value = float('inf')
                for action in Leg_actions:
#lmao you coppies and pasted here
                    #Do the ghost tunr which is to minimize it , 
#it's the same thing but min insetead of max
                    value = min(value, alphaBeta(state.generateSuccessor(agentIndex, action), nexusDepth, nexusAgent, alpha, beta))

                    #same thing here but replace beta with aplaph 
                    if value < alpha:
                        return value
                    beta = min(beta, value)
                return value

        legalMoves = gameState.getLegalActions(0)
        optScore = float('-inf')
        optAction = None
        alpha = float('-inf')
        beta = float('inf')

#basically the same thingb ut here reutnr the optAction using hte alphaBeta Pruning

        for action in legalMoves:
            score = alphaBeta(gameState.generateSuccessor(0, action), 0, 1, alpha, beta)
            if score > optScore:
                optScore = score
                optAction = action
                #alpha would be the max of the score and alpha again hte same thign as minimax
            alpha = max(alpha, score)

        return optAction
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """
#def from the geeks for geeks: https://www.geeksforgeeks.org/expectimax-algorithm-in-game-theory/

#ps code: 
# function Expectimax(state, depth, isMaxPlayer):
#     if depth == 0 or terminal(state):
#         return utility(state)
    
#     if isMaxPlayer:
#         bestValue = -∞
#         for each action in actions(state):
#             value = Expectimax(result(state, action), depth - 1, False)
#             bestValue = max(bestValue, value)
#         return bestValue
#     elif isMinPlayer:
#         bestValue = ∞
#         for each action in actions(state):
#             value = Expectimax(result(state, action), depth - 1, True)
#             bestValue = min(bestValue, value)
#         return bestValue
#     else:
#         expectedValue = 0
#         for each outcome, probability in outcomes(state):
#             value = Expectimax(result(state, outcome), depth - 1, isMaxPlayer)
#             expectedValue += probability * value
#         return expectedValue


    def getAction(self, gameState: GameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***" 

    #follow the psudocode: need state, depth and agentIndex
    #depth is the number of moves left, agentIndex is the index of the current agent
    #isMaxPlayer is True if the current agent is the max player, False otherwise

        def expectimax(state, depth, agentIndex):
            if state.isWin() or state.isLose() or depth == self.depth:
                return self.evaluationFunction(state)
#same thing aas the previosu one, make a directory of like the one before
#store the legal actions in a var named actiosn
            act = state.getLegalActions(agentIndex)
            if not act:
                #false conditions
                return self.evaluationFunction(state)
            
#next stepts of the pacman which is agent 
#want to find the remainder of the next step so indOfAPc+1 bcuase it's one less and mod it by the number of agents
#just make sure to follow the psudeocode. 
            netAgent = (agentIndex + 1) % state.getNumAgents()
            netDepth = depth + 1 if netAgent == 0 else depth

            #im beginning to think tha all of these kinda follow the same format 
            #if it's the max player, then we want to find the max value of the next
            #if it's the min player, then we want to find the min value of the next
            if agentIndex == 0: 
                #pac has the max value 
                return max(expectimax(state.generateSuccessor(agentIndex, action), netDepth, netAgent) for action in act)
            else: 
                #tip, DO NOT AdD THE MIN VLAUE HERE
                #and follow thorugh with every action in act
                values = [expectimax(state.generateSuccessor(agentIndex, action), netDepth, netAgent) for action in act]
                #sinc eht eghosts decide to be craxy and act randomly then 
                return sum(values) / len(values) #bruh python is way easier tf
            #got me not liking javaaaa

        legalMoves = gameState.getLegalActions(0)
        #considered a float to initialize it properly 

        optScore = float('-inf')
        #initalze the act to none rn 

        optAct = None

        for action in legalMoves:
            score = expectimax(gameState.generateSuccessor(0, action), 0, 1)

            #determinng the values 
            if score > optScore:
                optScore = score
                optAct = action

        return optAct
    #ALMOST DONE WOOOOO
    #just need to make the minimax function and the evaluation function
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState: GameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: what I intend to do is to evaluate the pac's current state by m
    aximizing the number of pellets left and the number of food pellets left
    and minimizing the number of ghosts left and the number of capsules left
    also by rewarding the movement towards scared ghosts to gain poiins and vise versa by 
    peanilizing if they come too close to active and scary ghosts to make sure that the pac survives

    """
    "*** YOUR CODE HERE ***"

    #
    scorOfPAc = currentGameState.getScore()

    # first find pac's position
#find the  food grid and distance to nearest food
#get the ghost states and timers of being scared because we wantt o ensure the penality
# #want the pac to eat as much powerPel as poossible so encourage more food by offerin  
    pacmanPos = currentGameState.getPacmanPosition()
    listOfFood = currentGameState.getFood().asList()
    disToFood = min([manhattanDistance(pacmanPos, food) for food in listOfFood]) if listOfFood else 1

   
    stateOFGhost = currentGameState.getGhostStates()
    #sTImes and store them in the scared Ghost
    scaredGhost = [ghostState.scaredTimer for ghostState in stateOFGhost]
    ghostDistances = [manhattanDistance(pacmanPos, ghost.getPosition()) for ghost in stateOFGhost]
    evalFinalScore = scorOfPAc
    evalFinalScore += 10.0 / disToFood

    #iterate thorug the disance of ghsots and if there's a scared ghost then give a good reward 500 WOo
    #but if it's an ACTIVE ghost then -20 make sure that the pac doiesnt go there
    for i, distance in enumerate(ghostDistances):
        if scaredGhost[i] > 0:
            # Reward for approaching scared ghosts
            evalFinalScore += 500.0 / (distance + 1)
        else:
            if distance > 0:
                evalFinalScore -= 20.0 / distance
    evalFinalScore -= 4 * len(listOfFood)

#the fewer the better
    pellets = currentGameState.getCapsules()
    evalFinalScore -= 15 * len(pellets)




#return the final score when done iwht everythig 

    return evalFinalScore
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
