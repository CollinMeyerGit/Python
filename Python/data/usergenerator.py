import random
chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
'n','o','p','q','r','s','t','u','v','w','x','y','z','0','1',
'2','3','4','5','6','7','8','9','!','@','#','$','%','&','*','?']
def createPass(length):
    password = ""
    idx = 0
    while(idx <= int(length)):
        spot = random.randint(0,43)
        pick = chars[spot]
        password = password + pick
        idx = idx + 1
    return password
def buildNames():
    names = []
    file = open("names.txt", "r")
    for x in file:
        stripped = x[0:(len(x) - 2)]
        names.append(stripped)
    return names

def main():
    users = {}
    names = buildNames()
    for x in names:
        passLength = random.randint(5,15)
        password = createPass(passLength)
        users.update({x: password})
    print(users)
if __name__ == "__main__":
   main()
