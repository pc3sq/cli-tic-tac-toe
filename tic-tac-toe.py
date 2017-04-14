import pdb

def init_board(size=(3,3)):
    return [ [i for i in xrange(m*size[0], m*size[0]+size[0])] for m in xrange(0, size[1]) ]

def print_board(board):
    print "  " + "-" * (4 * len(board[0]) - 1)

    for row in board:
            print (" | " + " | ".join(["%d"] * len(row)) + " | ") % tuple(row)
            print "  " + "-" * (4 * len(row) - 1)

def init_game():
    num_of_players = 0

    while num_of_players not in ["1", "2"]:
        print "TIC-TAC-TOE"
        num_of_players = raw_input("How many human players? (max of 2)\n")

    board = init_board()

    print_board(board)

    print "End of start_game()."


# pdb.set_trace()

if __name__ == '__main__':
    init_game()
