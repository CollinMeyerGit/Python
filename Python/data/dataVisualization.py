def getData():
    data = []
    rows = int(input("how many rows of data do you have: "))
    idx = 0
    while(idx < rows):
        data.append(int(input("data point: ")))
        idx += 1
    return data

def printData(data):
    print("\n" * 3)
    for x in (data):
        print(("*" * x) + "\n")

def sort(data):
    data.sort()
    return data
data = getData()
data = sort(data)
printData(data)