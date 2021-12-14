# INTIAL BLIND OF $50
def blind(p1_balance, p2_balance, pot):
    print("\n ----- $50 Blind Is Paid To Enter Round -----")
    p1_balance -= 50
    p2_balance -= 50
    pot += 100
    return p1_balance, p2_balance, pot

# CHECK, MATCH, RAISE, FOLD


def fold(opposingBalance, pot):
    # lose your blind + any previous bets (basically the pot)
    opposingBalance += pot
    print("You Folded, Pot is awarded to Opposing Player")
    return opposingBalance, pot


def check(bet):
    # check is a free bet, nothing is paid
    bet = 0
    print("You Check!")
    return bet


def match(balance, bet, opposingBet, pot):
    # matches the opposing bet, e.g if player 1 puts 50, and p2 puts 75, to match p1 would pay the difference of 15
    takeaway = opposingBet - bet
    bet = opposingBet
    balance -= takeaway
    pot += takeaway
    print("You Matched Opposing Player's Bet! Pot Is Now At $" + str(pot))
    return balance, bet, opposingBet, pot


def raising(balance, bet, opposingBet, pot):
    # Raising means how much ONTOP of the opposing players bet
    while True:
        bet = int(input("How Much Do You Wish To RAISE: "))
        bet += opposingBet

        # Different scenarios about the bet amount
        if bet > balance:
            print("You Cannot Raise More Than You Have!")
        elif bet == balance:
            print("ALL IN")
            balance -= bet
            pot += bet
            print("YOU ARE ALL IN. Pot is at $" + str(pot))
            break
        else:
            balance -= bet
            pot += bet
            print("You Bet $" + str(bet) +
                  ". Pot is now at $" + str(pot))
            break

    return balance, bet, opposingBet, pot


def bet(balance, opposingBalance, bet, opposingBet, pot):
    # Function that houses all other functions internally, asks each player their move and calls the apporpiate function
    while True:
        while True:
            # PLAYER 1
            ask = input(
                "\n\n" + "Player 1, Do You Want To Fold, Match, Raise, or Check? Enter (f/m/r/c): ").lower()

            if ask == "f":
                opposingBalance, pot = fold(opposingBalance, pot)
                break

            elif ask == "m":
                if bet <= 0 and opposingBet <= 0:
                    print(
                        "Cannot Match, Please Raise, Fold, or Check")
                elif bet == opposingBet:
                    print("You Matched Opposing Player's Bet!")
                else:
                    balance, bet, opposingBet, pot = match(
                        balance, bet, opposingBet, pot)
                    break

            elif ask == "r":
                balance, bet, opposingBet, pot = raising(
                    balance, bet, opposingBet, pot)
                break

            elif ask == "c":
                if opposingBet != 0:
                    print(
                        "Cannot Check If Opponent Didn't Check! Please Raise, Match, or Fold")
                else:
                    bet = check(bet)
                    break

            print("Action Unavailable or Invalid Input; Try Again")

        # If player 1 folds, player 2 doesn't need to bet
        while ask != "f":
            # PLAYER 2
            ask = input(
                "\n\n" + "Player 2, Do You Want To Fold, Match, Raise, or Check? Enter (f/m/r/c): ").lower()

            if ask == "f":
                balance, pot = fold(balance, pot)
                break

            elif ask == "m":
                if opposingBet == bet:
                    print("You Matched Opposing Player's Bet!")
                else:
                    opposingBalance, opposingBet, bet, pot = match(
                        opposingBalance, opposingBet, bet, pot)
                break

            elif ask == "r":
                opposingBalance, opposingBet, bet, pot = raising(
                    opposingBalance, opposingBet, bet, pot)
                break

            elif ask == "c":
                if bet != 0:
                    print(
                        "Cannot Check If Opponent Didn't Check! Please Raise, Match, or Fold")
                else:
                    opposingBet = check(opposingBet)
                    break

            print("Action Unavailable or Invalid Input; Try Again")

        # BETTING only ends when bets are equal, or if one of the player's fold their cards
        if bet == opposingBet:
            break
        elif ask == "f":
            break

    return balance, opposingBalance, bet, opposingBet, pot
