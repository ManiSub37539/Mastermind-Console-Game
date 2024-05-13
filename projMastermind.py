#Name: Mani Subramani
#Due Date: 5/2/2023
#Project: Mastermind
#Objective: Computer chooses hidden colors, human guesses the hidden colors

import random

#function to generate random numbers within specified seed
#random numbers get appended to a secret list used by computer
def getRandom():
    secretList = []
    secret = []
    i = 0
    
    while i < 4:
        seedValue = random.randint(0,5)
        secretList.append(seedValue)
        i +=1
    
    return secretList

#function which converts the numerical value of player guesses to corresponding colors
def guessConv(guess):
    guessList = []
    
    for j in range(len(guess)):
        if guess[j] == 0:
            guessList.append("red")
        if guess[j] == 1:
            guessList.append("orange")
        if guess[j] == 2:
            guessList.append("yellow")
        if guess[j] == 3:
            guessList.append("green")
        if guess[j] == 4:
            guessList.append("blue")
        if guess[j] == 5:
            guessList.append("purple")
    return guessList

#function which displays the initial game screen and player guess inputs
def playGame():
    print("-----------------------------")
    print("Make a guess of four colors: ")
    print("0  -  red")
    print("1  -  orange")
    print("2  -  yellow")
    print("3  -  green")
    print("4  -  blue")
    print("5  -  purple")
    print("-----------------------------")
    
    i = 0
    numGuessList = []
    guessList = []
    valid = False

    #while loop checks whether the player inputs valid numerical values/characters
    while valid == False:
        #exception handling for value error
        try:
            #while loop to append numerical guess values to list
            while i < 4:
                guessValue = int(input("Guess color: "))
                if(guessValue <= 5):
                    numGuessList.append(guessValue)
                    i +=1
                else:
                    print("Invalid guess, try again: ")
            if i == 4:
                valid = True
        except ValueError:
            print("Invalid number, try again:")

    #calls previous guessConv function to convert numerical guess values to corresponding colors
    guessList = guessConv(numGuessList)        
    
    print("-----------------------------")
    print("Your guess is:")
    print(guessList)
    print(" ")
        
    return guessList, numGuessList

#function to check whether the guesses are correct or not and provides appropriate clues
def checkGuess(guessList, numGuessList, secretList):
    
    checkCounter = 0
    
    index = -5
    indexJ = -5
    indexK = -5
    clueList = []
    temp = []

    #Values from secret list is appended to a temporary list used in place of the secret list to check guesses
    #This ensures that the actual secret list used throughout runtime of the game remains constant   
    for i in range(len(secretList)):
        temp.append(secretList[i])

    #for loop checks for same values in same positions and returns 2's
    for i in range(len(numGuessList)):
        if(numGuessList[i] == temp[i] and index != i):
            clueList.append(2)
            temp[i] = -1
            numGuessList[i] = -2
            checkCounter = 1
            index = i
            
    #for loop checks for same values in different positions and returns 1's
    for k in range(len(numGuessList)):
        for j in range(len(temp)):
            if(numGuessList[k] == temp[j] and index != k):
                clueList.append(1)
                temp[j] = -1
                index = k
    clueList.sort()
    return clueList

#unction to check for win condition and returns a boolean value used in main()
def checkWin(clueList, secretList):
    if clueList == [2, 2, 2, 2]:
        checkWinning = True    
    else:
        print("Your clue is: ", clueList)
        print(" ")
        checkWinning = False
           
    return checkWinning


#main() calls other functions and contains endgame conditions                                                                   
def main(seedIn):
    checkWinning = False
    endScreen = False
    seed = random.seed(seedIn)
    secretList = getRandom()
    playAgain = True

    #outer while loop used during game's runtime
    while playAgain == True:
        print("The secret code has been chosen. You have 10 tries to guess the code.")
        print(" ")
        guessCounter = 10
        
        #inner while loop used when the number of guesses > 0
        while guessCounter > 0:
            guessList, numGuessList = playGame()
            clueList = checkGuess(guessList, numGuessList, secretList)
            checkWinning = checkWin(clueList, secretList)
            guessCounter -=1

            #checks whether player should keep going or ran out of guesses, or they guessed right
            if checkWinning == False:
                if guessCounter > 0:
                    print("You have", guessCounter, "guesses left")
                elif guessCounter == 0:
                    print("No more guesses, the hidden colors were:")
                    print(" ")
                    print(guessConv(secretList))
                    print(" ")
                    endScreen = True
                    break
            
            elif checkWinning == True:
                print("Correct! You finished in ", 10-guessCounter, " guesses")
                print(" ")
                endScreen = True
                break
            
        #when game is over and the end screen is displayed
        if endScreen == True:
            #exception handling
            try:
                prompt = input("Would you like to play again? (Y/N)")
                
                #if player presses n, exits playAgain while loop
                if prompt == "N" or prompt == "n":
                    print(" ")
                    print("Thank you for playing.  Good-bye!")
                    endScreen = False
                    playAgain = False
                #elif player presses 'y', cycles back to the start of while loop
                elif prompt == "Y" or prompt == "y":
                    endScreen = False
                    secretList = getRandom()
            
            except EOFError:
                break
            
   
        



