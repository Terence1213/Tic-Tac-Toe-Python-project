import random
import time

table = [{"A1": "-", "A2": "-", "A3": "-"},
             {"B1": "-", "B2": "-", "B3": "-"},
             {"C1": "-", "C2": "-", "C3": "-"}]

def printTable(table):

    print("\n-----------------------------------")
    values = ["A", "B", "C"]
    valueNum = 0
    print("  1 2 3")

    #For each dictionary in the table, the program is printing each key value of each dictionary.
    for row in table:
        print(values[valueNum], end = " ")
        valueNum += 1
        for key in row:
            print(row.get(key), end = " ")
        print()

def won(table):

    printTable(table)
    print("\nYou Won!")
    return True

def lost(table):

    printTable(table)
    print("\nYou Lost!")
    return True

def decideWinner(player, table):

    #Used for checking if the game has ended.
    gameWon = False

    #Used for checking whether the player stays as won, or if he loses and playerWon is set to false.
    playerWon = True

    #Converting the table from rows, to columns, so that column wins can be checked.
    columns = [[table[0]["A1"], table[1]["B1"], table[2]["C1"]],
               [table[0]["A2"], table[1]["B2"], table[2]["C2"]],
               [table[0]["A3"], table[1]["B3"], table[2]["C3"]]]


    #For each row in the table, if not all values are the same (and not blank), the "player" wins.
    for row in table:
        #Previous key is the value of the previous key in the row. This variable is used to turn playerWon to false
        #If any keys on the same row are different from each other.
        playerWon = True

        previousKey = ""

        #As already stated, if any keys are different from one another, playerWon is set to False.
        for key in row:
            #If any keys are different from each other, or one of the keys is blank, then the player doesn't win.
            if (previousKey != "" and previousKey != row.get(key)) or row.get(key) == "-":
                playerWon = False
            previousKey = row.get(key)

        #If playerWon is set to true, then the winner is stated.
        if playerWon == True:
            if player == "X":
                gameWon = won(table)
                break
            elif player == "O":
                gameWon = lost(table)
                break

    #If all values of a column are the same, (and not blank) then the winner is stated.
    for column in columns:
        if column[0] == player and column[0] == column[1] == column[2]:
            if player == "X":
                gameWon = won(table)
            elif player == "O":
                gameWon = lost(table)

    #Checks for diagonal wins. - Top left to bottom right
    if table[0]["A1"] == player and table[0]["A1"] == table[1]["B2"] == table[2]["C3"]:
        if player == "X":
            gameWon = won(table)
        elif player == "O":
            gameWon = lost(table)

    #Checks for diagonal wins - Top right to bottom left.
    if table[0]["A3"] == player and table[0]["A3"] == table[1]["B2"] == table[2]["C1"]:
        if player == "X":
            gameWon = won(table)
        elif player == "O":
            gameWon = lost(table)

    return gameWon

def startTurn(player, isAI, isTie):

    print()
    printTable(table)
    turnComplete = False

    # inputValid is mainly used so that if the user enters an invalid input, rather than an already filled slot,
    # rather than outputting "already filled slot", the program outputs "invalid input".
    inputValid = False

    #Putting all the valid coordinate choices in a list so that a random one of them can be chosen for the AI.
    choiceList = list()

    for row in table:
        for key in row:
            choiceList.append(key)

    #An animation for each AI turn is held if the player chooses AI mode.
    if player == "O" and isAI == True:
        for i in range(1, 3):
            print("\n" * 50)
            printTable(table)
            print("Computer is choosing", end="")
            for i in range(0,3):
                time.sleep(0.5)
                print(".", end="")
            time.sleep(0.25)

    # If an already filled space or an invalid input are chosen, the user is re - asked to enter his input (even the AI)
    while inputValid == False or turnComplete == False:

        if player == "X":
            playerChoice = input(
                '\nPlayer 1: please enter a coordinate of your choice! (which is unchosen) - (A1, A2, A3 etc..): ').upper()

        elif player == "O" and isAI == True:
            playerChoice = random.choice(choiceList)

        elif player == "O" and isAI == False:
            playerChoice = input(
                '\nPlayer 2: please enter a coordinate of your choice! (which is unchosen) - (A1, A2, A3 etc..): ').upper()

        #Used for modifying the "table" variable.
        rowNum = 0

        #Used for checking for a tie. If all 9 coordinates are filled, and neither player has won yet, then the result
        #Is a tie.
        nonBlankAmount = 0

        for row in table:
            for key in row:
                if row.get(key) != "-":
                    nonBlankAmount += 1

                # If the key, in the loop is equal to that of the player's choice, and it's empty, then the key's value
                # is filled with "X" or "O" - depending on who's turn it is.
                if key == playerChoice and row.get(key) == "-":
                    table[rowNum][key] = player
                    turnComplete = True
                    inputValid = True

                # If the key is a valid coordinate in the table, but is already filled, an error message is displayed.
                elif key == playerChoice and row.get(key) != "-":
                    inputValid = True
                    print("That coordinate is already filled!")

            rowNum += 1

        if nonBlankAmount >= 8:
            isTie = True
            printTable(table)
            print("The match is a tie!")
            break

        # If the input wasn't in the table range, the below error message is displayed.
        # This is because that if inputValid is false, then the key which the player enters, is never
        # equal to any of the keys which are existent in the table.
        if inputValid == False:
            print("Invalid input!, please enter a valid coordinate (A1, A2, A3 etc..): ")

    return isTie

def clearTable():

    for row in table:
        for key in row:
            row[key] = "-"

def startGame():

    clearTable()

    #Defines if player 1 ("X") or player 2 ("O") starts first
    order = random.randrange(0, 2)

    isAI = False

    while True:
        choice = int(input("\n\nEnter 1. = Play vs AI\nEnter 2. = Play vs Friend\nEnter your choice (1 - 2): "))
        if choice == 1:
            isAI = True
            break
        elif choice == 2:
            break

    isTie = False

    if order == 0:
        while True:
            #"X" plays his turn, and if with his turn he wins, the round ends, since the while loop stops.
            startTurn("X", isAI, isTie)
            if decideWinner("X", table) == True or isTie == True:
                break

            #"O" plays his turn, and if with his turn he wins, the round ends, since the while loop stops.
            startTurn("O", isAI, isTie)
            if decideWinner("O", table) == True or isTie == True:
                break
    else:
        while True:
            #"O" plays his turn, and if with his turn he wins, the round ends, since the while loop stops.
            isTie = startTurn("O", isAI, isTie)
            if decideWinner("O", table) == True or isTie == True:
                break

            #"X" plays his turn, and if with his turn he wins, the round ends, since the while loop stops.
            isTie = startTurn("X", isAI, isTie)
            if decideWinner("X", table) == True or isTie == True:
                break

def menu():
    while True:
        print("\n-----------------------------------------------")
        choice = int(input("\nEnter 1. = Play\nEnter 2. = Quit\nEnter your choice (1 - 2): "))

        if choice == 1:
            startGame()
        elif choice == 2:
            break

menu()