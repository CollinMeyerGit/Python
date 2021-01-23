terms = int(input("please enter number of fibancii terms: "))
if terms == 1:
    print("0")
else:
    numFirst = 0
    numSecond = 1
    print(str(numFirst) + "\n" + str(numSecond))
    for x in range (terms - 2):
        printed = numFirst + numSecond
        print(printed)
        numFirst = numSecond
        numSecond = printed