import getpass
play = True
player1Points = 0
player2Points = 0
while play:
    counter = 8 #amount of lives the guesser has
    guesser = input("Is Player 1 or Player 2 guessing? ") #word the other player thinks of
    guesser = guesser.title()
    #words = input("Please enter a word you would like people to guess: ") #word the other player thinks of
    words = getpass.getpass("Please enter a word you would like the other player to guess: ")
    if words.isalpha() and len(words) > 1 and guesser == "Player 1" : #checks the user has entered a word greater than 1 in length
        print("Player 2 has entered a word")
    elif words.isalpha() and len(words) > 1 and guesser == "Player 2" : #checks the user has entered a word greater than 1 in length
        print("Player 1 has entered a word")
    else: #if not a word entered will print out and exit program
        print("Please enter an actual word")
        exit()

    word = list(words) #will store word as a list so can loop through
    #print(word)
    points = len(words) #points is the amount user must guess
    count = 0 #counter
    holder = [] #empty array
    check = False #flag

    while counter > 0 and points>count: #as long as user has not used lives and they have not guessed the word
        guess = input("Please enter a single letter you believe could be included in the word: ") #user guesses
        for i in word: #loops through word
            #if word.count(i) ==
            if i == guess: #if i eqwuals guess will change flag to true, to decrease guess from counter
                check = True
                #print[(i)]
                if word.count(i) == 3: #dependant on how many times letter occurs will remove from list, will loop through until all gone
                    print("The Letter " +i+ " is included in the word 3 times and will now be removed")
                    count = count+1
                    #print(word(i))
                    holder.append(i)
                    word.remove(i)
                if word.count(i) == 2:
                    print("The Letter " +i+ " is included in the word 2 times and will now be removed")
                    count = count+1
                    #print(word[i])
                    holder.append(i)
                    word.remove(i)
                if word.count(i) == 1:
                    print("The Letter " +i+ " is included in the word once and will now be removed")
                    count = count+1
                    holder.append(i)
                    #print(word[i])
                    word.remove(i)

            else:
                print("Letter is not included in the word")

        if check == False:
            counter = counter -1

        check = False
        print("You have " +str(counter)+ " lives left")
        print("You have " +str(count)+ " point/s")
        print("The word has " +str(points)+ " letters")
        #print(word)
        print("Letter/s guessed correctly so far " +str(holder))
        lettersLeft = points - len(holder)
        print("You have " +str(lettersLeft)+ " letters left to guess")
        print("---------------------------------------------")

    if count == points and guesser == "Player 1": #will print out whether guessed word or not
        print("You successfully guessed the word " +words+ " Player 1 has now gained a point")
        player1Points = player1Points +1
        print("Player 1 has " +str(player1Points)+ " points")
        print("Player 2 has " +str(player2Points)+ " points")
    elif count == points and guesser == "Player 2": #will print out whether guessed word or not
        print("You successfully guessed the word " +words+ " Player 2 has now gained a point")
        player2Points = player2Points +1
        print("Player 1 has " +str(player1Points)+ " points")
        print("Player 2 has " +str(player2Points)+ " points")
    elif counter < 1 and guesser == "Player 1": #will print out whether guessed word or not
        print("Player 1 did not guess the word " +words+ " Player 2 has now gained a point")
        player2Points = player2Points +1
        print("Player 1 has " +str(player1Points)+ " points")
        print("Player 2 has " +str(player2Points)+ " points")
    else :
        print("Player 2 did not guess the word " +words+ "! Player 1 has now gained a point")
        player1Points = player1Points +1
        print("Player 1 has " +str(player1Points)+ " points")
        print("Player 2 has " +str(player2Points)+ " points")


    done = True
    while done:
        playAgain = input("Do you want to play again, type yes or no: ")
        playAgain = playAgain.lower()
        if playAgain == "no" and player1Points > player2Points:
            play = False
            done = False
            print("Game over, Player 1 wins with " +str(player1Points)+ " points")
        elif playAgain == "no" and player2Points > player1Points:
            play = False
            done = False
            print("Game over, Player 2 wins with " +str(player2Points)+ " points")
        elif playAgain == "no" and player2Points == player1Points:
            play = False
            done = False
            print("Game over, Player 1 and Player 2 both have " +str(player2Points)+ " points, therefore the game is a draw")
        elif playAgain == "yes":
            done = False
            print("Next game is starting now")
        else:
            print("Please enter a valid input, yes or no ")
