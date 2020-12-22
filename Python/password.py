# this program accepts a password and checks it against the correct password
password = "easyaccess"
i = 1
while(i < 5):
    enteredPassword = input('Enter Password:')
    if enteredPassword == password:
        print('Correct')
        i = 10
    else:
        print('incorrect')
        i = i + 1
        
       

