# COMMUNITY CARDS - FLOP, TURN, RIVER

def dealFlop(deck, board):
    del deck[0]  # simiulate burning off a card

    for i in range(0, 3):
        board.append(deck[i])

    del deck[0:3]
    return deck, board


def dealTurn(deck, board):
    del deck[0]
    board.append(deck[0])
    del deck[0]
    return deck, board


def dealRiver(deck, board):
    deck, board = dealTurn(deck, board)
    return deck, board
