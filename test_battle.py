# Code for the battleship game obtained from http://code.activestate.com/recipes/578836-the-game-of-battleships-in-python/

import copy, random

def print_board(s,board):

	# WARNING: This function was crafted with a lot of attention. Please be aware that any
	#          modifications to this function will result in a poor output of the board 
	#          layout. You have been warn. 

	#find out if you are printing the computer or user board
	player = "Computer"
	if s == "u":
		player = "User"
	
	print "The " + player + "'s board look like this: \n"

	#print the horizontal numbers
	print " ",
	for i in range(10):
		print "  " + str(i+1) + "  ",
	print "\n"

	for i in range(10):
	
		#print the vertical line number
		if i != 9: 
			print str(i+1) + "  ",
		else:
			print str(i+1) + " ",

		#print the board values, and cell dividers
		for j in range(10):
			if board[i][j] == -1:
				print ' ',	
			elif s == "u":
				print board[i][j],
			elif s == "c":
				if board[i][j] == ('\x1b[0;31;40m' + "*" + '\x1b[0m') or board[i][j] == ('\x1b[0;32;40m' + 'X' + '\x1b[0m'):
					print board[i][j],
				else:
					print " ",
			
			if j != 9:
				print ('\x1b[1;37;44m' + " | " + '\x1b[0m'),
		print
		
		#print a horizontal line
		if i != 9:
			print ('\x1b[1;37;44m' + "   ----------------------------------------------------------" + '\x1b[0m')
		else: 
			print 


def computer_place_ships(board,ships):

	for ship in ships.keys():
	
		#genreate random coordinates and vlidate the postion
		valid = False
		while(not valid):

			x = random.randint(1,10)-1
			y = random.randint(1,10)-1
			o = random.randint(0,1)
			if o == 0: 
				ori = "v"
			else:
				ori = "h"
			valid = validate(board,ships[ship],x,y,ori)

		#place the ship
		print "Computer placing a/an " + ship
		board = place_ship(board,ships[ship],ship[0],ori,x,y)
	
	return board


def place_ship(board,ship,s,ori,x,y):

	#place ship based on orientation
	if ori == "v":
		for i in range(ship):
			board[x+i][y] = s
	elif ori == "h":
		for i in range(ship):
			board[x][y+i] = s

	return board
	
def validate(board,ship,x,y,ori):

	#validate the ship can be placed at given coordinates
	if ori == "v" and x+ship > 10:
		return False
	elif ori == "h" and y+ship > 10:
		return False
	else:
		if ori == "v":
			for i in range(ship):
				if board[x+i][y] != -1:
					return False
		elif ori == "h":
			for i in range(ship):
				if board[x][y+i] != -1:
					return False
		
	return True

def v_or_h():

	#get ship orientation from user
	while(True):
		user_input = raw_input("vertical or horizontal (v,h) ? ")
		if user_input == "v" or user_input == "h":
			return user_input
		else:
			print "Invalid input. Please only enter v or h"


def make_move(board,x,y):
	
	#make a move on the board and return the result, hit, miss or try again for repeat hit
	if board[x][y] == -1:
		return "miss"
	elif board[x][y] == ('\x1b[0;31;40m' + "*" + '\x1b[0m') or board[x][y] == ('\x1b[0;32;40m' + 'X' + '\x1b[0m'):
		return "try again"
	else:
		return "hit"


def computer_move(board):
	
	#generate user coordinates from the user and try to make move
	#if move is a hit, check ship sunk and win condition
	while(True):
		x = random.randint(1,10)-1
		y = random.randint(1,10)-1
		res = make_move(board,x,y)
		if res == "hit":
			print "Hit at " + str(x+1) + "," + str(y+1)
			check_sink(board,x,y)
			board[x][y] = ('\x1b[0;32;40m' + 'X' + '\x1b[0m')
			if check_win(board):
				return "WIN"
		elif res == "miss":
			print "Sorry, " + str(x+1) + "," + str(y+1) + " is a miss."
			board[x][y] = ('\x1b[0;31;40m' + "*" + '\x1b[0m')

		if res != "try again":
			
			return board
	
def check_sink(board,x,y):

	#figure out what ship was hit
	if board[x][y] == "A":
		ship = "Aircraft Carrier"
	elif board[x][y] == "B":
		ship = "Battleship"
	elif board[x][y] == "S":
		ship = "Submarine" 
	elif board[x][y] == "D":
		ship = "Destroyer"
	elif board[x][y] == "P": 
		ship = "Patrol Boat"
	
	#mark cell as hit and check if sunk
	board[-1][ship] -= 1
	if board[-1][ship] == 0:
		print ship + " Sunk"
		

def check_win(board):
	
	#simple for loop to check all cells in 2d board
	#if any cell contains a char that is not a hit or a miss return false
	for i in range(10):
		for j in range(10):
			if board[i][j] != -1 and board[i][j] != ('\x1b[0;31;40m' + "*" + '\x1b[0m') and board[i][j] != ('\x1b[0;32;40m' + 'X' + '\x1b[0m'):
				return False
	return True

def main():

	#types of ships
	ships = {"Aircraft Carrier":5,
		     "Battleship":4,
 		     "Submarine":3,
		     "Destroyer":3,
		     "Patrol Boat":2}

	#setup blank 10x10 board
	board = []
	for i in range(10):
		board_row = []
		for j in range(10):
			board_row.append(-1)
		board.append(board_row)

	#setup board
	user_board = copy.deepcopy(board)

	#add ships as last element in the array
	user_board.append(copy.deepcopy(ships))

	#ship placement
	user_board = computer_place_ships(user_board,ships)
	count = 0
	#game main loop
	while(1):

		#computer move
		user_board = computer_move(user_board)
		count = count + 1
		#check if computer move
		if user_board == "WIN":
			print "GAME OVER"
			print "Move count :",count,"."
			quit()
			
		#display user board
		print_board("u",user_board)
		raw_input("To end computer turn hit ENTER")
	
if __name__=="__main__":
	main()
