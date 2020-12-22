# This takes a username and password to login users
def login():
    print("Welcome to login")
    usernames = []
    passwords = []

    with open('usernames.txt', 'r') as filehandle:
        for line in filehandle:
            currentPlace = line[:-1]
            usernames.append(currentPlace)

    with open('passwords.txt', 'r') as filehandle:
        for line in filehandle:
            currentPlace = line[:-1]
            passwords.append(currentPlace)
    i = 1
    while(i == 1):
        print("To make a new account type new for the username")
        inputUser = input('Username: ')
        if inputUser.lower() == 'new':
            newUser = input('Please enter a new username: ')
            usernames.append(newUser)
            with open('usernames.txt', 'a') as filehandle:
                filehandle.write('%s\n' % newUser)
            newPass = input('Password: ')
            passwords.append(newPass)
            with open('passwords.txt', 'a') as filehandle:
                filehandle.write('%s\n' % newPass)
            print('ACCOUNT ADDED!\n')
        else:
            if usernames.count(inputUser) == 0:
                print('That username does not exist\n')
            else:
                inputPass = input('Please enter your password: ')
                userPosition = usernames.index(inputUser)
                checkPass = passwords[userPosition]
                if inputPass == checkPass:
                    print('Logged in')
                    i = 2
                else:
                    print('That password is incorrect')
    return inputUser