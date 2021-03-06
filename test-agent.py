
import random, util, copy

class Agent:

    #initialize agent. Arguments to be determined...
    def __init__(self, alpha=0.3, gamma=0.7):

        #learning rate
        self.alpha = float(alpha)

        #discount factor
        self.discount = float(gamma)

        self.qValues = util.Counter()

    def getRemainingActions(self, shotsFired):

        remainingActions = []
       
        for i in range(10):
            for j in range(10):
                if (i,j) not in shotsFired:
                    remainingActions.append((i,j))

        return remainingActions

    def computeActionsFromQValues(self, shotsFired, hits):

        actions = self.getRemainingActions(shotsFired)
        actValPair = util.Counter()
        qVals = []

        if len(actions) == 0:
            return None

        max_actions = []

        for action in actions:
            actValPair[action] = self.getQValue(action,shotsFired, hits)
            #print actValPair[action]
            qVals.append(actValPair[action])

        max_value = max(qVals)

        for action in actions:

            if actValPair[action] == max_value:
                max_actions.append(action)

        if len(max_actions) > 1:
          max_action = random.choice(max_actions)

        else:
          max_action = max_actions[0]

        return max_action

    def getQValue(self, action, shotsFired, hits):

        return self.qValues[frozenset([action, hits, shotsFired])]

    def update_qvalue(self, isHit, target, counter, shotsFired, hits):

        legalActions = self.getRemainingActions(shotsFired)
        values = []
        
        if counter == 0:
            reward = 0

        elif isHit:
            reward=0.5
        else:
            reward=0.1

        #for action in legalActions:
         #   values.append(self.getQValue(action, shotsFired,hits))

        #print self.qValues
        #max_value = max(values)
        #print max_value
        sample = reward + self.discount * max(self.getQValue(action,shotsFired, hits) for action in legalActions)
        self.qValues[(target, hits, shotsFired)] = (1-self.alpha) * self.getQValue(target, hits, shotsFired) + self.alpha * sample

        #else:
         #   self.qValuesOfMiss[distance] = (1-self.alpha) * self.getQValue(distance,isHit) + self.alpha * sample

    #def getAction(self):
    def print_board(self, s,board):

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


    def computer_place_ships(self,board,ships):

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
                valid = self.validate(board,ships[ship],x,y,ori)

            #place the ship
            print "Computer placing a/an " + ship
            board = self.place_ship(board,ships[ship],ship[0],ori,x,y)

        return board


    def place_ship(self,board,ship,s,ori,x,y):

        #place ship based on orientation
        if ori == "v":
            for i in range(ship):
                board[x+i][y] = s
        elif ori == "h":
            for i in range(ship):
                board[x][y+i] = s

        return board

    def validate(self,board,ship,x,y,ori):

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


    def make_move(self,board,x,y):

        #make a move on the board and return the result, hit, miss or try again for repeat hit
        if board[x][y] == -1:
            return "miss"
        elif board[x][y] == ('\x1b[0;31;40m' + "*" + '\x1b[0m') or board[x][y] == ('\x1b[0;32;40m' + 'X' + '\x1b[0m'):
            return "try again"
        else:
            return "hit"


    def random_mode(self,board):

        #generate user coordinates from the user and try to make move
        #if move is a hit, check ship sunk and win condition
        while(True):
            x = random.randint(1,10)-1
            y = random.randint(1,10)-1
            res = self.make_move(board,x,y)
            if res == "hit":
                print "Hit at " + str(x+1) + "," + str(y+1)
                self.check_sink(board,x,y)
                board[x][y] = ('\x1b[0;32;40m' + 'X' + '\x1b[0m')
                if self.check_win(board):
                    return "WIN"
            elif res == "miss":
                print "Sorry, " + str(x+1) + "," + str(y+1) + " is a miss."
                board[x][y] = ('\x1b[0;31;40m' + "*" + '\x1b[0m')

            if res != "try again":

                return board

    def estimate_mode(self,board, direction):
    #generate user coordinates from the user and try to make move
    #if move is a hit, check ship sunk and win condition
        while(True):

            for k in range(10):
                for i in range(10):
                    if direction == 'unknown':
                        if board[i][k] == ('\x1b[0;32;40m' + 'X' + '\x1b[0m') and i != 9:
                            res = self.make_move(board, i+1, k)
                            if res == "hit":
                                direction = 'down'
                                print "Hit at " + str(i+2) + "," + str(k+1)
                                self.check_sink(board,i+1,k)
                                board[i+1][k] = ('\x1b[0;32;40m' + 'X' + '\x1b[0m')
                                if self.check_win(board):
                                    return board, "WIN"
                                return board, direction
                            if res == "miss":
                                direction = 'not down'
                                print "Sorry, " + str(i+2) + "," + str(k+1) + " is a miss."
                                board[i+1][k] = ('\x1b[0;31;40m' + "*" + '\x1b[0m')
                                return board, direction
                            elif res == "try agian" and i!= 9:
                                direction = 'unknown'
                                i = i + 1
                                res = self.make_move(board, i, k)
                                if res == "try again" and i!= 9:
                                    i = i + 1
                                    res = self.make_move(board, i, k)
                                return board, direction 
                    if direction ==  'not down':
                        if board[i][k] == ('\x1b[0;32;40m' + 'X' + '\x1b[0m') and i != 0:
                            res = self.make_move(board, i - 1, k)
                            if res == "hit":
                                direction = 'up'
                                print "Hit at " + str(i) + "," + str(k+1)
                                self.check_sink(board,i-1,k)
                                board[i-1][k] = ('\x1b[0;32;40m' + 'X' + '\x1b[0m')
                                if self.check_win(board):
                                    return board, "WIN"
                                return board, direction
                            if res == "miss":
                                direction = 'not up'
                                print "Sorry, " + str(i) + "," + str(k+1) + " is a miss."
                                board[i-1][k] = ('\x1b[0;31;40m' + "*" + '\x1b[0m')
                                return board, direction
                            elif res == "try agian" and i!= 0:
                                direction = 'unknown'
                                i = i - 1
                                res = self.make_move(board, i, k)
                                if res == "try again" and i!= 0:
                                    i = i - 1
                                    res = self.make_move(board, i, k)
                                return board, direction
                    if direction == 'not up':
                        if board[i][k] == ('\x1b[0;32;40m' + 'X' + '\x1b[0m') and k != 9:
                            res = self.make_move(board, i, k+ 1)
                            if res == "hit":
                                direction = 'right'
                                print "Hit at " + str(i+1) + "," + str(k+2)
                                self.check_sink(board,i,k + 1)
                                board[i][k+1] = ('\x1b[0;32;40m' + 'X' + '\x1b[0m')
                                if self.check_win(board):
                                    return board, "WIN"
                                return board, direction
                            if res == "miss":
                                direction = 'not right'
                                print "Sorry, " + str(i+1) + "," + str(k+2) + " is a miss."
                                board[i][k+1] = ('\x1b[0;31;40m' + "*" + '\x1b[0m')
                                return board, direction
                            elif res == "try agian" and k!= 9:
                                direction = 'unknown'
                                k = k + 1
                                res = self.make_move(board, i, k)
                                if res == "try again" and k!= 9:
                                    k= k + 1
                                    res = self.make_move(board, i, k)
                                return board, direction
                    if direction == 'not right':
                        if board[i][k] == ('\x1b[0;32;40m' + 'X' + '\x1b[0m') and k != 0:
                            res = self.make_move(board, i, k - 1)
                            if res == "hit":
                                direction = 'left'
                                print "Hit at " + str(i+1) + "," + str(k)
                                self.check_sink(board,i,k - 1)
                                board[i][k-1] = ('\x1b[0;32;40m' + 'X' + '\x1b[0m')
                                if self.check_win(board):
                                    return board, "WIN"
                                return board, direction
                            if res == "miss":
                                direction = 'unknown'
                                print "Sorry, " + str(i+1) + "," + str(k) + " is a miss."
                                board[i][k-1] = ('\x1b[0;31;40m' + "*" + '\x1b[0m')
                                return board, direction
                            elif res == "try agian" and k!= 0:
                                direction = 'unknown'
                                k = k - 1
                                res = self.make_move(board, i, k)
                                if res == "try again" and k!= 0:
                                    k = k - 1
                                    res = self.make_move(board, i, k)
                                return board, direction


                    if direction == 'down':
                        if board[i][k] == ('\x1b[0;32;40m' + 'X' + '\x1b[0m') and i != 9:
                            res = self.make_move(board, i+1, k)
                            if res == "hit":
                                direction = 'down'
                                print "Hit at " + str(i+2) + "," + str(k+1)
                                self.check_sink(board,i+1,k)
                                board[i+1][k] = ('\x1b[0;32;40m' + 'X' + '\x1b[0m')
                                if self.check_win(board):
                                    return board, "WIN"
                                return board, direction
                            if res == "miss":
                                direction = 'up'
                                print "Sorry, " + str(i+2) + "," + str(k+1) + " is a miss."
                                board[i+1][k] = ('\x1b[0;31;40m' + "*" + '\x1b[0m')
                                return board, direction
                            elif res == "try agian" and i!= 9:
                                direction = 'down'
                                i = i + 1
                                res = self.make_move(board, i, k)
                                if res == "try again" and i!= 9:
                                    i = i + 1
                                    res = self.make_move(board, i, k)
                                return board, direction 
                    
                    if direction == 'up':
                        if board[i][k] == ('\x1b[0;32;40m' + 'X' + '\x1b[0m') and i != 0:
                            res = self.make_move(board, i-1, k)
                            if res == "hit":
                                direction = 'up'
                                print "Hit at " + str(i) + "," + str(k+1)
                                self.check_sink(board,i-1,k)
                                board[i-1][k] = ('\x1b[0;32;40m' + 'X' + '\x1b[0m')
                                if self.check_win(board):
                                    return board, "WIN"
                                return board, direction
                            if res == "miss":
                                direction = 'down'
                                print "Sorry, " + str(i) + "," + str(k+1) + " is a miss."
                                board[i-1][k] = ('\x1b[0;31;40m' + "*" + '\x1b[0m')
                                return board, direction
                            elif res == "try agian" and i!= 0:
                                direction = 'up'
                                i = i - 1
                                res = self.make_move(board, i, k)
                                if res == "try again" and i!= 0:
                                    i = i - 1
                                    res = self.make_move(board, i, k)
                                return board, direction 
                    if direction == 'right':
                        if board[i][k] == ('\x1b[0;32;40m' + 'X' + '\x1b[0m') and k != 9:
                            res = self.make_move(board, i, k+ 1)
                            if res == "hit":
                                direction = 'right'
                                print "Hit at " + str(i+1) + "," + str(k+2)
                                self.check_sink(board,i,k + 1)
                                board[i][k+1] = ('\x1b[0;32;40m' + 'X' + '\x1b[0m')
                                if self.check_win(board):
                                    return board, "WIN"
                                return board, direction
                            if res == "miss":
                                direction = 'left'
                                print "Sorry, " + str(i+1) + "," + str(k+2) + " is a miss."
                                board[i][k+1] = ('\x1b[0;31;40m' + "*" + '\x1b[0m')
                                return board, direction
                            elif res == "try agian" and k!= 9:
                                direction = 'right'
                                k = k + 1
                                res = self.make_move(board, i, k)
                                if res == "try again" and k!= 9:
                                    k= k + 1
                                    res = self.make_move(board, i, k)
                                return board, direction
                    if direction == 'left':
                        if board[i][k] == ('\x1b[0;32;40m' + 'X' + '\x1b[0m') and k != 0:
                            res = self.make_move(board, i, k - 1)
                            if res == "hit":
                                direction = 'left'
                                print "Hit at " + str(i+1) + "," + str(k)
                                self.check_sink(board,i,k - 1)
                                board[i][k-1] = ('\x1b[0;32;40m' + 'X' + '\x1b[0m')
                                if self.check_win(board):
                                    return board, "WIN"
                                return board, direction
                            if res == "miss":
                                direction = 'right'
                                print "Sorry, " + str(i+1) + "," + str(k) + " is a miss."
                                board[i][k-1] = ('\x1b[0;31;40m' + "*" + '\x1b[0m')
                                return board, direction
                            elif res == "try agian" and k!= 0:
                                direction = 'left'
                                k = k - 1
                                res = self.make_move(board, i, k)
                                if res == "try again" and k!= 0:
                                    k = k - 1
                                    res = self.make_move(board, i, k)
                                return board, direction
            
            direction = 'unknown'
            x = random.randint(1,10)-1
            y = random.randint(1,10)-1
            res = self.make_move(board,x,y)
            if res == "hit":
                print "Hit at " + str(x+1) + "," + str(y+1)
                self.check_sink(board,x,y)
                board[x][y] = ('\x1b[0;32;40m' + 'X' + '\x1b[0m')
                if self.check_win(board):
                    return board, "WIN"
            elif res == "miss":
                print "Sorry, " + str(x+1) + "," + str(y+1) + " is a miss."
                board[x][y] = ('\x1b[0;31;40m' + "*" + '\x1b[0m')
            if res != "try again":
                return board, direction

    def qlearning_mode(self, board, shotsFired, hits):

        
        isHit = False
        counter = 0
        x = random.randint(1,10)-1
        y = random.randint(1,10)-1 
        current_target = x,y

        res = self.make_move(board,x,y)
        if res == "hit":
            isHit = True
            hits = hits.union(current_target)
            #print hits
            shotsFired = shotsFired.union(current_target)
            #print "Hit at " + str(x+1) + "," + str(y+1)
            self.check_sink(board,x,y)
            board[x][y] = ('\x1b[0;32;40m' + 'X' + '\x1b[0m')
            
        elif res == "miss":
            isHit = False
            shotsFired = shotsFired.union(current_target)
            #print "Sorry, " + str(x+1) + "," + str(y+1) + " is a miss."
            board[x][y] = ('\x1b[0;31;40m' + "*" + '\x1b[0m')

        self.update_qvalue(isHit, current_target, counter, shotsFired, hits)

        while(True):
            x, y = self.computeActionsFromQValues(shotsFired, hits)
            current_target = x,y

            res = self.make_move(board,x,y)
            if res == "hit":
                isHit = True
                hits = hits.union(current_target)
                #print hits
                shotsFired = shotsFired.union(current_target)
                #print "Hit at " + str(x+1) + "," + str(y+1)
                self.check_sink(board,x,y)
                board[x][y] = ('\x1b[0;32;40m' + 'X' + '\x1b[0m')
                if self.check_win(board):
                    return "WIN"

            elif res == "miss":
                isHit = False
                shotsFired = shotsFired.union(current_target)
                #print "Sorry, " + str(x+1) + "," + str(y+1) + " is a miss."
                board[x][y] = ('\x1b[0;31;40m' + "*" + '\x1b[0m')

            if res != "try again":
                #self.hits = hits
                #self.shotsFired = shotsFired
                return board

            counter += 1
            self.update_qvalue(isHit, current_target, counter, shotsFired, hits)

    def check_sink(self,board,x,y):

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


    def check_win(self,board):

        #simple for loop to check all cells in 2d board
        #if any cell contains a char that is not a hit or a miss return false
        for i in range(10):
            for j in range(10):
                if board[i][j] != -1 and board[i][j] != ('\x1b[0;31;40m' + "*" + '\x1b[0m') and board[i][j] != ('\x1b[0;32;40m' + 'X' + '\x1b[0m'):
                    return False
        return True

def main():

    agent = Agent()
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
    user_board = agent.computer_place_ships(user_board,ships)
    count = 0
    #game main loop
    print "Welcome to battleship, which game mode do you want to simulate?"
    print "\n"
    test_bool = True
    while (test_bool):
        game_mode = raw_input("\tRandom (r)\n\tEstimated Guess (e)\n\tQ Learning (q)\n")
        if game_mode == "r" or game_mode == "e" or game_mode == "q":
            test_bool = False
        else:
            print "Invalid input. Please only enter r, e, or q"
            test_bool = True

    if game_mode == 'r':

        while(1):

        #computer move
            user_board = agent.random_mode(user_board)
            count = count + 1
        #check if computer move
            if user_board == "WIN":
                print "GAME OVER"
                print "Move count :",count,"."
                quit()

        #display user board
            agent.print_board("u",user_board)
            raw_input("To end computer turn hit ENTER")

    if game_mode == 'e':
        direction = 'unknown'
        while(1):


            user_board, direction =  agent.estimate_mode(user_board, direction)
            count = count + 1
            print direction
        #check if computer move
            if direction == "WIN":
                print "GAME OVER"
                print "Move count :",count,"."
                quit()
            agent.print_board("u", user_board)
            raw_input("To end computer turn hit ENTER")

    if game_mode == 'q':
        i = 0

        while(i < 2000):
            shotsFired = frozenset()
            hits = frozenset()
            board = []
            for j in range(10):
                board_row = []
                for k in range(10):
                    board_row.append(-1)
                board.append(board_row)

            #setup board
            user_board = copy.deepcopy(board)

            #add ships as last element in the array
            user_board.append(copy.deepcopy(ships))

            #ship placement
            user_board = agent.computer_place_ships(user_board,ships)
            count = 0
            i += 1 
            print "Iteration: ", i,"."     
            while(1):
               
                user_board = agent.qlearning_mode(user_board, shotsFired, hits)
                count = count + 1
                #check if computer move
                if user_board == "WIN":
                    #print "GAME OVER"
                    print "Move count :",count,"."
                    break

if __name__=="__main__":
    main()


