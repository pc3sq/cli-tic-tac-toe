import pdb

def init_board(size=(3,3)):
    return [ [i for i in xrange(m*size[0], m*size[0]+size[0])] for m in xrange(0, size[1]) ]


# pdb.set_trace()

if __name__ == '__main__':
    # board = init_board((6, 10))
    board = init_board()
    print board
