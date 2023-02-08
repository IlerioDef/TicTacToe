def game_grid(value, file_obj=None):
    print("\n", file=file_obj)
    print("\t       |       |", file=file_obj)
    print("\t   {}   |   {}   |   {}".format(value[0], value[1], value[2]), file=file_obj)
    print('\t_______|_______|_______', file=file_obj)
    print("\t       |       |", file=file_obj)
    print("\t   {}   |   {}   |   {}".format(value[3], value[4], value[5]), file=file_obj)
    print('\t_______|_______|_______', file=file_obj)
    print("\t       |       |", file=file_obj)
    print("\t   {}   |   {}   |   {}".format(value[6], value[7], value[8]), file=file_obj)
    print("\t       |       |", file=file_obj)
    print("\n", file=file_obj)

def my_scoreboard(score_board):
    def name_reductor(name, separator=" "):
        red_name = str()
        if len(name) <= 25:
            red_name=name+(25-len(name))*separator
        else:
            red_name = name[:25]
        return red_name




    print("\t----------------------------------------------------------------")
    print("\t         The SCOREBOARD for TIC TAC TOE PYTHON GAME       ")
    print("\t----------------------------------------------------------------")

    list_of_the_two_players = list(score_board.keys())
    print("\t    "*2, name_reductor(list_of_the_two_players[0]), "\t    ", score_board[list_of_the_two_players[0]])
    print("\t    "*2, name_reductor(list_of_the_two_players[1]), "\t    ", score_board[list_of_the_two_players[1]])

    print("\t----------------------------------------------------------------\n")

###To validate the Win or Tie situation of tic tac toe Python
# User-defined function Python for validating the win combinations in the entire tic tac toe Python game
def win_validate(position_player, player_current):

 # Below are all the possible winning combinations that were analyzed to win the tic tac toe Python game
    win_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

# using the for loop in Python to validate if any winning combination is getting validated as TRUE or not
    for i in win_combinations:
        if all(j in position_player[player_current] for j in i):

# If any winning combination is getting validated as TRUE then the function shall return TRUE
            return True
# If any winning combination is not getting validated as TRUE then the function shall return FALSE
    return False

# User-defined function Python for validating is the tic ta toe Python game is a tie
def tie_validate(position_player):
    if len(position_player['X']) + len(position_player['O']) == 9:
        return True
    return False
