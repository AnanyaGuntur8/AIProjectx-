# analysis.py
# -----------
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


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

#discount: care about the future rewards
# higher discount means higher want for future rewards, lower is immediate

#noise: number of unplanned actions 
#higher means that the actions may not be planned to more caution 
#lower means that the actions are more planned

#reward: living reward
#higher means that the living reward is higher, meaning wants to stay alive
#lower means that it wants to exit the game quickly 
def question2a():
    """
      Prefer the close exit (+1), risking the cliff (-10).
    """
    # discouts are more of an average here since the problem doesnt really state it 
    # noise is, has to be very planned  because riksing the cliff so anywhere from 0.01 - 0.09 choose the intermediate
    # since close exit then the game is ended quickly 
    #
    answerDiscount = 0.4
    answerNoise = 0.03
    answerLivingReward = -1
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question2b():
    """
      Prefer the close exit (+1), but avoiding the cliff (-10).
    """
    # discouts are more of an average here since the problem doesnt really state it 
    # noise is, can be slightly unplanned since avoiding the the clift
    # since close exit then the game is ended quickly 
    #
    answerDiscount = 0.5
    answerNoise = 0.2
    answerLivingReward = -1
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question2c():
    """
      Prefer the distant exit (+10), risking the cliff (-10).
    """
     # discouts: prefering the +!0 menaning a need for future rewards 
    # noise is, has to be very planned  because riksing the cliff so anywhere from 0.01 - 0.09 choose the intermediate
    # the game is ended quickly 
    #
    answerDiscount = 0.9
    answerNoise = 0.04
    answerLivingReward = -1
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question2d():
    """
      Prefer the distant exit (+10), avoiding the cliff (-10).
    """
     # discouts: prefering the +10 menaning a need for future rewards so closer to 1
    # noise is, has to be somewhat unplanned to avoid the cliff
    # the game is ended quickly ("exit")
    #
    answerDiscount = 0.8
    answerNoise = 0.3
    answerLivingReward = -1
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question2e():
    """
      Avoid both exits and the cliff (so an episode should never terminate).
    """
    # discouts: prefering the +10 menaning a need for future rewards so closer to 1
    # noise is, has to be somewhat unplanned to avoid the cliff
    # the game shuld never terminate so that means that the living rewards is higher 
    #
    answerDiscount = 0.9
    answerNoise = 0.3
    answerLivingReward = 10
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

if __name__ == '__main__':
    print('Answers to analysis questions:')
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print('  Question %s:\t%s' % (q, str(response)))
