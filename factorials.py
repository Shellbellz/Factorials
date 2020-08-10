'''
factorial.py

This program takes user input and then prints out the factorial
'''


def main():
    userNumber = userInput()
    factorial(userNumber)
'''
factorial function accepts value as int type
loops through the range from one to the value inclusively 
and multiplies all values together to get the factorial.
displays factorial
'''
def factorial(value):
    fac = 1
    for i in range(1,value + 1):
        fac = fac * i
    print('The factorial of ',value,' is ',fac, sep='')

'''
userInput function receives input from user
if user input is not an int, ask user for input again
if user input is an int, return value
'''
def userInput():
    userNum = input('Enter a number to get the factorial: ')
    while testInput(userNum):
        userNum = input('Please enter a number to get the factorial: ')
    return int(userNum)

'''
testInput function to see if user enters a number or not
accepts a single value of any type
returns whether or not program errs out on cast to int
'''
def testInput(value):
    try:
        int(value)
        return False
    except:
        return True


main()