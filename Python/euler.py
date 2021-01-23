def getData():
    text = open("nums.txt")
    lines = text.readlines()
    fixed = []
    for x in lines:
        current = (x.rstrip()).split(' ')
        for i in current:
            
getData()