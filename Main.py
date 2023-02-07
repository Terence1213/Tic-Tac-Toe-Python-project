#Make a tic - tac - toe game.
#Plan:
# Make the game more readable and user friendly.
# WINNING DECISION MAKING ISN'T WORKING CORRECTLY
# Then I start working on the AI.
# Bonus feature: Make it so whoever starts the game first is random.
import random

table = [{"A1": "-", "A2": "-", "A3": "-"},
             {"B1": "-", "B2": "-", "B3": "-"},
             {"C1": "-", "C2": "-", "C3": "-"}]

def printTable(table):
    print("\n-----------------------------------")
    values = ["A", "B", "C"]
    valueNum = 0
    print("  1 2 3")
    for row in table:
        print(values[valueNum], end = " ")
        valueNum += 1
        for key in row:
            print(row.get(key), end = " ")
        print()

def decideWinner(player, table):
    gameWon = False
    playerWon = True
    #Converting the table from rows, to columns, so that column wins can be checked.
    columns = [[table[0]["A1"], table[1]["B1"], table[2]["C1"]],
               [table[0]["A2"], table[1]["B2"], table[2]["C2"]],
               [table[0]["A3"], table[1]["B3"], table[2]["C3"]]]


    #For each row in the table, if not all values are the same (and not blank), the "player" wins.
    for row in table:
        #Previous key is the value of the previous key in the row. This variable is used to turn playerWon to false
        #If any keys on the same row are different from each other.
        previousKey = ""
        #As already stated, if any keys are different from one another, playerWon is set to False.
        for key in row:
            if previousKey != "" and previousKey != row.get(key):
                playerWon = False
            previousKey = row.get(key)

        #If playerWon is set to true, then the winner is stated.
        if playerWon == True:
            if player == "X":
                printTable(table)
                print("\nYou won!")
                gameWon = True
                break
            elif player == "O":
                printTable(table)
                print("\nYou lost!")
                gameWon = True
                break

    #If all values of a column are the same, (and not blank) then the winner is stated.
    for column in columns:
        #Column one of the 3 columns in the variable "columns"
        if column[0] == player and column[0] == column[1] == column[2]:
            if player == "X":
                printTable(table)
                gameWon = True
                print("\nYou won!")
            elif player == "O":
                printTable(table)
                gameWon = True
                print("\nYou lost!")

    #Checks for diagonal wins. - Top left to bottom right
    if table[0]["A1"] == player and table[0]["A1"] == table[1]["B2"] == table[2]["C3"]:
        if player == "X":
            printTable(table)
            gameWon = True
            print("\nYou won!")
        elif player == "O":
            printTable(table)
            gameWon = True
            print("\nYou lost!")

    #Checks for diagonal wins - Top right to bottom left.
    if table[0]["A3"] == player and table[0]["A3"] == table[1]["B2"] == table[2]["C1"]:
        if player == "X":
            printTable(table)
            gameWon = True
            print("\nYou won!")
        elif player == "O":
            printTable(table)
            gameWon = True
            print("\nYou lost!")

    return gameWon

def startTurn(player):
    print()
    printTable(table)
    turnComplete = False
    # inputValid is mainly used so that if the user enters an invalid input, rather than an already filled slot,
    # rather than outputting "already filled slot", the program outputs "invalid input".
    inputValid = False
    choiceList = list()
    for row in table:
        for key in row:
            choiceList.append(key)

    # If an already filled space or an invalid input are chosen, the code loops.
    while inputValid == False or turnComplete == False:

        if player == "X":
            playerChoice = input("Pease enter a coordinate of your choice! (which is unchosen) - (A1, A2, A3 etc..): ")
        elif player == "O":
            playerChoice = random.choice(choiceList)

        rowNum = 0
        for row in table:
            for key in row:
                # If the key, in the loop is equal to that of the player's choice, and it's empty, then the key's value
                # is filled.
                if key == playerChoice and row.get(key) == "-":
                    table[rowNum][key] = player
                    turnComplete = True
                    inputValid = True
                # If the key is a valid coordinate in the table, but is already filled, an error message is displayed.
                elif key == playerChoice and row.get(key) != "-":
                    inputValid = True
                    print("That coordinate is already filled!")
            rowNum += 1

        # If the input wasn't in the table range, the below error message is displayed.
        # This is because that if inputValid is false, then the key which the player enters, is never
        # equal to any of the keys which are existent in the table.
        if inputValid == False:
            print("Invalid input!, please enter a valid coordinate (A1, A2, A3 etc..")

def clearTable():
    for row in table:
        for key in row:
            row[key] = "-"

def startGame():

    clearTable()

    while True:
        startTurn("X")
        if decideWinner("X", table) == True:
            break
        startTurn("O")
        if decideWinner("O", table) == True:
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