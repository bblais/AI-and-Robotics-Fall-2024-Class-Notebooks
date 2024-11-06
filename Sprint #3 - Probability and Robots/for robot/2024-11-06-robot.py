from Game import *
from Robot373 import *

left,right=Motors("ab")



#=============GAME FUNCTIONS ===============
def initial_state():
    return Board(3,3)

def count_pieces(state):
    count=0
    for location in range(9):
        if state[location]!=0:
            count=count+1
            
    return count

def row(state,location):
    r,c=state.rc_from_index(location)
    return r
def col(state,location):
    r,c=state.rc_from_index(location)
    return c

def valid_moves(state,player):
    
    moves=[]
    
    if count_pieces(state)<9:  # placement - temporaily set to 9 to behave like ttt
        # placement
        for location in range(9): 
            if state[location]==0:
                moves.append(location)
    else:
        # sliding
        for start in range(9):
            if state[start]!=player:
                continue

            rs,cs=row(state,start),col(state,start)

            for location in range(9):
                end=None

                r,c=row(state,location),col(state,location)

                if state[location]==0:

                    if r-rs==1 and c-cs==0:  # vertical
                        end=location
                    if r-rs==-1 and c-cs==0:  # vertical
                        end=location
                    if r-rs==0 and c-cs==1:  # horizontal
                        end=location
                    if r-rs==0 and c-cs==-1:  # horizontal
                        end=location
                    if r-rs==1 and c-cs==1:  # diagonal
                        end=location
                    if r-rs==-1 and c-cs==-1:  # diagonal
                        end=location
                    if r-rs==1 and c-cs==-1:  # diagonal
                        end=location
                    if r-rs==-1 and c-cs==1:  # diagonal
                        end=location

                    if not end is None:
                        moves.append([start,end])
                pass

        
    return moves
    
    
def update_state(state,player,move):
    if isinstance(move,int):  # placement
        new_state=state
        new_state[move]=player
        
    else:  # sliding
        start,end=move
        new_state=state
        new_state[start]=0
        new_state[end]=player
        
    return new_state

def win_status(state,player):
    # 0  1  2 
    # 3  4  5 
    # 6  7  8 

    if player==1:
        other_player=2
    else:
        other_player=1
    
    if state[0]==state[1]==state[2]==player:
        return "win"
    if state[3]==state[4]==state[5]==player:
        return "win"
    if state[6]==state[7]==state[8]==player:
        return "win"
    if state[0]==state[3]==state[6]==player:
        return "win"
    if state[1]==state[4]==state[7]==player:
        return "win"
    if state[2]==state[5]==state[8]==player:
        return "win"
    if state[0]==state[4]==state[8]==player:
        return "win"
    if state[6]==state[4]==state[2]==player:
        return "win"
    
    if not valid_moves(state,other_player):
        return "stalemate"
    
    return None

def show_state(state,player):
    print(state)


#=============AGENT FUNCTIONS (not all of them) ===============

def random_move(state,player):    
    moves=valid_moves(state,player)
    return random.choice(moves)

random_agent=Agent(random_move)

def human_move(state,player):
    print("Player ", player)
    valid_move=False
    while not valid_move:
        move=int(input('What is your move? '))

        if move in valid_moves(state,player):
            valid_move=True
        else:
            print("Illegal move.")

    return move
human_agent=Agent(human_move)



#=============ROBOT Functions ===============


def get_move(state,player):
    if player==1:
        Q=LoadTable("TTT Q1 Table.json")
    else:
        Q=LoadTable("TTT Q2 Table.json")

    if state not in Q:
        print("State not in the table: ",state)
        move=random_move(state,player)
    else:
        move=top_choice(Q[state])

    return move


def read_state_from_file(filename):
    from Game import Board
    text=open(filename).read()
    text=text.strip()
    lines=[line.strip() for line in text.split('\n')]  # get rid of \n

    row=lines[0].split()
    R,C=len(lines),len(row)
    print(f"{R}x{C} board")
    state=Board(R,C)
    state.board=[int(val) for val in text.split()]
    print(state)
    return state

read_state=read_state_from_file

def forward():
    left.power=19
    right.power=19  # Reset both motors to forward

def stop():
    left.power=0
    right.power=0  # Reset both motors to forward


def get_color(verbose=False):
    r,g,b,something=color_sensor.value
    detected_color=closest_color(r,g,b,
        yellow=[255,255,0],
        blue=[0,0,255],
        white=[255,255,255],
        black=[0,0,0]
    )

    if verbose:
        print("Color read: ",r,g,b)
        print("Color name: ",detected_color)


    return detected_color


def go_forward_squares(n):
    forward()
    Wait(0.2*n)
    stop()

def rot90():
    left.power=-20
    right.power=20
    Wait(0.5)
    stop()



def make_move(state,player,move):
    start,end=move
    row,col=state.row(start),state.col(start)

    # depends on where the robot starts
    number_cols_to_move=4-col
    number_rows_to_move=4-row


    go_forward_squares(number_cols_to_move)
    rot90()
    go_forward_squares(number_rows_to_move)


    #  0  1  2  3 
    #  4  5  6  7 
    #  8  9 10 11 
    # 12 13 14 15 
    
    if start-end==3:
        do_right_diag()
    elif start-end==5:
        do_left_diag()
    elif start-end==4:
        do_forward_move()
    else:
        raise ValueError("You can't get there from here")


#======== MAIN CODE=========

player=1 # or player=2 depending on which you want
state=read_state() # read the pieces, and construct the state
move=get_move(state,player) # replace with minimax,skitles, Q, etc...
make_move(state,player,move) # actually move the pieces

