#! /usr/bin/env python3

y = int(input('enter a number '))

for i in range(1, y+1): 
    for j in range(1, y+1):
        print(i*j, end='\t')
    print()

