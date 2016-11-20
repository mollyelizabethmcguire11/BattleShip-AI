# This will be where the logic for the Battleship agent will be.
# Currently, we want to create three different playing styles for the agent
#
# 	1. Random Shooting - the agent selects a target randomly
#
#	2. Hunt/Target strategy - The agent begins by shooting randomly, hunting a ship.
#	   when a ship is hit, the agent begins targeting that ship by searching the locations near the hit.
#
#	3. Probabolostic Reasoning - Aim for the most probable locations. This will determine where a ship can fit
#	   on the board based on the current state, given the board size and the number of shots taken.
#
# This logic is based off information found at http://www.datagenetics.com/blog/december32011/