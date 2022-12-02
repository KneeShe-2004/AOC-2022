counter = 0
string = ""
list = []
x = 0

f = open('Day1-Input.txt', 'r')

lines = f.readlines()
numberOfLines = len(lines)

f.close()

f = open('Day1-Input.txt', 'r')

for x in range(numberOfLines):
    string = f.readline()
    if string == "\n":
        list.append(counter)
        counter = 0
        continue

    counter = counter + int(string)

list.sort()

print(list)

f.close()