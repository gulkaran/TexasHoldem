# Gulkaran Singh
# Poker - Culminating Pt 1.
# 2021-05-12

# IMPORT STATEMENTS
import random
from deck import *
from betting import *
from board import *
from winner import *

# INITIALIZING VARIABLES
player1_balance, player2_balance = 1000, 1000


# TITLES, RULES
print("----- WELCOME TO TEXAS HOLD-EM -----")
print("\n----- RULES -----")
print("To win you must bankrupt your foe! Traditional Rules Apply Except Aces Are Considered Low Cards; Winning Conditions Strongest to Weakest: ")
print("Royal Flush, Straight Flush, Four of a Kind, Full House, Flush, Straight, Three of a Kind, Two Pair, One Pair, High Card")


# GAME LOOP -> pot = 0, new deck, blind is payed, cards are dealt, first round of betting, 3 CC, bet, 1CC, bet, 1CC, final evalutation, winner
while player1_balance > 0 and player2_balance > 0:
    # RESETS ROUND VARIABLES
    pot = 0
    player1_hand, player2_hand, deck, board = [], [], [], []
    player1_bet, player2_bet = 0, 0
    P1_cardHigh, P2_cardHigh = 0, 0

    # GENERATE NEW DECK
    deck = newDeck(deck)

    # PAY BLIND
    player1_balance, player2_balance, pot = blind(
        player1_balance, player2_balance, pot)

    # CARDS ARE DEALT
    deck, player1_hand, player2_hand = cards(deck)

    # FIRST ROUND OF BETTING
    player1_balance, player2_balance, player1_bet, player2_bet, pot = bet(
        player1_balance, player2_balance, player1_bet, player2_bet, pot)

    # FIRST 3 COMMUNITY CARDS ARE DEALT - FLOP CARDS
    deck, board = dealFlop(deck, board)
    print("\n----- Flop Cards -----")
    for i in board:
        print("| " + str(i), end=" |  ")

    # SECOND ROUND OF BETTING
    player1_bet, player2_bet = 0, 0
    player1_balance, player2_balance, player1_bet, player2_bet, pot = bet(
        player1_balance, player2_balance, player1_bet, player2_bet, pot)

    # +1 COMMUNITY CARD IS DEALT - TURN CARD
    deck, board = dealTurn(deck, board)
    print("\n\n----- Turn Card -----")
    for i in board:
        print("| " + str(i), end=" |  ")

    # LAST ROUND OF BETTING
    player1_bet, player2_bet = 0, 0
    player1_balance, player2_balance, player1_bet, player2_bet, pot = bet(
        player1_balance, player2_balance, player1_bet, player2_bet, pot)

    # +1 COMMUNITY CARD IS DEALT - RIVER CARD
    deck, board = dealRiver(deck, board)
    print("\n\n----- River Card -----")
    for i in board:
        print("| " + str(i), end=" |  ")

    # CREATING PLAYER 2 BOARD FROM BASE BOARD
    board2 = []
    for i in range(5):
        board2.append(board[i])

    # FUNCTION TO CREATE BOARDS FROM PLAYER HANDS
    board, board2, player1_hand, player2_hand = playerBoard(
        board, board2, player1_hand, player2_hand)

    var1 = ""
    player1_points = 0
    var2 = ""
    player2_points = 0

    # CHECK WHAT WINNING CONDITION PLAYER 1 GOT
    board, mykey, var1, P1_cardHigh, player1_points = winner(
        board, mykey, var1, P1_cardHigh, player1_points)

    print("\n\nPlayer 1 Has " + str(var1) + " with",
          str(P1_cardHigh), "High Card")

    # CHECK WHAT WINNING CONDITION PLAYER 1 GOT
    board2, mykey, var2, P2_cardHigh, player2_points = winner(
        board2, mykey, var2, P2_cardHigh, player2_points)

    print("Player 2 Has " + str(var2) + " with",
          str(P2_cardHigh), "High Card")

    # ROUND WINNER - check winner function on more information
    print("\n----- ROUND WINNER -----")

    my_file = open("output.txt", "r+")

    if player1_points > player2_points:
        print("Player 1 Has The Stronger Hand! They Win The Pot!")
        player1_balance += pot
        my_file.write("Player 1 Wins\n")

    elif player2_points > player1_points:
        print("Player 2 Has The Stronger Hand! They Win The Pot!")
        player2_balance += pot
        my_file.write("Player 2 Wins\n")

    # IF PLAYER POINTS ARE TIED, CARD HIGHS ARE CHECKED
    elif player1_points == player2_points:

        if P1_cardHigh > P2_cardHigh:
            print("Player 1 Has The Stronger High Card! They Win The Pot!")
            player1_balance += pot
            my_file.write("Player 1 Wins\n")

        elif P2_cardHigh > P1_cardHigh:
            print("Player 2 Has The Stronger High Card! They Win The Pot!")
            player2_balance += pot
            my_file.write("Player 2 Wins\n")

        elif P1_cardHigh == P2_cardHigh:
            print("Both Player's Tie! Pot Get's Split!")
            pot /= 2
            player1_balance += pot
            player2_balance += pot
            my_file.write("Player's Tie\n")

    # PRINT OF FINAL BALANCES
    print("\n----- ENDING BALANCES -----")
    print("Player 1 Balance:", player1_balance)
    print("Player 2 Balance:", player2_balance)

    my_file.close()
# GAME WINNER
if player1_balance == 0:
    print("Player 1 Is Bankrupt! Player 2 WINS!")
elif player2_balance == 0:
    print("Player 2 Is Bankrupt! Player 1 WINS!")
