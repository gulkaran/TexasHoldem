import random


def newDeck(deck):
    # CREATING DECK USING NESTED FOR LOOP
    suits = ["Spades", "Clubs", "Hearts", "Diamonds"]

    cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack",
             "Queen", "King"]

    for i in suits:
        for j in cards:
            deck.append(j + " of " + i)

    random.shuffle(deck)
    return deck


# Handing out Cards
def cards(deck):
    player1_hand = [deck[0], deck[2]]
    player2_hand = [deck[1], deck[3]]
    del deck[0:4]
    print("Player 1, Your cards are", player1_hand)
    print("Player 2, Your cards are", player2_hand)
    return deck, player1_hand, player2_hand


# Values Key - used for
mykey = {
    "Ace": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 11, "Queen": 12, "King": 13,
}

rkey = {
    1: "Ace", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10", 11: "Jack", 12: "Queen", 13: "King",
}
