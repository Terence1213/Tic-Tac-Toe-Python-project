#Make a tic - tac - toe game.
#Plan:
# FIX THE LOOPCOMPLETE AND TURNCOMPLETE VARIABLE NAMES (CURRENTLY VERY CONFUSING)
# Make it so the game is repeated until someone wins.
# Make the game more readable and user friendly.
# Then I start working on the AI.
# Bonus feature: Make it so whoever starts the game first is random.

table = [{"A1" : "-", "A2" : "-", "A3" : "-"},
         {"B1" : "-", "B2" : "-", "B3" : "-"},
         {"C1" : "-", "C2" : "-", "C3" : "-"}]

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
    #Converting the table from rows, to columns, so that column wins can be checked.
    columns = [[table[0]["A1"], table[1]["B1"], table[2]["C1"]],
               [table[0]["A2"], table[1]["B2"], table[2]["C2"]],
               [table[0]["A3"], table[1]["B3"], table[2]["C3"]]]

    #For each row in the table, if not all values are the same (and not blank), the "player" wins.
    for row in table:
        #Previous key is the value of the previous key in the row. This variable is used to turn playerWon to false
        #If any keys on the same row are different from each other.
        previousKey = ""
        playerWon = True

        #As already stated, if any keys are different from one another, playerWon is set to False.
        for key in row:
            if previousKey != "" and previousKey != row.get(key):
                playerWon = False
            previousKey = row.get(key)

        #If playerWon is set to true, then the winner is stated.
        if playerWon == True:
            if player == "X":
                print("You won!")
                break
            elif player == "O":
                print("You lost!")

    #If all values of a column are the same, (and not blank) then the winner is stated.
    for column in columns:
        #Column one of the 3 columns in the variable "columns"
        if column[0] == player and column[0] == column[1] == column[2]:
            if player == "X":
                print("You won!")
            elif player == "O":
                print("You lost!")

    #Checks for diagonal wins. - Top left to bottom right
    if table[0]["A1"] == player and table[0]["A1"] == table[1]["B2"] == table[2]["C3"]:
        if player == "X":
            print("You won!")
        elif player == "O":
            print("You lost!")

    #Checks for diagonal wins - Top right to bottom left.
    if table[0]["A3"] == player and table[0]["A3"] == table[1]["B2"] == table[2]["C1"]:
        if player == "X":
            print("You won!")
        elif player == "O":
            print("You lost!")


def startGame():
    printTable(table)
    turnComplete = False
    #loopComplete is mainly used so that if the user enters an invalid input, rather than an already filled slot,
    #rather than outputting "already filled slot", the program outputs "invalid input".
    loopComplete = False

    #If an already filled space or an invalid input are chosen, the code loops.
    while loopComplete == False or turnComplete == False :

        playerChoice = input("Pease enter a coordinate of your choice! (which is unchosen) - (A1, A2, A3 etc..")

        rowNum = 0
        for row in table:
            for key in row:
                #If the key, in the loop is equal to that of the player's choice, and it's empty, then the key's value
                #is filled.
                if key == playerChoice and row.get(key) == "-":
                    table[rowNum][key] = "X"
                    turnComplete = True
                    loopComplete = True
                #If the key is already filled an error message is displayed.
                elif key == playerChoice and row.get(key) != "-":
                    loopComplete = True
                    print("That coordinate is already filled!")
            rowNum += 1

        #If the input wasn't in the table range, the below error message is displayed.
        #This is because that if loopComplete is false, then the key which the player enters, is never
        #equal to any of the keys which are existent in the table.
        if loopComplete == False:
            print("Invalid input!, please enter a valid coordinate (A1, A2, A3 etc..")

    decideWinner("X", table)
    print()
    printTable(table)

def menu():
    while True:
        print("\n-----------------------------------------------")
        choice = int(input("\nEnter 1. = Play\nEnter 2. = Quit"))

        if choice == 1:
            startGame()
        elif choice == 2:
            break

menu()