# This will be where the logic for the Battleship agent will be.
# Currently, our goal is to create three different playing styles for the agent
#
# 	1. Random Shooting - the agent selects a target randomly
#
#	2. Hunt/Target strategy - The agent begins by shooting randomly, hunting a ship.
#	   when a ship is hit, the agent begins targeting that ship by searching the locations near the hit.
#
#	3. Probabalistic Reasoning - Aim for the most probable locations. This will determine where a ship can fit
#	   on the board based on the current state, given the board size and the number of shots taken.
#
# This logic is based off information found at http://www.datagenetics.com/blog/december32011/

import random, util.py

#Globals to be used
HEIGHT = 10
WIDTH = 10
#Ships size constants
CARRIER = 5
BATTLESHIP = 4
SUBMARINE = 3
CRUISER = 3
DESTROYER = 2

def Agent:

	#initialize agent. Arguments to be determined...
	def __init__(self, alpha=0.3, gamma=0.9, epsilon=0.2):

		#learning rate
		self.alpha = float(alpha)

		#discount factor
		self.discount = float(gamma)

		#epsilon
		self.epsilon = float(epsilon)

		self.qValues = util.Counter()
		
		#reward for hitting a target
		#self.hitReward = 1

		#Penalty for missing
		#self.missReward = -.5

		#All actions taken
		self.shotsFired = []

	
	def getRemainingActions(self, shotsFired):

		remainingActions = []

		for i in range(WIDTH):
			for j in range(HEIGHT):
				if shotsFired[i][j] != None:
					remainingActions.append((i,j))

		return remainingActions

	#function for hunt/target algorithm. Used for second strategy.
	# def huntTarget(self):

	# 	#stack of all shots fired
	# 	oldCoords = []

	# 	#Will take random shots until a hit is made

	# 	target = randomShot()
	# 	oldCoords.push(target)

	# 	while shoot(target) != True and target not in oldCoords:

	# 		target = randomShot()

	# 		if target not in oldCoords:
	# 			oldCoords.push(target)

	# 	#Next we would check the nearby coordinates after we land a hit
	# 	currentTarget = target

	# 	while shoot(target) == True:
			
	# 		temp = target

	# 		target.ycoord = target.ycoord + 1
			
	# 		if target not in oldCoords:
	# 			oldCoords.push(target)

	# 		else:
	# 			target = temp

	# 	target = currentTarget	

	# 	while shoot(target) == True:

	# 		temp = target

	# 		target.ycoord = target.ycoord - 1

	# 		if target not in oldCoords:
	# 			oldCoords.push(target)

	# 		else:
	# 			target = temp

	# 	target = currentTarget	


	# 	while shoot(target) == True:

	# 		temp = target

	# 		target.xcoord = target.xcoord + 1

	# 		if target not in oldCoords:
	# 			oldCoords.push(target)

	# 		else:
	# 			target = temp

	# 	target = currentTarget	

	# 	while shoot(target) == True:

	# 		temp = target 

	# 		target.xcoord = target.xcoord - 1
			
	# 		if target not in oldCoords:
	# 			oldCoords.push(target)

	# 		else:
	# 			target = temp


	#computes the best action based on the state and current qValue
	def computeActionsFromQValues(self):


	def getQValue(self):

	def update_qvalue(self,isHit,target,counter):

		#Code based on code from the Berkley Pacman projects
        """
          The parent class calls this to observe a
          state = action => nextState and reward transition.
          You should do your Q-Value update here
          NOTE: You should never call this function,
          it will be called on your behalf
        """
        legalActions = self.getRemainingActions(self.shotsFired)

        if counter == 0:
            reward = 0

        elif isHit:
                reward=0.5
        else:
                reward=0.1
        
        #Function for Q value iteration    
        #sample = reward + self.discount * max(self.getQValue() 
        #if isHit:

        sample = reward + self.discount * max(self.getQValue(action,hitOrnot) for action in legalActions)
        self.qValues[target] = (1-self.alpha) * self.getQValue(target,isHit) + self.alpha * sample

        #else:
         #   self.qValuesOfMiss[distance] = (1-self.alpha) * self.getQValue(distance,isHit) + self.alpha * sample

	#def getAction(self):

