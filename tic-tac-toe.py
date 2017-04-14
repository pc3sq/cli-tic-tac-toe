import pdb


class Board(object):
    """Proto for tic-tac-toe board."""
    def __init__(self, size=(3,3)):
        # super(, self).__init__()
        self.size = size
        self.status = self.init_board()


    def init_board(self):
        return [ [i for i in xrange(m * self.size[0], m * self.size[0] + self.size[0])] for m in xrange(0, self.size[1]) ]

    def print_board(self):
        print "  " + "-" * (4 * len(self.status[0]) - 1)

        for row in self.status:
                print (" | " + " | ".join(["%d"] * len(row)) + " | ") % tuple(row)
                print "  " + "-" * (4 * len(row) - 1)

    def init_game(self):
        num_of_players = 0

        while num_of_players not in ["1", "2"]:
            print "TIC-TAC-TOE"
            num_of_players = raw_input("How many human players? (max of 2)\n")

        # board = self.init_board()

        self.print_board()

        print "End of start_game()."


# pdb.set_trace()

if __name__ == '__main__':
    board = Board()
    board.init_game()
