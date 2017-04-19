import pdb

class Board(object):
    """Proto for tic-tac-toe board."""
    def __init__(self, size=(3,3)):
        # super(, self).__init__()
        self.size = size
        self.state = self.init_board()

    def init_board(self):
        return [ [i for i in xrange(m * self.size[0], m * self.size[0] + self.size[0])] for m in xrange(0, self.size[1]) ]

    def print_board(self):
        print "  " + "-" * (4 * len(self.state[0]) - 1)

        for row in self.state:
                print (" | " + " | ".join(["%d"] * len(row)) + " | ") % tuple(row)
                print "  " + "-" * (4 * len(row) - 1)

class Player(object):
    def __init__(self, name="Player Bozo", team="X"):
        self.name = name
        self.team = team

class Game(object):
    '''
    Keeps a record of all the game components like the players and the gameboard and controls the game dyanmics.
    '''
    def __init__(self, board):
        self.board = board
        self.num_players = int(self.set_num_players())
        self.players = []

    def set_num_players(self):
        num_of_players = 0

        while num_of_players not in ["1", "2"]:
            print "TIC-TAC-TOE"
            num_of_players = raw_input("How many human players? (max of 2)\n")

        print num_of_players
        return num_of_players

    def create_players(self):
        teams = ['x', 'o']

        team_select = "Which team, " + " or ".join("\'{}\'".format(t) for t in teams) + "?  "

        def repeat_team_select(team):
            return "Team \'{}\' not available. ".format(team) + team_select

        for i in xrange(self.num_players):
            name = raw_input("Name of player {}?\n".format(i+1))
            team = raw_input(team_select)

            while team not in teams:
                team = raw_input(repeat_team_select(team))

            self.players.append(Player(name, team))

            teams = filter(lambda t: t is not team, teams)

        print "Players created: " + " ,".join("{}".format(t) for t in teams)


    def create_game(self):
        self.create_players()

    def print_players(self):
        # print " ,".join("{}".format(p) for p in [p.name for p in self.players])
        print
        for i, p in enumerate(self.players):
            print "Player {}: {}".format(i+1, p.name)

    def status(self):
        self.print_players()
        self.board.print_board()
        print "The End."


# pdb.set_trace()

if __name__ == '__main__':
    board = Board()
    game = Game(board)
    game.create_game()
    game.status()
