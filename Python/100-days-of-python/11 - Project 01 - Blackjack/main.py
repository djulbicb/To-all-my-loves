#%%
# sum()
# [].remove() uklanja prvi takav clan

import random

logo = """
>>>>>>>>>>>> BLACK JACK <<<<<<<<<<<<<
"""
userWinEnd = """
------------ USER WIN END ------------
"""
pcWinEnd = """
------------ PC WIN END ------------
"""
tieEnd = """
------------ TIE END ------------
"""

userCards = []
pcCards = []

def getCard():
    """
    Returns card from the deck
    """
    cardDeck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cardDeck)

def printDeck(cardDeck, ownerName, hideCardsIndex = -1):
    cards = ""
    for i in range(len(cardDeck)):
        card = cardDeck[i]
        if hideCardsIndex >= 0 and i >= hideCardsIndex:
            cards = cards + "_ "
        else:
            cards = cards + (str(card) + " " )
    print(f"{ownerName} deck: {cards}")

def getScore(deck, aceIsOne = False):
    if (len(deck) == 2 and sum(deck) == 21):
        return 21

    copy = deck.copy()
    if (aceIsOne == True and (11 in copy)):

        idx = copy.index(11);
        # print("Index was " + str(idx) + " " + str(copy))
        copy[idx] = 1;

    total = 0
    for card in copy:
        total += card

    if total > 21 and (11 in copy):
        return getScore(copy, True)
    return total

def userTurn():
    askForNextCard = True
    while askForNextCard:
        nextMove = input("Type 'y' to get another card or 'n' to pass: ") # 'n'
        if nextMove == 'y':
            userCards.append(getCard())
            printDeck(userCards, "My")
            if (getScore(userCards) >= 21):
                askForNextCard = False
        elif nextMove == 'n':
            askForNextCard = False
        else:
            print("Wrong choice. Type 'y' or 'n'")

def pcTurn():
    askForNextCard = getScore(pcCards) < 16
    while askForNextCard:
        pcCards.append(getCard())
        askForNextCard = getScore(pcCards) < 16


def dealCards():
    for i in range(0,2):
        userCards.append(getCard())
        pcCards.append(getCard())

def playGame():
    dealCards()

    printDeck(userCards, "Your")
    printDeck(pcCards, "PC", 1)
    print("---")

    if (getScore(pcCards) == 21):
        print(pcWinEnd)
        return

    userTurn();

    printDeck(userCards, "Your final")
    printDeck(pcCards, "PC")
    print("---")

    pcTurn()

    printDeck(userCards, "Your final")
    printDeck(pcCards, "PC final")
    print("---")

def printWinner():
    if (pcScore == 21):
        print(pcWinEnd)
    elif (userScore == 21):
        print(userWinEnd)
    elif (userScore > 21 and pcScore <=21 ):
        print(pcWinEnd)
    elif (pcScore > 21 and userScore <=21 ):
        print(userWinEnd)
    elif (pcScore > userScore):
        print(pcWinEnd)
    elif ( userScore > pcScore):
        print(userWinEnd)
    elif (userScore == pcScore):
        print(tieEnd)
    else:
        print("Unexpected output: ", userCards, pcCards)


# MAIN
# ------------------------------------------------------------------
play = True
while play:
    print(logo)

    playGame()

    userScore = getScore(userCards)
    pcScore = getScore(pcCards)
    print("Your final is " + str(userScore))
    print("PC final is " + str(pcScore))

    printWinner()

    if (input("Another game?: ") == 'y'):
        userCards = []
        pcCards = []
    else:
        print("Goodbye")
        play = False





