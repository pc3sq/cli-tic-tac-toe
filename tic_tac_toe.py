import pdb

class Board(object):
    """Proto for tic-tac-toe board."""
    def __init__(self, size=(3,3)):
        # super(, self).__init__()
        self.size = size
        self.layout = { 0: (0,0),
                        1: (0,1),
                        2: (0,2),
                        3: (1,0),
                        4: (1,1),
                        5: (1,2),
                        6: (2,0),
                        7: (2,1),
                        8: (2,2) }
        self.state = self.init_board()

    def init_board(self):
        return [ [i for i in xrange(m * self.size[0], m * self.size[0] + self.size[0])] for m in xrange(0, self.size[1]) ]

    def print_board(self):
        print "  " + "-" * (4 * len(self.state[0]) - 1)

        for row in self.state:
                print (" | " + " | ".join(["%s"] * len(row)) + " | ") % tuple(row)
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

        if self.num_players == 2:
            for i in xrange(self.num_players):
                name = raw_input("Name of player {}?\n".format(i+1))

                if i == 0:
                    team = raw_input(team_select)

                    while team not in teams:
                        team = raw_input(repeat_team_select(team))

                    self.players.append(Player(name, team))

                    teams = filter(lambda t: team is not t, teams)
                else:
                    self.players.append(Player(name, teams[0]))
                    print "Player 2, name, defaults to team {}".format(teams[0])

            # print "Players created: " + " ,".join("{}".format(t) for t in teams)
            self.print_players()

        else:
            name = raw_input("Name of player {}?\n".format(i+1))
            team = raw_input(team_select)

            while team not in teams:
                team = raw_input(repeat_team_select(team))

            self.players.append(Player(name, team))

            self.print_players()


    def create_game(self):
        self.create_players()

    def print_players(self):
        # print " ,".join("{}".format(p) for p in [p.name for p in self.players])
        print
        for i, p in enumerate(self.players):
            print "Player {}: {} \t\t Team: {}".format(i+1, p.name, p.team.upper())

    def status(self):
        self.print_players()
        self.board.print_board()


    def run_game(self):
        self.status()

        if self.num_players == 2:
            # until all spaces are filled
            whos_turn = [1,0]
            player_turn = 1
            self.status()

            try:
                space = int(raw_input("{}, which space would you like to take?\n".format(self.players[player_turn].name.upper())))
            except:
                space = int(raw_input("{}, which space would you like to take?\n".format(self.players[player_turn].name.upper())))

            print space
            print self.board.state

            space_loc = self.board.layout[space]

            while space not in [num for sublist in self.board.state for num in sublist] or self.board.state[space_loc[0]][space_loc[1]] in ['x', 'o']:
                space = raw_input("Space {} not available. Please choose another space.".format(space, self.players[player_turn].name.upper()))

            self.board.state[space_loc[0]][space_loc[1]] = self.players[player_turn].team


        else:
            print "Need to create a computer player."

        self.status()
        print "The End."


# pdb.set_trace()

if __name__ == '__main__':
    board = Board()
    game = Game(board)
    game.create_game()
    game.status()
    game.run_game()
