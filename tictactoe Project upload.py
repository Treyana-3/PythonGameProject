# This is the board template of the game 
board = [
["-", "-", "-", "-"],
["-", "-", "-", "-"],
["-", "-", "-", "-"],
["-", "-", "-", "-"]
]

user = True #True refers to x otherwise o
turns = 0
# This prints out the board 
def print_board(board):
    for row in board:
        for slot in row:#this looks at each individual slot for each row 
            print(f"{slot} ", end="")#This spaces out the rows 
        print()#Makes 4 different rows 

print_board(board) #Makes a new line for each slot printed 
#F defines strings as variables 

#A loop is needed to end the game when someone wins --> 
def quit(user_input):
    if user_input.lower() == "q": #letters are made lowercase 
        print("Thank you for playing") 
        return False 
    else: return True

#Checks for a number (1-12)
def check_input(user_input):
    user_input: int(user_input)
    if not isnum(user_input): return False #Stops the function if the output is false 

    return True
    #If you get throught the entire function it will return true

def isnum(user_input):
    if  not user_input.isnumeric():
        print("This is not a valid number")#Is not a number 1-12
        return False 
    else: return True #Is a number 1-12
#Checking bounderies 
#def bounds(user_input):


#Checks if a spot is taken or not to be filled in
def istaken(coords, board): #Sees if the cordinates on the board are already taken
    row = coords[0]
    col = coords[1]
    if board[row][col]  != "-":
        print("This position is already taken.")
        return True
    else: return False



def cordinates(user_input):
    row = int(user_input / 3)
    col = user_input
    if col > 2: col = int(col % 3)
    return(row,col)

def add_to_board(coords, board, active_user): #Adds cordinates
    row = coords[0]
    col = coords[1]
    board[row][col] = active_user

def current_user(user):
    if user: return "x"
    else: return "o"

def iswin(user, board):
    if check_row(user, board): return True
    if check_col(user, board): return True
    if check_diag(user, board): return True
    return False


def check_row(user, board):
    for row in board:
        complete_row = True #Keeps track of te game (win/lose)
        for slot in row:
            if slot != user:
                complete_row = False
                break #doesnt check any further if false 
            if complete_row: return True
        return False #Checks the rows 

def check_col(user, board):
    for col in range(4):
        complete_col = True
    for row in range(4):
        if board[row][col] != user:
            complete_col = False
            break
    if complete_col: return True #End so the game doesnt keep going on
    return False 

def check_diag(user, board):
    if board[0][0] == user and board[1][1] == user and board[2][2] == user:return True
    elif board[0][2] == user and board[1][1] == user and board[2][0] == user: return True
    else: return False

while turns < 12:
    active_user = current_user(user) #Boolean x, or o 
    print_board(board)
    user_input = input("Enter a position 1 through 12 or enter q to quit:")
    if quit(user_input): break
    if not check_input(user_input):
        print("Please try again.")
        continue #This code re-runs the loop from the begining 

#Have to account for this function because we are asking for 1-9 and the index is at 0
user_input = int(user_input) - 1
coords = cordinates(user_input)
if istaken(coords, board):
    print("please try again.")

add_to_board(coords, board, active_user)
if iswin(active_user, board):
    print(f"{active_user.upper()} won!")

turns +=1
if turns == 12: print("Tie!")
user = not user #This code switches turns between the users palying the game 

    

        