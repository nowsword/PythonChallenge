def translate(string):
    start = ord('a')
    maps = str.maketrans({chr(start + x) : chr(start + (x + 2) % 26) for x in range(26)})
    return string.translate(maps)

file = open('1.in')
for line in file:
    print(translate(line), end = '')
file.close()
