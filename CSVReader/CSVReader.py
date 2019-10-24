import sys

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

if sys.version_info[0] < 3:
    sys.exit("Must be run with Python 3\nExiting...")

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    sys.exit("Usage: python CSVReader.py <filename.csv> [options]")

if ".csv" not in filename:
    sys.exit("Filename must have .csv extension")

sort_col = -1
headers = False
if len(sys.argv) > 2:
    for arg in sys.argv:
        if "sort" in arg:
            sort_col = int(arg.split('=')[1])-1
            print("Sorting by column: " + str(sort_col+1))
        elif arg == "headers":
            headers = True

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

# if headers are not included, remove
if not headers:
    arr.pop(0)

# if needed, sort arr
if sort_col >= 0 and sort_col < num_col:
    arr.sort(key=lambda x: float(x[sort_col]) if is_number(x[sort_col]) else x[sort_col].lower(), reverse=True if is_number(arr[1][sort_col]) else False)
elif sort_col >= 0:
    print("Invalid sort collumn")

printer = ""
# print column letters
printer += "+-----"
for col in cell_wid:
    printer += '+'
    printer += '-' * (col+2)
printer += "+\n"
printer += "|     "
# for each collumn in current row
for ind in range(len(line)):     
    # print vertical line
    printer += '| '
    printer += str(ind+1).rjust(cell_wid[ind])
    printer += ' '
printer += "|\n"

line_num = 1
# for each row in array
for line in arr:
    # print horizontal line
    printer += "+-----"
    for col in cell_wid:
        printer += '+'
        printer += '-' * (col+2)
    printer += "+\n"

    # print row numbers 
    printer += "|" + str(line_num).rjust(5)
    line_num += 1
    
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
printer += "+-----"
for col in cell_wid:
    printer += '+'
    printer += '-' * (col+2)
printer += "+\n"

print(printer)

fin.close()
