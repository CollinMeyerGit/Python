import random
password = ""
stringFull = ""
tempList = []
def pick(pickLetters, pickNumbers, pickSymbols):
    if pickLetters.lower() == 'y':
        randLetter = random.randint(0,25)
        tempList.append(randLetter)
    if pickNumbers.lower() == 'y':
        randNumbers = random.randint(26, 35)
        tempList.append(randNumbers)
    if pickSymbols.lower() == 'y':
        randSymbol = random.randint(36, 43)
        tempList.append(randSymbol)
    randPick = random.randint(0, ((len(tempList))-1))
    numChar = tempList[randPick]
    return numChar
    #USER INPUTS
print('Welcome to my password generator')
num = input('How many charecters would you like your password to have?: ')
pickLetters = input('Do you want letters?(Y/N): ')
pickNumbers = input('Do you want numbers?(Y/N): ')
pickSymbols = input('Do you want symbols?(Y/N): ')
    #LIST OF POSSIBLE CHARECTERS
chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
't','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','!','@','#','$','%','&','*','?']
var = 0
while(var < int(num)):
    numChar = pick(pickLetters, pickNumbers, pickSymbols)
    stringOne = chars[numChar]
    stringFull = stringFull + stringOne
    var = var + 1
print(stringFull)