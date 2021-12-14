# MOST OF THE CODE IS REPETITIVE AS MANY WINNING CONDITIONS REQUIRE SIMILAR CRITERIA
# E.G ROYAL FLUSH, STRAIGHT FLUSH, FLUSH, SIMILAR CODE TO FIND IF ITS A FLUSH


def playerBoard(boardx, boardy, handx, handy):
    # Function to append player hands to board -> 5 community cards + 2 player hand cards
    for i in handx:
        boardx.append(i)

    for j in handy:
        boardy.append(j)
    return boardx, boardy, handx, handy


def sort(board, key):
    # sorts the final hand/board from greatest/highest value to lowest value
    # bubble sort - from POTD
    # the board[k].split(" ")[0] is to change string values to int values using a dictionary
    # more specifically "King" -> 13, "Queen" -> 12, "Jack" -> 11, etc.
    x = len(board)
    for i in board:
        for k in range(x-1):
            if key[board[k].split(" ")[0]] < key[board[k+1].split(" ")[0]]:
                board[k], board[k+1] = board[k+1], board[k]

    return board, key


def isRoyalFlush(board, royalflush):
    # Checks if all cards are the same suit by adding up suit totals
    Htotal, Stotal, Ctotal, Dtotal = 0, 0, 0, 0
    x = 0
    for i in board:
        i = i.split(" ")
        if i[-1] == "Hearts":
            Htotal += 1
        elif i[-1] == "Spades":
            Stotal += 1
        elif i[-1] == "Clubs":
            Ctotal += 1
        elif i[-1] == "Diamonds":
            Dtotal += 1

    # if >= 5 more is totaled for a specific suit, it is considered a flush
    # That is one of the criteria for a royal FLUSH
    if Htotal >= 5 or Stotal >= 5 or Ctotal >= 5 or Dtotal >= 5:
        # This For Loop checks for the required [10, Jack, Queen, King, Ace]
        for i in board:
            i = i.split(" ")
            if Htotal >= 5:
                if i[-1] == "Hearts":
                    if i[0] == "10":
                        x += 1
                    elif i[0] == "Jack":
                        x += 1
                    elif i[0] == "Queen":
                        x += 1
                    elif i[0] == "King":
                        x += 1
                    elif i[0] == "Ace":
                        x += 1
            elif Stotal >= 5:
                if i[-1] == "Spades":
                    if i[0] == "10":
                        x += 1
                    elif i[0] == "Jack":
                        x += 1
                    elif i[0] == "Queen":
                        x += 1
                    elif i[0] == "King":
                        x += 1
                    elif i[0] == "Ace":
                        x += 1
            elif Ctotal >= 5:
                if i[-1] == "Clubs":
                    if i[0] == "10":
                        x += 1
                    elif i[0] == "Jack":
                        x += 1
                    elif i[0] == "Queen":
                        x += 1
                    elif i[0] == "King":
                        x += 1
                    elif i[0] == "Ace":
                        x += 1
            elif Dtotal >= 5:
                if i[-1] == "Diamonds":
                    if i[0] == "10":
                        x += 1
                    elif i[0] == "Jack":
                        x += 1
                    elif i[0] == "Queen":
                        x += 1
                    elif i[0] == "King":
                        x += 1
                    elif i[0] == "Ace":
                        x += 1

    if x == 5:
        royalflush = True

    return board, royalflush


def isStraightFlush(board, key, straightflush, cardHigh):
    # this function checks for a straight flush
    board, key = sort(board, key)

    # Checks the number of each card and enters a nested loop
    # to check if the next card is in sequential order
    # also notes the suit and ensures that the suit is the same when checking if in sequential order
    for i in range(0, 3):
        num = key[board[i].split(" ")[0]]
        cardHigh = num
        suit = board[i].split(" ")[-1]
        total = 1

        for j in range(i+1, len(board)):
            first = key[board[j].split(" ")[0]]
            last = board[j].split(" ")[-1]

            if num-1 == first and suit == last:
                num -= 1
                total += 1

        # if the total is >= 5, the requirement for a straight flush, it returns the check as True
        if total >= 5:
            straightflush = True
            break

    return board, key, straightflush, cardHigh


def isFourKind(board, key, fourkind, cardHigh):
    # Checks the number of each card and enters a nested loop
    # to check if the next card has the same value, if it does it will add to the total
    for i in range(0, 4):
        num = key[board[i].split(" ")[0]]
        total = 1  # starts with one because we start with the first card

        for j in range(i+1, len(board)):
            first = key[board[j].split(" ")[0]]

            if num == first:
                total += 1

        if total >= 4:
            fourkind = True
            cardHigh = num
            return board, key, fourkind, cardHigh

    return board, key, fourkind, cardHigh


def isFullHouse(board, key, fullhouse, cardHigh):
    # function to check if a 2 pair and 3 pair is present at the same time
    board, key = sort(board, key)

    for i in range(len(board)-1):
        num = key[board[i].split(" ")[0]]
        total = 1

        for j in range(i+1, len(board)):
            first = key[board[j].split(" ")[0]]

            if num == first:
                total += 1

        if total >= 2:
            break

    # enters another if statement if there's a pair of 2 or greater
    if total >= 2:
        for i in range(len(board)-1):
            num1 = key[board[i].split(" ")[0]]
            total1 = 1

            if num1 != num:
                for j in range(i+1, len(board)):
                    first = key[board[j].split(" ")[0]]

                    if num1 == first:
                        total1 += 1

                if total1 >= 2:
                    break

    # if it finds that both totals are >= 2/3 then there's a pair of 2 and 3
    if total >= 2 and total1 >= 3:
        fullhouse = True
        cardHigh = num

    elif total >= 3 and total1 >= 2:
        fullhouse = True
        cardHigh = num1

    return board, key, fullhouse, cardHigh


def isFlush(board, key, flush, cardHigh):

    # Checks if all cards are the same suit by adding up suit totals
    Htotal, Stotal, Ctotal, Dtotal = 0, 0, 0, 0
    for i in board:
        i = i.split(" ")
        if i[-1] == "Hearts":
            Htotal += 1
        elif i[-1] == "Spades":
            Stotal += 1
        elif i[-1] == "Clubs":
            Ctotal += 1
        elif i[-1] == "Diamonds":
            Dtotal += 1

    # if >= 5 more is totaled for a specific suit, it is considered a flush
    if Htotal >= 5 or Stotal >= 5 or Ctotal >= 5 or Dtotal >= 5:
        flush = True

    # Sorts Board - To check for highest card in flush
    board, key = sort(board, key)

    for i in board:
        i = i.split(" ")
        if Htotal >= 5:
            if i[-1] == "Hearts":
                cardHigh = i[0]
                break

        elif Stotal >= 5:
            if i[-1] == "Spades":
                cardHigh = i[0]
                break

        elif Ctotal >= 5:
            if i[-1] == "Clubs":
                cardHigh = i[0]
                break

        elif Dtotal >= 5:
            if i[-1] == "Diamonds":
                cardHigh = i[0]
                break

    return board, key, flush, cardHigh


def isStraight(board, key, straight, cardHigh):
    # Checks the number of each card and enters a nested loop
    # to check if the next card is in sequential order | similar code to straightflush
    board, key = sort(board, key)

    for i in range(0, 3):
        num = key[board[i].split(" ")[0]]
        cardHigh = num
        total = 1

        for j in range(i+1, len(board)):
            first = key[board[j].split(" ")[0]]

            if num-1 == first:
                num -= 1
                total += 1

        if total >= 5:
            straight = True
            return board, key, straight, cardHigh

    return board, key, straight, cardHigh


def isThreeKind(board, key, threekind, cardHigh):
    # similar code to 4 of a kind, however, this time the total only needs to be >= 3 for it to be a 3 of a kind
    for i in range(0, 4):
        num = key[board[i].split(" ")[0]]
        total = 1

        for j in range(i+1, len(board)):
            first = key[board[j].split(" ")[0]]

            if num == first:
                total += 1

        if total >= 3:
            threekind = True
            cardHigh = num
            return board, key, threekind, cardHigh

    return board, key, threekind, cardHigh


def isTwoPair(board, key, twopair, cardHigh):
    # similar to Full House Code, but instead of pairs of 2 and 3, it only needs pairs of 2 and 2
    board, key = sort(board, key)

    for i in range(len(board)-1):
        num = key[board[i].split(" ")[0]]
        total = 1

        for j in range(i+1, len(board)):
            first = key[board[j].split(" ")[0]]

            if num == first:
                total += 1

        if total == 2:
            break

    if total == 2:
        for i in range(len(board)-1):
            num1 = key[board[i].split(" ")[0]]
            total1 = 1

            if num1 != num:
                for j in range(i+1, len(board)):
                    first = key[board[j].split(" ")[0]]

                    if num1 == first:
                        total1 += 1

                if total1 == 2:
                    break

    if total == 2 and total1 == 2:
        twopair = True
        if num1 > num:
            cardHigh = num1
        elif num > num1:
            cardHigh = num

    return board, key, twopair, cardHigh


def isOnePair(board, key, onepair, cardHigh):
    # similar to Full House Code and two pair, but instead it only needs 1 pairs
    board, key = sort(board, key)

    for i in range(len(board)-1):
        num = key[board[i].split(" ")[0]]
        total = 1

        for j in range(i+1, len(board)):
            first = key[board[j].split(" ")[0]]

            if num == first:
                total += 1

        if total == 2:
            break

    if total == 2:
        onepair = True
        cardHigh = num

    return board, key, onepair, cardHigh


def isHighCard(board, key, cardHigh):
    # sort the board and check if the last card is an Ace, if its not then the first index is the highest card (a.k.a high Card)
    board, key = sort(board, key)

    first = board[0].split(" ")[0]
    last = board[-1].split(" ")[0]

    if last == "Ace":
        cardHigh = key[last]
    else:
        cardHigh = key[first]

    return board, key, cardHigh


def winner(board, key, var, cardHigh, points):
    # function to check all winning conditions in one internal function
    check = None

    # Royal Flush
    board, check = isRoyalFlush(board, check)
    if check:
        var = "Royal Flush"
        points = 10
        return board, key, var, cardHigh, points

    # Straight Flush
    board, key, check, cardHigh = isStraightFlush(board, key, check, cardHigh)
    if check:
        var = "Straight Flush"
        points = 9
        return board, key, var, cardHigh, points

    # Four of a Kind
    board, key, check, cardHigh = isFourKind(board, key, check, cardHigh)
    if check:
        var = "Four of a Kind"
        points = 8
        return board, key, var, cardHigh, points

    # Full House
    board, key, check, cardHigh = isFullHouse(board, key, check, cardHigh)
    if check:
        var = "Full House"
        points = 7
        return board, key, var, cardHigh, points

    # Flush
    board, key, check, cardHigh = isFlush(board, key, check, cardHigh)
    if check:
        var = "Flush"
        points = 6
        return board, key, var, cardHigh, points

    # Straight
    board, key, check, cardHigh = isStraight(board, key, check, cardHigh)
    if check:
        var = "Straight"
        points = 5
        return board, key, var, cardHigh, points

    # Three of a Kind
    board, key, check, cardHigh = isThreeKind(board, key, check, cardHigh)
    if check:
        var = "Three of a Kind"
        points = 4
        return board, key, var, cardHigh, points

    # Two Pair
    board, key, check, cardHigh = isTwoPair(board, key, check, cardHigh)
    if check:
        var = "Two Pair"
        points = 3
        return board, key, var, cardHigh, points

    # One Pair
    board, key, check, cardHigh = isOnePair(board, key, check, cardHigh)
    if check:
        var = "One Pair"
        points = 2
        return board, key, var, cardHigh, points

    # High Card
    board, key, cardHigh = isHighCard(board, key, cardHigh)
    if True:
        var = "High Card"
        points = 1
        return board, key, var, cardHigh, points
