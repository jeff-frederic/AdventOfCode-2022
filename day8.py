
with open('day8.in') as file:
    data = [row.strip() for row in file.readlines()]

rows = len(data)            # num of rows
columns = len(data[0])      # num of columns

edges = (rows * 2) + ((columns - 2) * 2)    # trees visible from edges
total = edges                               # total trees visible

for row in range(1, rows-1):
    for col in range(1, columns-1):
        tree = data[row][col]

        left = max([data[row][col-i] for i in range(1, col+1)])
        right = max([data[row][col+i] for i in range(1, columns-col)])
        up = max([data[row-i][col] for i in range(1, row+1)])
        down = max([data[row+i][col] for i in range(1, rows-row)])

        if (left < tree or right<tree or up<tree or down<tree):
            total += 1

print("Answer to part 1: ", total)
