# generate a (pseudo) random number (between 1 and 10)
import random
myNumber = random.randint(1, 10)
#print(myNumber)
score = 3

def getGuess():
    """Prompt user to guess an integer between 1 and 10"""
    return int(input("Guess my number (between 1 and 10): "))

while score > 0:
    # Ask user to guess a number (between 1 and 10)
    try:
        guessNumber = getGuess()
    except:
        print('Please enter an integer between 1 and 10')
        try:
            guessNumber = getGuess()
        except:
            print('Input Error')
            break
    print(guessNumber)

    # return if the number is greater than or less than user's input
    if (guessNumber == myNumber):
        print('Wow, You\'ve correctly guessed my Number! \nScore: ' + str(score))
        break
    else:
        if (score == 1):
            print("You've made too many incorrect guesses! You lose!")
            break
        print('That\'s not my number!, try again!')
    score -= 1
# If user fails to guess the correct number 3 times, the user loses. If they win the get a score based on how quickly they guessed the number
# 0 if Fail
# 1 if they get it on the third try
# 2 if they get it on the second try
# and 3 if they get it on the first try

