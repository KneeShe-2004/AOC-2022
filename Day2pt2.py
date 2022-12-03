line = ""
blank = []
score = 0


f = open('Day2-Input.txt', 'r')
lines = f.readlines()
numberoflines = len(lines)

f.close()

f = open('Day2-Input.txt', 'r')

for x in range(numberoflines+1):
    line = f.readline()

    blank = line.split(" ")
    
    if blank[0] == 'A' and blank[1] == 'X\n':
        score = score + 3

    if blank[0] == 'A' and blank[1] == 'Y\n':
        score = score + 4

    elif blank[0] == 'A' and blank[1] == 'Z\n':
        score = score + 8

    elif blank[0] == 'B' and blank[1] == 'X\n':
        score = score + 1
    
    elif blank[0] == 'B' and blank[1] == 'Y\n':
        score = score + 5
    
    elif blank[0] == 'B' and blank[1] == 'Z\n':
        score = score + 9
    
    elif blank[0] == 'C' and blank[1] == 'X\n':
        score = score + 2
    
    elif blank[0] == 'C' and blank[1] == 'Y\n':
        score = score + 6
    
    elif blank[0] == 'C' and blank[1] == 'Z\n':
        score = score + 7
f.close()

print(score)