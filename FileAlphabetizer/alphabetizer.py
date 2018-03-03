filename = input('Input filename (without extension):\n')

fileIn = open(str(filename) + '.txt', 'r')
lines = []

for line in fileIn:
    lines.append(line)

lines.sort()

fileOut = open(str(filename) + '_sorted.txt', 'w')
for line in lines:
    fileOut.write(line)

print('Lines in file: ' + str(len(lines)))
print('File Sorted!')

fileIn.close()
fileOut.close()
