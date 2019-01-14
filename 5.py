import pickle

file = open('5.in', 'rb')
data = pickle.load(file)
file.close()

file = open('5.out', 'w')
for x in data:
    for y in x:
        file.write(y[1] * y[0])
    file.write('\n')
file.close()
