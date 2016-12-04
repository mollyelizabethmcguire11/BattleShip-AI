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
	def __init__(self):

	#return if a given shot hits or misses
	def isHit(self, coords):

		#logic to be determined...
		return true

	#random shot function. Used for first and second strategy.

	def shoot(self, xcoord, ycoord):
		#this would integrate with the actual game to take the shot
		#return true if hit was made
	def randomShot(self):

		#this is the general idea. Integration with the actual battleship game will let us test
		#when this function is called, the return value should be checked against already target locations
		xcoord = randit(0, WIDTH - 1)
		ycoord = randit(0, HEIGHT - 1)

		return (xcoord, ycoord)

	#function for hunt/target algorithm. Used for second strategy.
	def huntTarget(self):

		#stack of all shots fired
		oldCoords = []

		#Will take random shots until a hit is made

		target = randomShot()
		oldCoords.push(target)

		while shoot(target) != True and target not in oldCoords:

			target = randomShot()

			if target not in oldCoords:
				oldCoords.push(target)

		#Next we would check the nearby coordinates after we land a hit
		currentTarget = target

		while shoot(target) == True:
			
			temp = target

			target.ycoord = target.ycoord + 1
			
			if target not in oldCoords:
				oldCoords.push(target)

			else:
				target = temp

		target = currentTarget	

		while shoot(target) == True:

			temp = target

			target.ycoord = target.ycoord - 1

			if target not in oldCoords:
				oldCoords.push(target)

			else:
				target = temp

		target = currentTarget	


		while shoot(target) == True:

			temp = target

			target.xcoord = target.xcoord + 1

			if target not in oldCoords:
				oldCoords.push(target)

			else:
				target = temp

		target = currentTarget	

		while shoot(target) == True:

			temp = target 

			target.xcoord = target.xcoord - 1
			
			if target not in oldCoords:
				oldCoords.push(target)

			else:
				target = temp




	#the best algorithim of the three, using Q-learning and prob reasoning
	def ProbReasoning(self):

	#other functions to create

	#updates state of board after a move is made
	def updateBoard(self):

	#Q-learning functions

	#computes the best action based on the state and current qValue
	def computeActionsFromQValues(self):


	def getQValue(self):

	def update_qvalue(self,position, isHit,distance,counter):

		#Code based on code from the Berkley Pacman projects
        """
          The parent class calls this to observe a
          state = action => nextState and reward transition.
          You should do your Q-Value update here
          NOTE: You should never call this function,
          it will be called on your behalf
        """
        if counter == 0:
            reward = 0

        elif isHit:
                reward=0.5
        else:
                reward=0.1
        
        #Function for Q value iteration    
        #sample = reward + self.discount * max(self.getQValue() 
        if isHit:
            self.qValuesOfhit[distance] = (1-self.alpha) * self.getQValue(distance,isHit) + self.alpha * sample
        else:
            self.qValuesOfMiss[distance] = (1-self.alpha) * self.getQValue(distance,isHit) + self.alpha * sample

	def getAction(self):


