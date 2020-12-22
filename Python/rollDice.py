
#This program takes in 


import sys
import random
    #ASCII representations of the different dice face to print
def printOne():
    print('|---------|\n')
    print('|         |\n')
    print('|    *    |\n')
    print('|         |\n')
    print('|_________|\n')
def printTwo():
    print('|---------|\n')
    print('|  *      |\n')
    print('|         |\n')
    print('|      *  |\n')
    print('|_________|\n')
def printThree():
    print('|---------|\n')
    print('|       * |\n')
    print('|    *    |\n')
    print('| *       |\n')
    print('|_________|\n')
def printFour():
    print('|---------|\n')
    print('|  *   *  |\n')
    print('|         |\n')
    print('|  *   *  |\n')
    print('|_________|\n')
def printFive():
    print('|---------|\n')
    print('|  *   *  |\n')
    print('|    *    |\n')
    print('|  *   *  |\n')
    print('|_________|\n')
def printSix():
    print('|---------|\n')
    print('|  *   *  |\n')
    print('|  *   *  |\n')
    print('|  *   *  |\n')
    print('|_________|\n')
    
    #Function for using roll input to print the dice
    
def getRoll(number):
    for x in range(number):
        roll = random.randint(1,6)
        if roll == 1:
            printOne()
        elif roll == 2:
            printTwo()
        elif roll == 3:
            printThree()
        elif roll == 4:
            printFour()
        elif roll == 5:
            printFive()
        elif roll == 6:
            printSix()

    #Either uses command line argument or user input in program to determine roll number

try:
    sys.argv[1]
except IndexError:
    number = input('Please enter number of dice you want roll:')
    number = int(number)
    getRoll(number)
else:
    number = sys.argv[1]
    number = int(number)
    getRoll(number)