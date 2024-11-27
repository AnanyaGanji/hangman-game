import random

def wordGenerate() :
    l = ["hello", "cycle", "machine", "blanket", "movie", "space", "train", "metro"]
    word = random.choice(l)
    # print(word)
    return word


def blanks(word) :
    guess = []
    for i in range(len(word)) :
        guess.append('_')
    print(guess)
    return guess


def checkBlankSpaces(guess) :
    space = 0
    for i in guess :
        if i == '_' :
            space += 1
            return
    return space
    

def figure(chances) :
    if chances == 6 :
        print("    +----+")
        print("    |    |")
        print("         |")
        print("         |")
        print("         |")
    
    elif chances == 5 :
        print("    +----+")
        print("    |    |")
        print("    0    |")
        print("         |")
        print("         |")

    elif chances == 4 :
        print("    +----+")
        print("    |    |")
        print("    0    |")
        print("    |    |")
        print("         |")

    elif chances == 3 :
        print("    +----+")
        print("    |    |")
        print("    0    |")
        print("   /|    |")
        print("         |")

    elif chances == 2 :
        print("    +----+")
        print("    |    |")
        print("    0    |")
        print("   /|\   |")
        print("         |")

    elif chances == 1 :
        print("    +----+")
        print("    |    |")
        print("    0    |")
        print("   /|\   |")
        print("   /     |")

    elif chances == 0 :
        print("    +----+")
        print("    |    |")
        print("    0    |")
        print("   /|\   |")
        print("   / \   |")
    

def guessLetter(word, guess, chances) :
    letter = input("Guess a letter: ")
    c = 0
    flag = 0
    for i in word :
        # print(i)
        if i == letter :
            guess[c] = letter
            flag = 1    
            c += 1
        else :
            c += 1
            # print("No such letter")

    print(guess)
    if flag == 0 :
        chances += 1 
    return chances



#generate a random word
word = wordGenerate()

#create list with blank spaces to guess the word
guess = blanks(word)

chances = 0
while chances < 6 :
    #guess a letter and check if it is present in the word
    chances = guessLetter(word, guess, chances)

    # checking if the word is completed or not i.e., if there any blanks left in guess 
    space = checkBlankSpaces(guess)

    if space == 0 :
        print("You Guessed it!!!!!")
        break
    figure(6-chances)
    print("You have", 6 - chances, "chances left")
    
if chances == 6 :
    print("You loose")
    print("The word is", word)