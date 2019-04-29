#import itertools pack to iterate through player 1 and 2 
import itertools


#function that checks for winners
def win(current_game):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    #check for horizontal winners 
    for row in game:
        print(row)
        if all_same(row):
            print(f"Player {row[0]} is the winner horizontally!")
            return True

    #check for vertical winners 
    for col in range(len(game[0])):
        check = []
        for row in game:
            check.append(row[col])
        if all_same(check):
            print(f"Player {check[0]} is the winner vertically!")
            return True

    #check for / diagonal winners  
    diags = []
    for idx, reverse_idx in enumerate(reversed(range(len(game)))):
        diags.append(game[idx][reverse_idx])
    if all_same(diags):
        print(f"Player {diags[0]} has won diagonally (/)")
        return True

    #check for \ diagonal winners
    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        print(f"Player {diags[0]} has won diagonally (\\)")
        return True

    return False


#define and initialize game baord function 
def game_board(game_map, player=0, row=0, col=0, just_display=False):
    try:
        #if the user inputs a location out of range
        if game_map[row][col] != 0:
            print("This space is occupied, try another!")
            return False

        #change the value of the index that the user specified
        print("   0  1  2")
        if not just_display:
            game_map[row][col] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map
    
    #notify index error 
    except IndexError:
        print("Make sure to play a row or col within the range of 0,1 or 2? (IndexError)")
        return False
    #notify exception error  
    except Exception as e:
        print(str(e))
        return False

#define player 1 and 2 and restart game board    
play = True
players = [1, 2]
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    #iterate player 1 and 2 
    game_won = False
    game = game_board(game, just_display=True)
    player_cycle = itertools.cycle([1, 2])
    
    #take row and col input from user 
    while not game_won:
        current_player = next(player_cycle) 
        played = False
        
        while not played:
            print(f"Player: {current_player}")
            col_choice = int(input("Which column? "))
            row_choice = int(input("Which row? "))
            played = game_board(game, player=current_player, row=row_choice, col=col_choice)
        if win(game):
            game_won = True
            again = input("The game is over, would you like to play again? (y/n) ")
            if again.lower() == "y":
                print("Restarting")
            elif again.lower() == "n":
                print("Bye")
                play = False
            else:
                print("Not a valid answer")
                play = False