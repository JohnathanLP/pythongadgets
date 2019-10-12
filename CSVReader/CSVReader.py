import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    sys.exit("Usage: python CSVReader.py <filename.csv>")

if ".csv" not in filename:
    sys.exit("Filename must have .csv extension")

fin = open(filename, "r")

arr = []

for line in fin:
    arr.append(line.replace("\n",''))
for ind in range(len(arr)):
    arr[ind] = arr[ind].split(',')

# calculate max number of collumns in a row
num_col = 0;
for line in arr:
    if len(line) > num_col:
        num_col = len(line)

# calculate max number of char in each collumn
cell_wid = [0] *num_col
for line in arr:
    for ind in range(len(line)):
        if len(line[ind]) > cell_wid[ind]:
            cell_wid[ind] = len(line[ind])

printer = ""
# for each row in array
for line in arr:
    # print horizontal line
    for col in cell_wid:
        printer += '+'
        printer += '-' * (col+2)
    printer += "+\n"

    # for each collumn in current row
    for ind in range(len(line)):     
        # print vertical line
        printer += '| '

        # print entry
        printer += line[ind].rjust(cell_wid[ind])
        printer += ' '
    printer += "|\n"

    # print last vertical line

# print last horizontal line
for col in cell_wid:
    printer += '+'
    printer += '-' * (col+2)
printer += "+\n"

print(printer)

fin.close()
