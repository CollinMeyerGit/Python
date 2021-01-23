from tkinter import filedialog
def getData(file):
    lines = (open(file)).readlines()
    return lines
def main():
    count = 0
    total = 0
    lines = getData(filedialog.askopenfilename())
    fixed = []
    for i in lines:
        fixed.append(i.rstrip())
    for i in fixed:
        if i == '':
            count = 0
            print('\n')
        else:
            temp = i.split(' ')
            for i in temp:
                check = i[0:3]
                print(check)
                if (check == 'byr') or (check == 'iyr') or (check == 'eyr') or (check == 'hgt') or (check == 'hcl') or (check == 'ecl') or (check == 'pid'):
                    count += 1
        if count == 7:
            total += 1
    print(total)
    
if __name__ == "__main__":
    main()