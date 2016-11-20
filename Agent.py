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

		while isHit(target) != True:

			target = randomShot()
			oldCoords.push(target)

		#Next we would check the nearby coordinates after we land a hit

	#the best algorithim of the three, using Q-learning and prob reasoning
	def ProbReasoning(self):

	#other functions to create

	#updates state of board after a move is made
	def updateBoard(self):

	#Q-learning functions
	def computeActionsFromQValues(self):
	def getQValue(self):
	def getAction(self):


