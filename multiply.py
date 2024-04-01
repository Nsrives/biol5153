#! /usr/bin/env python3

# ask for the size of the multiplicatino matrix
y = int(input('enter a number '))

# calculate how many spaces we will need for the output of each cell
cell_width = len(str((y * y))) + 1

# nested for loop to calculate i * j
for i in range(1, y+1): 
    for j in range(1, y+1):
        print("{:>{cell_width}}".format(i*j, cell_width = cell_width), end='\t')
# print a newline character at the end of each row 
    print()

