def getChain(number):
    length = 1
    while True:
        if number % 2 == 0:
            number = number/2
            length += 1
        else:
            number = (3*number) + 1
            length += 1
        if number == 1:
            break
    return length

def main():
    list = []
    for x in range(1, 1000000):
        print(x)
        test = getChain(int(x))
        list.append(test)
    print(max(list))

if __name__ == "__main__":
    main()
    