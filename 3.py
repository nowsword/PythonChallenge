import re
file = open('3.in')
pattern = r'([^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z])|(^[A-Z]{3}[a-z][A-Z]{3}[^A-Z])|([^A-Z][A-Z]{3}[a-z][A-Z]{3}$)|(^[A-Z]{3}[a-z][A-Z]{3}$)'
for line in file:
    line = line.strip()
    for res in re.findall(pattern, line):
        for x in res:
            if x == '':
                continue
            if x[3] >= 'a' and x[3] <= 'z':
                print(x[3], end='')
            else:
                print(x[4], end='')
print()
file.close()
