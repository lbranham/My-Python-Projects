
def userIntInput():
    """take user input for a number and determine if it's an integer"""
    while True:
        rawInput = input('\nEnter a whole number(or \'quit\' to exit): ')
                
        if rawInput == 'quit':
            raise SystemExit(0)
        
        try:
            rawInput = int(rawInput)
            return rawInput
            break
        except:
            print('\nMust Enter a whole number. Please try again')
            

def IsOddOrEven(integer):
    """determine if an integer is odd or even"""
    if integer % 2 == 0:    # all even numbers can be divided by two with no remainder; odd numbers will always have a remainder.
        print('\n{} is an Even number\n'.format(integer))
    else:
        print('\n{} is an Odd number\n'.format(integer))


def main():

    IsOddOrEven(userIntInput())

    
if __name__ == '__main__':
    main()
    
