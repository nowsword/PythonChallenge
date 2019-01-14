file = open('2.in')
L = []
D = {}
for line in file:
    for char in line[:-1]:
        if char in D:
            D[char] += 1
        else:
            D[char] = 1
            L.append(char)
for char in L:
    print('%r: %d' % (char, D[char]))
file.close()
